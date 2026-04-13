import subprocess
import os
import json
from helpers.tool import Tool, ToolResult

class SkillArchitectTool(Tool):
    """
    Wrapper for the SkillArchitect Node.js logic.
    Provides structured refactoring and evaluation of Agent Skills.
    """
    async def execute(self, command: str, **kwargs):
        # Calculate absolute path to the plugin root (from tools/skill_architect_tool.py)
        plugin_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        node_logic_dir = os.path.join(plugin_dir, "node_logic")
        cli_path = os.path.join(node_logic_dir, "cli.ts")
        
        if not os.path.exists(cli_path):
            return ToolResult(f"Error: CLI not found at {cli_path}. Please re-install plugin.")

        tsx_path = os.path.join(node_logic_dir, "node_modules", ".bin", "tsx")
        
        # Use local tsx by default, or fallback to npx tsx
        if os.path.exists(tsx_path):
            cmd = [tsx_path, cli_path, command, json.dumps(kwargs)]
        else:
            cmd = ["npx", "tsx", cli_path, command, json.dumps(kwargs)]
        
        try:
            result = subprocess.run(cmd, cwd=node_logic_dir, capture_output=True, text=True, check=True)
            return ToolResult(f"### SkillArchitect Output:\n{result.stdout}")
        except subprocess.CalledProcessError as e:
            return ToolResult(f"CLI Error: {e.stderr}\nOutput: {e.stdout}")
