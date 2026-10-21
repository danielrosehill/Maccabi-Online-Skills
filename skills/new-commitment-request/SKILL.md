---
name: new-commitment-request
description: Start a new commitment request (בקשת התחייבות / hitchaivut, Form 17) in Maccabi Online — choose the correct service type, fill it in, submit after confirmation. Use for 'request a hitchaivut', 'I need a Form 17 for an MRI', 'commitment for surgery'.
---

# New commitment request (hitchaivut / Form 17)

Route: `/sonline/requestsAndApprovals/ObligationRequest/Triage/`. H1: `בקשת התחייבות`.
Prompt: `לאיזה שירות מבוקשת ההתחייבות?`. **Choosing the right sub-type matters.**
It decides who processes the request and which documents are asked for.

| Option | Use for |
|---|---|
| `מרפאות חוץ ומכונים (ניתוחים ואשפוזים)` | Hospital outpatient clinics and institutes, including surgery and admissions |
| `דימות (PET-CT, CT, MRI)` | Imaging: PET-CT, CT, MRI |
| `ביקור במיון או פינוי אמבולנס` | ER visit or ambulance transport |
| `בקשה לאביזר ניידות` | Mobility aid (wheelchair, walker etc.) |
| `אחר` | Anything else |

## Steps

Run `${CLAUDE_PLUGIN_ROOT}/reference/preflight.md` first (browser, URL, page check, whose record).

1. Preflight. Confirm the member.
2. Ask what the commitment is for, map it onto the table, and confirm the option with
   the user if there is any doubt.
3. Select the option by its label and press `המשך`.
4. Fill in the fields the next screen asks for (usually provider, referral, documents)
   with the user. File uploads need the user to name the file.
5. Write gate, then submit.
6. Report the confirmation. Follow-up is in `request-status`.

## Write gate

This skill reaches a **write** control. Follow `${CLAUDE_PLUGIN_ROOT}/reference/write-actions.md`: fill, read back, get an explicit yes for this action, submit once.

## Provenance

Observed 2026-10-21 in a signed-in session; route `obligation_request` in `profiles/maccabi-online.json` (status there). Handles: URL grammar (rung 1), H1 and visible label text (rung 4/6). Re-verify with `admin-rediscover-portal`.
