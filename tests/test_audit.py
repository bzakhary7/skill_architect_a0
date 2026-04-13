import asyncio
import json
import sys
import os

# Add plugin root to py path so we can import properly
plugin_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, plugin_root)

from tools.skill_architect_tool import SkillArchitectTool

async def main():
    print("Initializing SkillArchitectTool...")
    tool = SkillArchitectTool()
    
    print("Testing skill_parse command...")
    # We will test parsing SKILL.md of the skill_architect itself
    kwargs = {"skillPath": os.path.join(plugin_root, "skills", "skill_architect")}
    response = await tool.execute(command="skill_parse", **kwargs)
    
    print("Response:")
    if response.message:
        print(response.message)
        print("TEST PASSED")
    else:
        print(response.error)
        print("TEST FAILED")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
