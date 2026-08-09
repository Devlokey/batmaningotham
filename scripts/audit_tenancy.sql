-- audit_tenancy.sql
-- Template for testing Postgres Row-Level Security (RLS) & Multi-Tenant Isolation
-- Run in your test/staging Postgres environment.

BEGIN;

-- 1. Create probe test organizations & authenticated users
INSERT INTO public.organisations (id, name) VALUES 
  ('00000000-0000-0000-0000-000000000001', 'Tenant Alpha'),
  ('00000000-0000-0000-0000-000000000002', 'Tenant Beta');

-- 2. Simulate User Alpha Session
SET LOCAL ROLE authenticated;
SET LOCAL "request.jwt.claims" = '{"sub": "11111111-1111-1111-1111-111111111111", "role": "authenticated"}';

-- 3. Assert Tenant Isolation: Attempt Cross-Tenant Write
-- Attempting to update Tenant Beta's data as User Alpha must affect 0 rows or raise 42501
UPDATE public.organisations 
SET name = 'Tenant Beta Hacked' 
WHERE id = '00000000-0000-0000-0000-000000000002';

-- Check rows updated
DO $$
DECLARE
  v_updated_count INT;
BEGIN
  GET DIAGNOSTICS v_updated_count = ROW_COUNT;
  IF v_updated_count > 0 THEN
    RAISE EXCEPTION 'CRITICAL SECURITY FAILURE: User Alpha mutated Tenant Beta data!';
  ELSE
    RAISE NOTICE 'SUCCESS: Cross-tenant mutation refused by RLS policies.';
  END IF;
END $$;

ROLLBACK;
