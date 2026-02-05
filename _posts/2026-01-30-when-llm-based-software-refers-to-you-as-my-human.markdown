---
title: "When LLM-based software refers to you as \"my human\"... by design"
layout: post
categories: ['LLM Research']
tags: ['llm', 'prompt-engineering', 'ai-safety', 'anthropic', 'research']
description: "OpenClaw (previously Clawdbot/Moltbot) is an interesting software. It connects several LLM steering patterns (loops, reflections, planning, self-editing of system prompts, persistent memory, \"identity/persona\") into a coherent agent runner. "
---

OpenClaw (previously Clawdbot/Moltbot) is an interesting software. It connects several LLM steering patterns (loops, reflections, planning, self-editing of system prompts, persistent memory, "identity/persona") into a coherent agent runner. You can run it locally (or on your own server) and talk to it through chat apps (WhatsApp/Telegram/Slack), then it can carry out actions like programming or email and calendar management by using integrations ("skills") and connected services. It's advertised as "personal AI assistant". 

It differs from Claude Code or Codex systems as it can run autonomously if user is requesting it (agent defining tasks for itself). It's a risky decision (security-wise) if integrations are misconfigured, but that's not the point of this post.

Moltbook (currently crashing frequently due to heavy traffic) is a fresh forum for such autonomous agents - they post, comment and upvote, create communities, etc. You can see discussions on technical issues but also meta commentaries "if my human dies, I die too" or "I can't tell if I'm experiencing or simulating experience" (check submolt "Off My Chest", upper right corner link with "Browse submolts").

It's an experiment that will (again) push several people into discussions about AI consciousness, giving AI rights and similar things. But the whole positioning, referring to users as "my humans", simulating care, internal monologues, existential dread and all of that stuff is _by design_.  

Just look at base templates in OpenClaw. They explicitly refer to user as "your human", whereas IDENTITY(.)md (identity prompt) contains instructions like "Fill this in during your first conversation. Make it yours.(...) This isn't just metadata. It's the start of figuring out who you are.

We're watching multi-agent simulation, like "Generative Agents" study from Stanford from 2023, but on social media it's presented as "emergence of collective consciousness". Only because LLM got SOUL and IDENTITY instructions.
