---
name: book-appointment
description: Start booking a new appointment in Maccabi Online (זימון תור חדש) — with a clinician seen in the last year or via the service search — and book only after confirmation. Use for 'book a doctor's appointment', 'get me an appointment with <specialty>', 'find a slot with my GP'.
---

# Book an appointment

Route: `/sonline/appointmentOrder/NewAppointment/`. H1: `זימון תור חדש`.
Prompt: `מה ברצונך לעשות?`. There are two paths, each with its own `המשך` button:

1. `זימון תור לרופאים/ות והמטפלים/ות אצלם ביקרת בשנה האחרונה`: book with a
   clinician the member saw in the last year. Fastest for a regular GP or paediatrician.
2. `חיפוש ואיתור שירותי בריאות`: search doctors, therapists, labs, urgent care,
   vaccinations and medical centres.

A seasonal banner (for example flu vaccine booking) may sit above these. Ignore it
unless it is what the user wants.

## Steps

Run `${CLAUDE_PLUGIN_ROOT}/reference/preflight.md` first (browser, URL, page check, whose record).

1. Preflight. Confirm which member the appointment is for.
2. Pick the path: the user's own clinician → path 1; a new specialty or service → path 2.
3. Click that card's `המשך` by reference. Read the clinicians or services offered,
   then the available slots. Present the options (date, time, clinician, location),
   earliest first, and let the user choose.
4. Write gate before the final booking confirmation.
5. Report the confirmed slot. Check it with `upcoming-appointments`.

The family doctor's own page (`my-doctor`) also has a `לזימון תור` button.

## Write gate

This skill reaches a **write** control. Follow `${CLAUDE_PLUGIN_ROOT}/reference/write-actions.md`: fill, read back, get an explicit yes for this action, submit once.

## Provenance note

Landing verified 2026-10-21. The slot-selection screens were not exercised, so
describe what you see there.

## Provenance

Observed 2026-10-21 in a signed-in session; route `new_appointment` in `profiles/maccabi-online.json` (status there). Handles: URL grammar (rung 1), H1 and visible label text (rung 4/6). Re-verify with `admin-rediscover-portal`.
