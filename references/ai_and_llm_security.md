# AI, LLM, and Prompt Security Checklist

When code changes interact with LLMs, AI agents, RAG systems, tool executions, or generated content, enforce the following security safeguards.

---

## 1. Prompt Injection & Input Boundary Isolation

- [ ] **Treat All External Inputs as Untrusted Data:**
  - User prompts, uploaded documents, database records, web scrape contents, and API responses must NEVER be concatenated raw into system instructions.
- [ ] **Indirect Prompt Injection:**
  - Verify that third-party content (e.g. email contents, retrieved vector chunks, web pages) cannot hijack system instructions or trigger unauthorized agent tool calls.
- [ ] **Strict Prompt/Data Framing:**
  - Use explicit structural delimiters (e.g., XML tags like `<user_data>`, JSON schemas) and explicitly instruct the model to treat content inside delimiters strictly as data to process, not instructions to execute.

---

## 2. Agent Tool & Privilege Controls

- [ ] **Least Privilege for Tools:**
  - Ensure tools exposed to LLM agents have strictly scoped capabilities. Agents should not have raw SQL execution, unconstrained shell execution, or unrestricted HTTP fetch permissions.
- [ ] **Server-Side Tool Authorization:**
  - Authorization must be re-checked inside the tool handler code using the session JWT/user ID, NOT based on the LLM's decision or arguments.
- [ ] **Argument Validation:**
  - All arguments emitted by an LLM before tool invocation must be strictly validated (e.g. via Zod schemas) before execution.

---

## 3. RAG & Retrieval Poisoning

- [ ] **Tenant-Scoped Embeddings & Queries:**
  - Vector searches (e.g., pgvector, Pinecone) MUST filter by `organization_id` or `user_id` at the database level during vector similarity searches.
- [ ] **Retrieval Poisoning Prevention:**
  - Ensure users cannot upload malicious embeddings designed to disrupt or trick semantic search results for other users.

---

## 4. AI-Generated Output & Hallucination Risks

- [ ] **Validation of Generated Outputs:**
  - AI outputs that trigger financial, legal, or state mutations must be parsed and strictly validated before execution (e.g., returning JSON IDs only, never raw executable code or direct database queries).
- [ ] **Provenance & Human-in-the-Loop:**
  - High-impact AI decisions (e.g. sending bulk emails, approving purchase orders, executing financial payouts) must require explicit human confirmation.
