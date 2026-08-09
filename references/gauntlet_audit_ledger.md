# Gauntlet Audit Ledger & Hostile Verification Protocol

The **Gauntlet** protocol enforces an un-cheatable, proof-driven audit process. It assumes every input is malicious and every claim of "safe code" is guilty until proven innocent by empirical verification.

---

## 🔒 Configuration Privacy & Abstract Protocol

> **CRITICAL DIRECTIVE:** The agent MUST NOT read, request, print, log, or reproduce sensitive runtime configuration values or environment strings in audit reports. All verification results MUST be structural and abstract.

---

## 🛡️ The Honest Ledger Rule

> **"Verified" means a test, a live query, an automated static check, or a direct line-by-line read of the compiled asset — NEVER "the code looks safe", "the comment says it checks X", or "the UI works in a browser demo".**

---

## 🎯 Hostile Audit Vectors

When reviewing code, actively attempt to break the implementation using these vectors:

1. **Direct API / Supabase Bypass:**
   - Can an attacker bypass the frontend completely by calling `/rest/v1/table` or API endpoints directly with the public anon key or user JWT?
2. **Cross-Tenant ID Swapping (IDOR & Isolation Failure):**
   - If User A submits User B's `organization_id`, `restaurant_id`, `supplier_id`, or `inventory_item_id`, does the backend perform operations on User B's data?
3. **Privilege Escalation & Role Matrix Bypass:**
   - Can a `staff` or `member` role user execute `admin` / `owner` operations (e.g. updating payout settings, deleting categories, changing prices)?
4. **Race Conditions & Concurrency (TOCTOU):**
   - Are read-then-write operations (e.g. inventory depletion, account balance deductions, voucher redemptions) atomic in SQL/transactions, or can concurrent requests cause race condition double-spending?
5. **Unit & Math Discrepancies:**
   - Are unit conversions (e.g., `g` vs `kg`, `ml` vs `L`) enforced? Do integer over/under-flows or floating-point rounding errors expose financial or logic flaws?
6. **Unauthenticated State Mutations:**
   - Are order placement, payment claim, password reset, or invoice creation endpoints protected with valid tokens, signatures, or HMACs?

---

## 🚥 Severity Matrix & Definition of Done

Assign exact severities to all discovered issues:

| Severity | Impact Criteria | Examples |
|:---|:---|:---|
| **P0 (Critical)** | System compromise, cross-tenant data leakage, unauthenticated data corruption, financial forgery | Direct REST write allowing arbitrary money values; cross-tenant SQL write; auth bypass |
| **P1 (High)** | Privilege escalation, draft data exposure, bypassable authorization, unverified tenant pointers | Staff modifying payout config; draft endpoints exposed publicly; unvalidated FK pointers |
| **P2 (Medium)** | Non-atomic race conditions, missing rate limits on sensitive endpoints, unvalidated unit strings | Racy inventory depletion; lack of rate limits on OTP/login; missing write validation |
| **P3 (Low)** | Code hygiene, minor info disclosure, hardening opportunities | Verbose error stack traces; missing security headers; unindexed RLS columns |

---

## 📝 Definition-of-Done Verification Matrix

Before declaring any review or remediation complete, populate the DoD Ledger:

| Target Component | Vulnerability ID | Vulnerability Description | Fix Applied | Proof of Verification (Command / Test / Query) | Status |
|:---|:---|:---|:---|:---|:---|
| *Component Name* | *P0-1* | *Description of flaw* | *Exact remediation file* | *Vitest / SQL Query / structural assertion* | **VERIFIED** |
