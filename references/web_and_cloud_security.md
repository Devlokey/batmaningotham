# Web, Cloud & Database Security Checklist

This document contains deep-dive verification standards for Web APIs, Cloud Infrastructure, Database RLS, Environment Configuration, and Compliance.

---

## 1. Database & Multi-Tenancy Isolation (Supabase / Postgres RLS)

- [ ] **Role-Aware RLS Write Policies:**
  - Verify that RLS `INSERT`, `UPDATE`, and `DELETE` policies enforce role permissions (e.g. `auth_can(restaurant_id, 'settings:write')`), not just simple organization membership.
- [ ] **Immutable Tenant Keys:**
  - Ensure foreign keys defining tenant ownership (e.g. `org_id`, `tenant_id`) cannot be updated via PostgREST or API requests. Use `BEFORE UPDATE` triggers or `REVOKE UPDATE (org_id)`.
- [ ] **Security Definer Function Hardening:**
  - `SECURITY DEFINER` RPCs must explicitly set `search_path = public, pg_temp` and revoke `EXECUTE` from `PUBLIC` unless strictly public.
  - Every RPC MUST validate input arguments against caller ownership before executing operations.

---

## 2. API Security & Input Validation

- [ ] **Server-Side Pricing & Money Integrity:**
  - Never trust client-supplied item prices, totals, or discounts in order/checkout endpoints. Always re-calculate totals server-side against database prices.
- [ ] **HMAC & Signed Tokens for State Mutations:**
  - Money-adjacent or unauthenticated claim operations (e.g. "I've paid" claims) MUST require signed tokens/HMACs generated server-side at creation. Use constant-time comparison (`crypto.timingSafeEqual`).
- [ ] **Rate Limiting & Abuse Protection:**
  - Auth, OTP, invoice processing, AI endpoints, and file uploads must have strict per-IP / per-user rate limits and request size limits.

---

## 3. Environment Configuration & Parameter Isolation

- [ ] **Environment Variable Isolation:**
  - Ensure all runtime configuration parameters (API endpoints, private keys, database strings) are loaded via environment variables (`process.env`) rather than inline code string literals.
- [ ] **Constant-Time Comparison for Hash Signatures:**
  - Webhooks, cron verification tokens, and HMAC signatures must be compared using constant-time algorithms (`crypto.timingSafeEqual`) to prevent timing side-channel attacks.
- [ ] **Data Minimization & Log Sanitization:**
  - Sensitive user data (PII, credit card info, passwords) must never appear in application logs or client-side error responses.
