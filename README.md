# SkillArchitect

SkillArchitect is an advanced Agent Zero plugin that radically transforms how agent skills are engineered. By moving away from brittle, ad-hoc skill authoring and one-shot AI prompts, SkillArchitect employs structured evaluation, iterative benchmarking, and precise prompt tuning to enforce reliability and performance at scale.

## Acknowledgments & Lineage
This project is deeply indebted to the open-source community. It is a direct adaptation of the excellent [opencode-skill-creator](https://github.com/antongulin/opencode-skill-creator) repository published by Anton Gulin. The core structure, evaluation logic, and tuning methodology were originally inspired by Anthropic Claude's own internal `skill-creator` architecture. 

SkillArchitect proudly encapsulates and extends this powerful legacy by wrapping the advanced testing infrastructure into a modular, Store-Ready Agent Zero plugin.

## Why SkillArchitect?
Creating skills manually or asking an AI to "write a skill to do X" often results in brittle mechanics. Standard skill creation suffers from common pitfalls:
- They are **over-fitted** to specific prompts, failing outside standard queries.
- They **under-trigger** because the LLM doesn't have the appropriate contextual cues mapped inside the skill to know *when* to invoke it.
- They invoke behaviors that are too rigid or break quietly on edge cases.

In contrast, SkillArchitect introduces a rigorous, automated engineering workflow that guarantees exponentially higher-quality skills:
- **Test-Driven Benchmarking:** Rather than guessing if a skill works, you curate a set of mock evaluations and assertions. SkillArchitect concurrently runs test queries across different skill iterations, meticulously logging token efficiency, performance durations, and empirical assertion pass rates.
- **Trigger Optimization:** A skill is entirely useless if the agent ignores it. To combat under-triggering, the plugin maps out a spectrum of synthesized test prompts (including "near misses" that shouldn't trigger the skill) and recursively rewrites the frontmatter `description` using a mathematical train/test split. It optimizes the text over several loops until precision hits a verifiable maximum.
- **Blind Comparison Pass:** Using statistical aggregation, SkillArchitect runs blind "baseline vs. new-skill" evaluations, comparing the outputs side-by-side using an independent model grader to surface underlying flakiness or regressions.
- **Iterative Improvement:** As you tweak the markdown instructions or remove redundant phrasing, you gain immediate, dashboard-style statistical insights on the quantitative impact to your validation suite.

## Technical Mechanics
- **Local Persistence Sandbox:** Leverages Agent Zero install directives (`hooks.py`) to isolatedly clone down necessary runtime dependencies via NPM in the exact execution folder, bypassing framework clutter while effortlessly surviving full-system docker restarts.
- **Native A0 Validation:** Safely invokes background Node modules without bypassing typing guardrails, strictly executing Python `ToolResult` API patterns bound dynamically back to the parent execution environment.

## Usage
Simply invoke Agent Zero through the main interface and ask to build, audit, or optimize an existing skill. The active prompt framework will automatically surface the SkillArchitect tools.

## License
Open-sourced under the [Apache 2.0 License](LICENSE).
