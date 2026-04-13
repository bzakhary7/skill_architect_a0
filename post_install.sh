#!/usr/bin/env bash

# SkillArchitect post-install script
# Install Node dependencies locally to survive container updates.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/node_logic" && npm install
