# Ponytail Security Pragmatics (Lazy Senior Dev Mindset)

The **Ponytail** mindset applies extreme efficiency and pragmatic engineering to security and code reviews: *The best code is the code never written, and the best security fix is the smallest diff at the root cause.*

---

## 🧗 The 7 Rungs of Security Remediation

When fixing a security flaw or refactoring code, stop at the first rung that holds:

1. **Does this feature need to exist at all? (YAGNI)**
   - Remove dead endpoints, unused admin routes, or unneeded data collection. Deletion is the ultimate security fix.
2. **Does an existing security middleware / DB policy already cover it?**
   - Reuse current RLS policies, auth guards, or validation schemas instead of writing duplicate checks.
3. **Does the native framework or standard library solve it?**
   - Use built-in framework security (e.g. Next.js middleware, Web Crypto API, Postgres RLS, standard ORM parameterization). Never invent custom cryptography or homegrown auth encoders.
4. **Does an installed, vetted dependency solve it?**
   - Use existing dependencies (`zod`, `jose`, `bcrypt`, `helmet`) instead of custom regexes or parsers.
5. **Can this be solved at the root bottleneck (Single Point of Enforcement)?**
   - Patch the shared database RPC, RLS policy, or API middleware once. One guard at the source is smaller and safer than 15 client-side checks.
6. **Can the fix be a single-line constraint?**
   - A SQL `CHECK` constraint, a Zod `.max(100)`, or a `NOT NULL` constraint is cleaner than multi-line imperative validation code.
7. **Only then: Write the minimum imperative code that seals the hole.**

---

## 📜 Core Rules

* **Root Cause > Symptom Patching:**
  - A bug report names a symptom (e.g. "User can edit payment status on form X"). Grep every caller and fix the table policy or backend handler once. Patching only the reported frontend component leaves sibling paths vulnerable.
* **No Frontend-Only Security:**
  - Disabling a UI button or hiding a form is UX, not security. If it isn't enforced in backend API routes or database RLS, it doesn't exist.
* **Deletion Over Addition:**
  - Boring over clever. Fewest modified files possible. Shortest working diff wins.
* **Minimal Runnable Self-Check:**
  - Fixes without a check are unfinished. Leave behind the smallest runnable test or script (e.g., a Vitest unit check or a negative DB query) that fails if the vulnerability reopens.
* **Known Ceilings Comment:**
  - If a pragmatic simplification is made (e.g. rate limit using in-memory store before Redis is added), mark it with a `// ponytail: <ceiling> -> <upgrade path>` comment.
