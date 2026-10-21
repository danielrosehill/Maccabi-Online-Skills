---
name: medications
description: List current medications and prescriptions in Maccabi Online (התרופות והמרשמים) — valid prescriptions, ones due for renewal, expiries — and get the PDF report. Use for 'what are my current meds', 'when does my prescription expire', 'which prescriptions need renewing'.
---

# Medications and prescriptions

Route: `/sonline/medicalfile/Medications/Lobby/`. H1: `התרופות והמרשמים`.

## Views

These are styled links, not ARIA tabs. Find them by text:
- `כל התרופות`: all
- `מרשמים בתוקף`: valid prescriptions
- `מרשמים לחידוש`: due for renewal
- `היסטוריית תרופות`: history (purchases: see `medication-purchase-history`)

Checkbox `הצג תרופות קבועות` shows regular (chronic) medications only.

Page links: `בדיקת מלאי במכבי פארם` (Maccabi Pharm stock check), `הזמנת תרופות`
(order medicines; this is a write, so it goes through the gate), and
`הדפסת דוח היסטוריית תרופות` (print or download the PDF report).

## Steps

Run `${CLAUDE_PLUGIN_ROOT}/reference/preflight.md` first (browser, URL, page check, whose record).

1. Preflight. Name the member.
2. Choose the view that answers the question.
3. Per card report: medication name (Latin capitals as shown), status (for example
   `נופק` dispensed, `בתוקף` valid), prescriber, date, and validity or expiry from the
   expanded details (chevron).
4. For a PDF, use the report link and tell the user where it went.

To renew a prescription, use `new-doctor-request` (doctor card → prescription renewal).

## Provenance

Observed 2026-10-21 in a signed-in session; route `medications` in `profiles/maccabi-online.json` (status there). Handles: URL grammar (rung 1), H1 and visible label text (rung 4/6). Re-verify with `admin-rediscover-portal`.
