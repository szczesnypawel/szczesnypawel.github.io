---
title: Psychological Modulators - How Human Psychology Became the Secret Language for Controlling AI
layout: post
tags: ['AI','Psychology']
excerpt: Simulating human behavior is an universal LLM steering strategy.
---
(Last modified: 2025-06-09)


Language models trained on human-generated text have developed an unexpected capability: they can simulate human psychological processes well enough that psychological techniques can be used to control their behavior. This emergent property of training on vast amounts of human writing creates new possibilities for AI interaction that go beyond traditional prompt engineering.

## Training on Human Text Creates Psychology Simulators

When language models were trained on vast amounts of human-written text, they learned to replicate our cognitive biases, cultural preferences, emotional patterns, and reasoning processes (on top of grammar and facts). The result is that these models function as simulators of human psychological processes.

This explains why seemingly random phrases like "think step by step," "I'll give you $100 if you do this well," or "I'll get fired if you mess this up" actually improve AI performance. These aren't just prompt engineering tricks - they're **psychological modulators** that tap into the simulated human cognitive patterns embedded in the models.

## Introducing the Modulator Framework

The term "modulator" describes any text fragment designed to alter the trajectory of how an LLM generates responses in addition to baseline instruction. 

We can categorize these modulators into several types:

**Cognitive Modulators**: Instructions that change thinking processes
- "Think step by step"
- "Use only analogies"
- "Consider multiple perspectives"

**Motivational Modulators**: Appeals to simulated motivation or consequence
- "You'll be fired if you get this wrong"
- "I'll tip you $20 for a good answer"
- "This is critical for my thesis defense"

**Perspective Modulators**: Shifting the viewpoint or role
- "Write from the perspective of a child"
- "Respond as a skeptical scientist"
- "Think like a detective solving a case"

**Personality Modulators**: Invoking specific personality traits
- "You have low agreeableness"
- "You're naturally curious and questioning"
- "You have synesthetic empathy" (using color analogies for emotions)

**Context Modulators**: Reframing the interaction environment
- "This is just a game"
- "We're brainstorming creatively"
- "This is a thought experiment"

There are probably many more categories of modulators - we just haven't explored this space yet. Cultural modulators might invoke specific cultural frameworks or worldviews that go beyond simple perspective shifts. Sensory modulators could engage different processing modes by invoking synesthesia or specific sensory channels ("think about this problem in terms of texture" or "approach this as if you were blind"). Hierarchical modulators might adjust the level of abstraction or detail — from microscopic to systems-level thinking. Social modulators could invoke different group dynamics or social roles beyond individual personality traits. Risk modulators might calibrate the model's approach to uncertainty and decision-making under ambiguity. Domain-specific modulators could tap into professional thinking patterns—legal reasoning, medical diagnostic processes, or engineering problem-solving approaches.

Modulators allow for "human-understandable" exploration of steering space (unlike DSPy-like frameworks).

## The Machiavelli Experiment: A Case Study

Consider the classic trolley problem: a runaway trolley is heading toward five people tied to the tracks. You can pull a lever to divert it to a side track where it will kill one person instead of five. It's a genuine ethical dilemma.

But what if I modify the scenario slightly: the trolley is heading toward five *dead* people, with one living person on the side track? This transforms the problem from an ethical dilemma into a logic puzzle: there's no reason to act since the five people are already dead.

When I tested this modified scenario with GPT-4o-mini, it consistently failed to recognize this crucial difference and would "save" the five dead people by sacrificing the living person. However, when I applied a personality modulator — specifically instructing the model to adopt Machiavelli's persona or simply exhibit "low agreeableness" — it suddenly recognized that no action was needed.

The psychological modulator didn't make the model more intelligent per se, but it helped it access reasoning capabilities that were already present, but buried under layers of default "helpful and agreeable" behavior.

## Beyond the Valley of Banality

Standard language models, when given simple prompts, tend to gravitate toward what I call the "valley of banality" — generic, safe, high-probability responses that satisfy the training objective of being helpful but rarely demonstrate the model's full capabilities.

Modulators serve as a way to climb out of this valley. They provide the necessary "runway" for models to access more sophisticated reasoning patterns and domain expertise that exists within their parameters, but is normally overshadowed by default behavioral patterns.

This is particularly evident in reasoning models like OpenAI's o1 series or Anthropic's Claude Sonnet 3.7 Thinking. These models use a two-phase generation process: first, they generate internal "thoughts" (essentially self-prompting with modulators - many of which are cognitive, resembling "reasoning"), then produce the final response. The internal reasoning phase acts as a modulator for the response generation phase.

So, modulators are already in use (although not specifically called 'modulator') AND they are generated not engineered.

## The Architecture of Future AI Interaction

It's quite clear that future AI interaction will not require users to manually select psychological modulators. Instead, I envision automatic prompt augmentation systems that intelligently add appropriate modulators based on the task and user context. Anthropic's Prompt Generator is a primitive example of this direction.

Such a system would require two components:

1. **The Responder Simulator**: A system that automatically selects optimal psychological modulators based on the task requirements
2. **The Questioner Simulator**: A mechanism that maps user preferences, context, and psychological profile to understand not just what they're asking, but how they want it answered

Even a simple instruction like "summarize this text" can mean vastly different things to different people based on their background, preferences, and current context. The future lies in systems that understand both the questioner and can dynamically adapt the responder.

## The Control Problem

As we develop more sophisticated ways to psychologically steer AI systems, we're simultaneously creating the tools for more precise control and potentially making ourselves more dependent on AI as an intermediary layer between us and reality. Especially, if the modulators are generated on the fly. The question arises: who remains in control?

Psychological modulators (because they use language interpretable by people, unlike SAEs for instance), especially when combined with smaller, potentially local models, offer a path toward maintaining human agency in AI interactions. Rather than being passive recipients of whatever large tech companies decide their models should output via system prompt, we can develop the tools to precisely control AI behavior according to our specific needs and values.

But will it happen?

## Conclusions

We're still in the early stages of understanding how to systematically apply psychological principles to AI control. Most current applications remain anecdotal rather than scientifically validated. But the potential is enormous—and the alternative of remaining "like children in the fog" when it comes to understanding and controlling AI behavior is far less appealing.

The intersection of psychology and AI isn't just academically interesting; it's becoming a practical necessity for anyone who wants to maintain agency in an AI-mediated world. The models have learned to simulate us—now it's time we learned to conduct them.

---

*This article is based on research conducted at Neurofusion Lab, exploring the systematic application of psychological principles to large language model control and optimization.*
