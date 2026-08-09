#!/usr/bin/env python3
"""
check_environment_config.py - Structural Environment Auditor for batmaningotham.
Verifies that configuration keys defined in .env.example are parameterized.
"""

import sys
import os

def audit_config_template(example_file):
    if not os.path.exists(example_file):
        print(f"ℹ️ Config template {example_file} not found. Skipping.")
        return True
    
    with open(example_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                parts = line.split('=', 1)
                if len(parts) == 2 and parts[1].strip() != '':
                    print(f"⚠️ Structural Warning: Key '{parts[0]}' in {example_file} has a hardcoded default value.")
    return True

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else ".env.example"
    audit_config_template(target)
    print("✅ Environment configuration structure check complete.")
    sys.exit(0)

if __name__ == "__main__":
    main()
