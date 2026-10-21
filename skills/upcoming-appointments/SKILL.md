---
name: upcoming-appointments
description: List upcoming booked appointments in Maccabi Online (תורים עתידיים). Use for 'what appointments do I have', 'when is my next doctor's appointment', 'does my son have anything booked'. Cancelling is gated.
---

# Upcoming appointments

Route: `/sonline/appointmentOrder/FutureAppointments/Lobby/`. H1: `תורים עתידיים`.

## Steps

Run `${CLAUDE_PLUGIN_ROOT}/reference/preflight.md` first (browser, URL, page check, whose record).

1. Preflight. The `סינון לפי חבר/ה` filter can show all linked members or one. Say
   which you used.
2. For each card report: member, date, time, clinic type, clinician, location.
3. To cancel or change, the page says to click the appointment details. Cancelling
   is a write, so run it through the gate.

If the list is empty after hydration, say there are no upcoming appointments for that
member/filter. Only say this once the page has fully rendered.

## Write gate

This skill reaches a **write** control. Follow `${CLAUDE_PLUGIN_ROOT}/reference/write-actions.md`: fill, read back, get an explicit yes for this action, submit once.

## Provenance

Observed 2026-10-21 in a signed-in session; route `future_appointments` in `profiles/maccabi-online.json` (status there). Handles: URL grammar (rung 1), H1 and visible label text (rung 4/6). Re-verify with `admin-rediscover-portal`.
