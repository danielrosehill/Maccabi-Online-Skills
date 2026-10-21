---
name: public-appeal
description: Use Maccabi's public enquiries/complaints form (פניות הציבור, no login needed) to follow up on something stuck in the portal. Use for 'complain to Maccabi', 'escalate my request', 'contact Maccabi public enquiries'.
---

# Public enquiries form

URL: `https://www.maccabi4u.co.il/forms/public-appeal/`. Title: `פניות הציבור מכבי`.
No session needed.

A second channel for following up on requests that stall inside the portal, such as
a commitment or refund with no answer, or a message with no reply.

## Steps

1. Open the form in the browser and read its fields.
2. Draft the enquiry with the user: what was requested, when, the request type, what
   has (not) happened, and what they want. Add reference numbers only if the user
   supplies them.
3. Filling in the member's personal details is data entry for the user. Show every
   value before entering it, and submit only after an explicit yes (write gate).
4. Report the confirmation or reference number.

## Write gate

This skill reaches a **write** control. Follow `${CLAUDE_PLUGIN_ROOT}/reference/write-actions.md`: fill, read back, get an explicit yes for this action, submit once.

## Provenance

Observed 2026-10-21 in a signed-in session; route `public_appeal` in `profiles/maccabi-online.json` (status there). Handles: URL grammar (rung 1), H1 and visible label text (rung 4/6). Re-verify with `admin-rediscover-portal`.
