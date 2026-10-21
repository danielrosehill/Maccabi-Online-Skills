---
name: visit-summaries
description: 'Find and download visit summaries (סיכומי ביקור) written by clinicians in Maccabi Online. Use for ''get the summary of my last doctor''s visit'', ''download the visit summary from [date]'', ''what did the doctor write''.'
license: MIT
compatibility: Claude Code with Claude in Chrome and the user's own signed-in Maccabi Online session (online.maccabi4u.co.il). Unofficial; not affiliated with Maccabi. Reads profiles/maccabi-online.json and reference/ from this repository.
---

# Visit summaries

Route: `/sonline/appointmentOrder/VisitSummary/Lobby/`. H1: `סיכומי ביקור`.

The page notes that a summary appears only once the doctor has written it, and that
not every visit gets one.

Filters: `סינון לפי שנים` (year) and `חיפוש לפי שם / תחום` (search by clinician or
specialty).

## Steps

Run `${CLAUDE_PLUGIN_ROOT}/reference/preflight.md` first (browser, URL, page check, whose record).

1. Preflight. Name the member.
2. Narrow by year and search as the request needs.
3. Per card report: date, clinician, specialty, and whether a document is attached
   (paperclip). Each card also has a `זימון תור חדש` link (a write: book-appointment).
4. Open the summary with the card's chevron. For a download, use the attachment and
   tell the user where it went.

## Provenance

Observed 2026-10-21 in a signed-in session; route `visit_summaries` in `profiles/maccabi-online.json` (status there). Handles: URL grammar (rung 1), H1 and visible label text (rung 4/6). Re-verify with `admin-rediscover-portal`.
