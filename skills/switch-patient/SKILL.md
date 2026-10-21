---
name: switch-patient
description: 'Switch which family member''s record Maccabi Online displays (מציג פרטים של). Use when the user asks about a child or other linked member, or says ''switch to [name]'' / ''show my son''s results''. Every other skill reads whichever member is selected.'
license: MIT
compatibility: Claude Code with Claude in Chrome and the user's own signed-in Maccabi Online session (online.maccabi4u.co.il). Unofficial; not affiliated with Maccabi. Reads profiles/maccabi-online.json and reference/ from this repository.
---

# Switch patient

The account holder can view linked members (typically children). The switch changes
whose record **every** page shows until switched back.

## Steps

1. Preflight steps 1–3 on any portal page (home is fine:
   `/sonline/homepage/NotificationAndUpdates/`).
2. `find` the header button whose name starts `מציג פרטים של`. Its text is the member
   currently shown.
3. If that is already the requested member, say so and stop.
4. Click it by reference. A list opens with one button per linked member; each
   button's text is the member's first name followed directly by their ID number.
5. Match the user's request against the **first name** only. If it is ambiguous or
   no match exists, list the first names (never the ID numbers) and ask.
6. Click the matching button by reference, wait 3 s, and assert that the switcher
   label and the H1 suffix now show the chosen first name. If not:
   `CHANGED: patient switch did not take effect`.
7. Tell the user who is now selected.

Never repeat ID numbers in chat unless the user asks for them, and never write them
anywhere.

## Provenance

Observed 2026-10-21 in a signed-in session; route `patient_switcher` in `profiles/maccabi-online.json` (status there). Handles: URL grammar (rung 1), H1 and visible label text (rung 4/6). Re-verify with `admin-rediscover-portal`.
