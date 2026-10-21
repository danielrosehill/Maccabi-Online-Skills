---
name: request-status
description: 'Check the status of administrative requests in Maccabi Online — commitments (התחייבות / Form 17), refunds, medicine pre-approvals (החזרים אישורים והתחייבויות). Use for ''was my hitchaivut approved'', ''status of my refund'', ''any news on the Form 17''.'
license: MIT
compatibility: Claude Code with Claude in Chrome and the user's own signed-in Maccabi Online session (online.maccabi4u.co.il). Unofficial; not affiliated with Maccabi. Reads profiles/maccabi-online.json and reference/ from this repository.
---

# Request status (hitchaivut, refunds, approvals)

Route: `/sonline/requestsAndApprovals/StatusRequest/Lobby/`. H1:
`החזרים אישורים והתחייבויות`.

A **hitchaivut** (התחייבות, Form 17 / טופס 17) is Maccabi's payment commitment to a
provider (hospital, imaging institute, specialist) for a service.

## Steps

Run `${CLAUDE_PLUGIN_ROOT}/reference/preflight.md` first (browser, URL, page check, whose record).

1. Preflight. This page hydrates slowly. Wait up to ~8 s and re-read before
   concluding the list is empty.
2. Use `מיין לפי` to sort or filter if useful.
3. For each request report: type (for example `בקשה להתחייבות`), service or
   provider, date submitted, current status, and whether a document such as the
   approved commitment is attached. Expand the item for details only when asked.
4. If the user wants the approved commitment, open its attachment and tell them it is
   available. It is a PDF the user can download.

To file a new request use `new-commitment-request`, `refund-request`, or the
`הגשת בקשה חדשה` dropdown on this page.

## Provenance

Observed 2026-10-21 in a signed-in session; route `request_status` in `profiles/maccabi-online.json` (status there). Handles: URL grammar (rung 1), H1 and visible label text (rung 4/6). Re-verify with `admin-rediscover-portal`.
