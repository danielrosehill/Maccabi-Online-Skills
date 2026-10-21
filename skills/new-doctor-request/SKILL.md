---
name: new-doctor-request
description: 'Draft and (after confirmation) send a new request via Maccabi Online — a message to the doctor (prescription renewal, sick note, question, referral) or to the clinic office (Form 17, drug pre-approval, copies). Use for ''message my doctor'', ''ask the doctor for a prescription renewal'', ''request a sick note''.'
license: MIT
compatibility: Claude Code with Claude in Chrome and the user's own signed-in Maccabi Online session (online.maccabi4u.co.il). Unofficial; not affiliated with Maccabi. Reads profiles/maccabi-online.json and reference/ from this repository.
---

# New request to the doctor or office

Route: `/sonline/communicationWithDoctor/NewRequest/`. H1: `שליחת בקשה חדשה`.
Prompt: `איך אפשר לעזור?`. There are three cards; choosing the right one matters:

| Card (starts with) | Goes to | Covers |
|---|---|---|
| `שליחת בקשה לרופא/ה בנושאים` | The doctor (**usual choice**) | Prescription renewal or request, sick note (אישור מחלה), question to the doctor, medical-status summary, referral |
| `שליחת בקשה למשרד בנושאים` | Clinic office | Commitment (התחייבות / טופס 17), drug pre-approval, finding a service or booking, copies of documents |
| `איתור מסמכים בתיק שלך` | Nobody (self-service) | Find an existing visit summary, referral, medical certificate or test result |

## Steps

Run `${CLAUDE_PLUGIN_ROOT}/reference/preflight.md` first (browser, URL, page check, whose record).

1. Preflight. Confirm whose behalf the request is on (switch-patient if needed).
2. Map the user's need onto a card using the table. If it could be either doctor or
   office, show both and ask. If the user only needs an existing document, point them
   at `visit-summaries`, `test-results` or the referrals page instead of sending anything.
3. Doctor messages have a **per-quarter quota**. If the flow shows the remaining
   count, report it before drafting.
4. Click the card by reference, choose the sub-topic the flow offers, and draft the
   text with the user. Keep it short and factual.
5. Write gate (see below), then send.
6. Report the confirmation and tell the user they can track it with `doctor-messages`.

## Write gate

This skill reaches a **write** control. Follow `${CLAUDE_PLUGIN_ROOT}/reference/write-actions.md`: fill, read back, get an explicit yes for this action, submit once.

## Provenance note

The landing card labels were verified 2026-10-21. The screens after the card was
clicked were not opened, so describe what you see there instead of assuming a layout.

## Provenance

Observed 2026-10-21 in a signed-in session; route `new_request` in `profiles/maccabi-online.json` (status there). Handles: URL grammar (rung 1), H1 and visible label text (rung 4/6). Re-verify with `admin-rediscover-portal`.
