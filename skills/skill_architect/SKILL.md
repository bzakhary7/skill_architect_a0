---
name: "skill-architect"
description: "Advanced engineering tool for refactoring and auditing Agent Skills."
tools: ["skill_architect_tool.py"]
---

# Skill Engineer Operational Protocol

This skill provides a structured interface for the SkillArchitect Skill Creator CLI via a Python wrapper. It is designed to harden "DeepThought" server logic and compress agent instructions.

## Operational Instructions

### 1. Tool Identification
**Primary Tool:** `skill_architect_tool.py`
**Method:** Do NOT use shell execution. Invoke the Python tool directly.

### 2. Refactor Workflow
When requested to "Refactor" a skill (e.g., SearXNG or Shelfmark):
1. **Analyze:** Use the tool with the `refactor` command to identify "Logic Leaks."
2. **Apply Semantic Compression:** The tool will suggest a high-density markdown structure.
3. **Harden Triggers:** Ensure the tool adds unique prefixes (e.g., `searxng:`) to prevent cross-skill conflicts.

### 3. Automated Evaluation (Evals)
Before overwriting any skill:
- **Command:** `eval`
- **Action:** The tool will simulate 5-10 "Edge Case" scenarios.
- **Requirement:** A skill MUST pass the Eval with >90% accuracy before being promoted to the production `/skills/` folder.

## Usage Example

```python
# To audit the SearXNG skill
skill_architect_tool.execute(
    command="audit", 
    skill_path="usr/skills/searxng/SKILL.md",
    focus=["semantic_compression", "trigger_hardening"]
)
