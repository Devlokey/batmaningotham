# Security Policy

## Supported Versions

Only the latest release of `batmaningotham` receives security updates and vulnerability fixes.

| Version | Supported          |
| ------- | ------------------ |
| 2.0.x   | :white_check_mark: |
| 1.0.x   | :x:                |

---

## Reporting a Vulnerability

If you discover a security vulnerability or security-relevant flaw within the `batmaningotham` skill instructions, reference checklists, or scripts:

1. **Do not create a public GitHub issue.**
2. Send a security report directly via GitHub Security Advisories or email `security@devlokey.dev` (or create a private disclosure).
3. Include detailed steps to reproduce the flaw, an example prompt/code diff, and potential impact.

---

## Security Boundaries & Guarantees

- **No Absolute Guarantees:** While `batmaningotham` applies strict OWASP, Ponytail, and Gauntlet audit principles, no automated or AI skill can guarantee 100% security against all zero-day vulnerabilities.
- **Human Verification Required:** Critical financial, legal, and tenant isolation changes should always undergo human/peer code review before deployment to production.
- **Secret Handling:** `batmaningotham` instructions explicitly prohibit printing, logging, or reproducing discovered plain-text credentials in review outputs.
