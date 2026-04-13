import subprocess
import os

def install():
    """Called by framework after plugin is placed in usr/plugins/."""
    print("Installing SkillArchitect Node.js dependencies...")
    plugin_dir = os.path.dirname(os.path.abspath(__file__))
    node_logic_dir = os.path.join(plugin_dir, "node_logic")
    try:
        subprocess.run(["npm", "install"], cwd=node_logic_dir, check=True)
        print("SkillArchitect Node dependencies installed.")
    except Exception as e:
        print(f"Failed to install NPM dependencies: {e}")
