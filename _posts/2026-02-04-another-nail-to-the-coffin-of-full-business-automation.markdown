---
title: "Another nail to the coffin of *full business automation with LLMs*"
layout: post
categories: ['LLM Research']
tags: ['llm', 'ai-safety', 'anthropic', 'research', 'training-data']
description: "Another nail to the coffin of \"full business automation with LLMs\". Some were saying this for years."
---

Increased capabilities of LLMs together with iterative looping systems (like OpenClaw/Clawdbot recent hype) are used to push a narrative that full business automation is within a reach. "It just needs a better context engineering bro" kind of thing. 

But here come two constraints of machine learning field:
1. Most approaches rarely generalize outside of distribution of training data (and we have more and more evidence that LLMs aren't an exception).
2. The larger the model the less predictable failures are.

On Alignment Science Blog of Anthropic there is a new article covering small research study on that very topic. Authors asked a question: "When AI systems fail, will they fail by systematically pursuing the wrong goals, or by being a hot mess?" In other words, they asked if models have tendency to systematically pursuit goals its constructors didn't train them to pursue.

Results aren't unexpected. I think I've heard that story from people in LLM-sceptic camp many times.

Incoherent responses (a proxy for unpredictable failures) correlate with "reasoning" effort and task complexity. The longer LLM generates "thinking" tokens or the more difficult task is, the more likely LLM will fail in an unpredictable way.

Real world is a mess. Data never comes clean and tidy. Complexity rears its ugly head often. It all makes machine learning models (including LLMs) behave unpredictably.

Until we find another architecture for AI, this is unlikely to change. 

This isn't an issue when things that an AI system does 1.) do not have large consequences or 2.) are easily reversible or 3.) verification of correctness is inexpensive. But typical business has plenty of places where none of the these is true. 

So the trend among AI practitioners seems to be to either enmesh AI into existing business fabric (provided that the fabric exists in a form of processes, frameworks or SOPs) or to build a business from scratch that has none of these three constraints on AI tasks. An example of the latter could be a faceless AI YouTube channels earning revenue from ads. 

But getting an existing messy business from no AI to full AI automation where the only thing CEO does manually is a morning coffee and all employees are automated away is still a science fiction. Or marketing speech of people who overinvested in AI labs and they seek somebody to dump shares on.
