---
name: update-personal-details
description: View and (after confirmation) update personal and contact details in Maccabi Online (עדכון פרטים אישיים) — English name, contact details, accessibility and service preferences. Use for 'update my phone number with Maccabi', 'change my address on Maccabi'.
---

# Update personal details

Route: `/sonline/directorship/editinformation/profile/`. H1: `עדכון פרטים אישיים`.

The page shows a member card (name, ID, clinic, insurance tier), English-name fields,
the personalised-services and accessibility preferences, and contact details further
down.

## Steps

Run `${CLAUDE_PLUGIN_ROOT}/reference/preflight.md` first (browser, URL, page check, whose record).

1. Preflight. **Confirm the member.** Details are per member.
2. Read back the current value of the field the user wants to change.
3. Edit only that field. Write gate: show old → new, then save once.
4. Read the confirmation and report it.

Never echo the full member card (ID number etc.) back unless the user asks.

## Write gate

This skill reaches a **write** control. Follow `${CLAUDE_PLUGIN_ROOT}/reference/write-actions.md`: fill, read back, get an explicit yes for this action, submit once.

## Provenance

Observed 2026-10-21 in a signed-in session; route `edit_profile` in `profiles/maccabi-online.json` (status there). Handles: URL grammar (rung 1), H1 and visible label text (rung 4/6). Re-verify with `admin-rediscover-portal`.
