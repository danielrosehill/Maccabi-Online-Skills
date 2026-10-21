---
name: travel-insurance
description: 'Open Maccabi''s travel-abroad insurance redirect (ביטוח נסיעות לחו"ל), which hands the member''s medical record to the insurer''s purchase flow. Only after explicit confirmation. Use for ''buy travel insurance through Maccabi''.'
license: MIT
compatibility: Claude Code with Claude in Chrome and the user's own signed-in Maccabi Online session (online.maccabi4u.co.il). Unofficial; not affiliated with Maccabi. Reads profiles/maccabi-online.json and reference/ from this repository.
---

# Travel insurance redirect

Route: `/sonline/directorship/travelabroadinsurance/`.

The portal redirects to the travel-insurance purchase flow **and passes the member's
medical record along**, so pre-existing conditions arrive already filled in. That is
the reason to use this route rather than going to the insurer directly. It is also
why opening it counts as a write: it sends data to a third party.

## Steps

1. Preflight steps 1–4 on any portal page. Confirm the member.
2. Tell the user, in one sentence, that opening the link shares the member's medical
   information with the insurer. Wait for a yes.
3. Navigate to the route and report where it landed: the final host and page title.
4. You may read the quote screens. **Never enter payment details or buy.** Hand those
   steps to the user.

## Status

U: the route was supplied by the user and was deliberately not opened during
discovery (2026-10-21). On the first real run, record the landing host in the profile.

## Provenance

Observed 2026-10-21 in a signed-in session; route `travel_insurance` in `profiles/maccabi-online.json` (status there). Handles: URL grammar (rung 1), H1 and visible label text (rung 4/6). Re-verify with `admin-rediscover-portal`.
