"""
test_skill_structure.py - Verifies repository integrity and structure.
"""

import os
import unittest

REQUIRED_FILES = [
    'README.md',
    'SKILL.md',
    'LICENSE',
    'SECURITY.md',
    'CHANGELOG.md',
    'references/ponytail_pragmatics.md',
    'references/gauntlet_audit_ledger.md',
    'references/ai_and_llm_security.md',
    'references/web_and_cloud_security.md',
    'scripts/check_environment_config.py',
    'scripts/audit_tenancy.sql'
]

class TestSkillStructure(unittest.TestCase):

    def setUp(self):
        self.root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    def test_required_files_exist(self):
        for rel_path in REQUIRED_FILES:
            full_path = os.path.join(self.root_dir, rel_path)
            self.assertTrue(os.path.isfile(full_path), f"Missing required file: {rel_path}")

    def test_skill_frontmatter(self):
        skill_md_path = os.path.join(self.root_dir, 'SKILL.md')
        with open(skill_md_path, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertTrue(content.startswith('---'), "SKILL.md must start with YAML frontmatter delimiter '---'")
            self.assertIn('name: batmaningotham', content, "SKILL.md frontmatter must contain 'name: batmaningotham'")
            self.assertIn('description:', content, "SKILL.md frontmatter must contain 'description:'")

if __name__ == '__main__':
    unittest.main()
