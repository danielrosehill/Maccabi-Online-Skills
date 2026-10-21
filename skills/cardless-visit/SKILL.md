---
name: cardless-visit
description: Get a cardless-visit approval (ביקור ללא כרטיס) in Maccabi Online — valid 14 hours — for a forgotten/lost card, or when a clinician or the phone line asks the member to issue one so they can access the record. Requested only after confirmation.
---

# Cardless visit approval

Route: `/sonline/directorship/NoCardVisit/Lobby/`. H1: `ביקור ללא כרטיס`.

This is used more widely than the name suggests. Besides a forgotten card, a doctor
or the phone line may ask the member to issue one so they can open the member's
record remotely.

**Terms (page text, 2026-10-21):**
- The approval is valid for **14 hours** and is registered in Maccabi's systems, so
  request it as close to the visit as possible.
- It is billed like a card visit; quarterly levies apply where they would.
- It does not book an appointment.
- It is not valid at labs or imaging institutes.

**Reasons (pick one):** `שכחתי כרטיס` (forgot), `הכרטיס אבד` (lost), `כרטיס לא תקין`
(faulty), `הכרטיס נגנב` (stolen), `אחר` (other). For a clinician or phone-line
request, use the reason the user gives you, or `אחר`.

## Steps

Run `${CLAUDE_PLUGIN_ROOT}/reference/preflight.md` first (browser, URL, page check, whose record).

1. Preflight. **Confirm the member.** The approval is issued for whoever is selected.
2. Ask the reason and when the visit is (warn if it is more than ~14 h away).
3. Select the reason by label. Write gate: state the member, the reason and the
   14-hour window.
4. Press `לקבלת אישור` once.
5. Read back the approval exactly as shown (number, validity) and give it to the user.
   Do not store it anywhere.

## Write gate

This skill reaches a **write** control. Follow `${CLAUDE_PLUGIN_ROOT}/reference/write-actions.md`: fill, read back, get an explicit yes for this action, submit once.

## Provenance

Observed 2026-10-21 in a signed-in session; route `no_card_visit` in `profiles/maccabi-online.json` (status there). Handles: URL grammar (rung 1), H1 and visible label text (rung 4/6). Re-verify with `admin-rediscover-portal`.
