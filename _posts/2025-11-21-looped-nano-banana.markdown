---
title: Looped Nano Banana via Replicate
layout: post
categories: ['Experiments']
tags: ['video-generation', 'replicate', 'nano-banana', 'script']
description: Using Replicate's nano-banana model to generate video frames with mood modifiers by adding steering phrases to a looped prompt that creates temporal continuity. 
---

Nano Banana can be effectively steered when generating consecutive frames via adding steering phrase or word to the classic: "The same scene but 0.1 seconds in the future" looped prompt.

The video below was created from a starting frame with mood modifiers: "calm,calmer,excited,angry,peaceful". Commands and script below.

{% include embed/youtube.html id='ozRi0pK4cSs' %}


`python nano_banana_timelapse.py --input-image 9d0yrttezsrm80ctjbwvvdn0nm.jpeg --steps 50 --flow calm,calmer,excited,angry,peaceful`

`ffmpeg -i timelapse_2fps.mp4 -vf "minterpolate=fps=48:mi_mode=mci:me_mode=bidir:mc_mode=aobmc:vsbmc=1" -c:v libx264 -preset slow -crf 18 timelapse_2fps_interpolated.mp4`


```python
#!/usr/bin/env python3
"""
Generate a short video by repeatedly editing an image with Replicate's
google/nano-banana model using the fixed prompt
"The same scene but 0.1 seconds in the future".

Requirements:
- Environment variable REPLICATE_API_TOKEN must be set.
- python -m pip install replicate pillow httpx (ffmpeg CLI must be available).

Example:
    REPLICATE_API_TOKEN=... python nano_banana_timelapse.py \\
        --input-image photo.png --steps 16
"""

import argparse
import base64
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import replicate
import httpx
from PIL import Image
from replicate.helpers import FileOutput

MODEL_REF = "google/nano-banana"
DEFAULT_PROMPT = "The same scene but 0.1 seconds in the future"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Iteratively edit an image with google/nano-banana and build a video."
    )
    parser.add_argument(
        "--input-image",
        required=True,
        help="Path to the starting image (any format supported by Pillow).",
    )
    parser.add_argument(
        "--steps",
        type=int,
        default=10,
        help="How many future frames to generate (default: 10).",
    )
    parser.add_argument(
        "--output-dir",
        default="nano_banana_runs",
        help="Directory where frames and the final video will be saved.",
    )
    parser.add_argument(
        "--aspect-ratio",
        default="4:3",
        help="Aspect ratio passed to the model (default: 4:3).",
    )
    parser.add_argument(
        "--output-format",
        choices=["jpg", "png", "webp"],
        default="jpg",
        help="Image format requested from the model (default: jpg).",
    )
    parser.add_argument(
        "--frame-rate",
        type=int,
        default=12,
        help="Frame rate of the generated video (default: 12).",
    )
    parser.add_argument(
        "--prompt",
        default=DEFAULT_PROMPT,
        help="Prompt sent to the model (default matches the requirement).",
    )
    parser.add_argument(
        "--flow",
        help="Optional comma-separated words to blend into the prompt over the run.",
    )
    return parser.parse_args()


def ensure_token() -> None:
    if not os.environ.get("REPLICATE_API_TOKEN"):
        print("Error: REPLICATE_API_TOKEN is not set.", file=sys.stderr)
        sys.exit(1)


def build_output_dirs(base_dir: str) -> tuple[Path, Path]:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = Path(base_dir) / f"nano_banana_{timestamp}"
    frames_dir = run_dir / "frames"
    frames_dir.mkdir(parents=True, exist_ok=True)
    return run_dir, frames_dir


def convert_to_format(src: Path, dst: Path, image_format: str) -> None:
    pil_format = "JPEG" if image_format.lower() == "jpg" else image_format.upper()
    with Image.open(src) as img:
        img.save(dst, format=pil_format)


def fetch_bytes_from_output(output_obj: Any) -> bytes:
    if isinstance(output_obj, FileOutput):
        return output_obj.read()
    if isinstance(output_obj, (list, tuple)):
        if not output_obj:
            raise RuntimeError("Model returned an empty output list.")
        return fetch_bytes_from_output(output_obj[0])
    if isinstance(output_obj, str):
        if output_obj.startswith("data:"):
            _, encoded = output_obj.split(",", 1)
            return base64.b64decode(encoded)
        response = httpx.get(output_obj, timeout=120)
        response.raise_for_status()
        return response.content
    raise TypeError(f"Unsupported output type: {type(output_obj)!r}")


def save_frame(data: bytes, path: Path) -> None:
    with open(path, "wb") as handle:
        handle.write(data)


def parse_flow_words(flow: str | None) -> list[str]:
    if not flow:
        return []
    return [word.strip() for word in flow.split(",") if word.strip()]


def build_frame_prompts(base_prompt: str, steps: int, flow_words: list[str]) -> list[str]:
    if not flow_words:
        return [base_prompt] * steps
    prompts = []
    buckets = len(flow_words)
    for step_index in range(steps):
        bucket_index = (step_index * buckets) // steps
        prompts.append(f"{base_prompt}, {flow_words[bucket_index]}")
    return prompts


def generate_frame(
    client: replicate.Client,
    current_image: Path,
    next_frame_path: Path,
    prompt: str,
    aspect_ratio: str,
    output_format: str,
) -> None:
    with open(current_image, "rb") as image_file:
        prediction = client.run(
            MODEL_REF,
            input={
                "aspect_ratio": aspect_ratio,
                "image_input": [image_file],
                "output_format": output_format,
                "prompt": prompt,
            },
        )
    frame_bytes = fetch_bytes_from_output(prediction)
    save_frame(frame_bytes, next_frame_path)


def build_video(frames_dir: Path, video_path: Path, frame_rate: int, extension: str):
    pattern = str(frames_dir / f"frame_%03d.{extension}")
    cmd = [
        "ffmpeg",
        "-y",
        "-framerate",
        str(frame_rate),
        "-i",
        pattern,
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        str(video_path),
    ]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError as exc:
        raise RuntimeError("ffmpeg is not installed or not in PATH.") from exc
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(f"ffmpeg failed: {exc.stderr.decode('utf-8', 'ignore')}") from exc


def main() -> None:
    args = parse_args()
    ensure_token()

    input_path = Path(args.input_image)
    if not input_path.exists():
        print(f"Error: Input image '{input_path}' does not exist.", file=sys.stderr)
        sys.exit(1)
    if args.steps < 1:
        print("Error: --steps must be at least 1.", file=sys.stderr)
        sys.exit(1)

    flow_words = parse_flow_words(args.flow)
    frame_prompts = build_frame_prompts(args.prompt, args.steps, flow_words)

    run_dir, frames_dir = build_output_dirs(args.output_dir)
    extension = args.output_format.lower()

    print(f"Saving run artifacts to {run_dir}")

    initial_frame = frames_dir / f"frame_000.{extension}"
    convert_to_format(input_path, initial_frame, extension)

    client = replicate.Client()

    current_frame = initial_frame
    for step in range(1, args.steps + 1):
        target_path = frames_dir / f"frame_{step:03d}.{extension}"
        print(f"Generating frame {step:03d} -> {target_path.name}")
        generate_frame(
            client,
            current_frame,
            target_path,
            frame_prompts[step - 1],
            args.aspect_ratio,
            args.output_format,
        )
        current_frame = target_path

    video_path = run_dir / "timelapse.mp4"
    print("Building video with ffmpeg...")
    build_video(frames_dir, video_path, args.frame_rate, extension)
    print(f"Done! Video saved to {video_path}")


if __name__ == "__main__":
    main()


```
