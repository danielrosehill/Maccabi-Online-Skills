---
name: my-doctor
description: Show the member's assigned family doctor in Maccabi Online (הרופא/ה שלי) — clinic address, phones, weekly opening hours — and, only after confirmation, start a change of doctor. Use for 'who is my doctor', 'when is the clinic open', 'change my GP'.
---

# My doctor

Route: `/sonline/MedicalFile/MyDoctor/`. H1: `הרופא/ה שלי`.

Shows the assigned doctor and specialty, the clinic details (address, phone,
appointment line, fax) and a weekly hours table with columns `ימים` (day) and
`שעות פעילות` (hours). `אין קבלת קהל` means closed that day.

## Steps

Run `${CLAUDE_PLUGIN_ROOT}/reference/preflight.md` first (browser, URL, page check, whose record).

1. Preflight. Name the member (children usually have a paediatrician here).
2. Answer from the page: doctor, clinic, contact details, hours (convert the table
   into a readable weekly schedule).
3. `לזימון תור` books with this doctor; hand off to `book-appointment`.
4. `לשינוי הרופא שלי` starts a change of doctor. This is a write, and Maccabi allows
   it only periodically, so tell the user before starting it. Then follow the gate.

## Write gate

This skill reaches a **write** control. Follow `${CLAUDE_PLUGIN_ROOT}/reference/write-actions.md`: fill, read back, get an explicit yes for this action, submit once.

## Provenance

Observed 2026-10-21 in a signed-in session; route `my_doctor` in `profiles/maccabi-online.json` (status there). Handles: URL grammar (rung 1), H1 and visible label text (rung 4/6). Re-verify with `admin-rediscover-portal`.
