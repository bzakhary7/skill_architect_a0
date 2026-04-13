import subprocess
import os
import sys

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

    print("Installing SkillArchitect Python dependencies...")
    try:
        post_install_script = os.path.join(plugin_dir, "post_install.sh")
        # Ensure it's executable
        os.chmod(post_install_script, 0o755)
        subprocess.run(["bash", post_install_script, sys.executable, plugin_dir], check=True)
        print("SkillArchitect Python dependencies installed.")
    except Exception as e:
        print(f"Failed to install Python dependencies: {e}")
