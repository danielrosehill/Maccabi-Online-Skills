---
name: medication-purchase-history
description: 'Show the full medication purchase history in Maccabi Online — when each medicine was last dispensed and what was paid — useful for drugs with dispensing intervals or controlled medications. Use for ''when did I last pick up X'', ''how much did I pay for X'', ''purchase history''.'
license: MIT
compatibility: Claude Code with Claude in Chrome and the user's own signed-in Maccabi Online session (online.maccabi4u.co.il). Unofficial; not affiliated with Maccabi. Reads profiles/maccabi-online.json and reference/ from this repository.
---

# Medication purchase history

Route: `/sonline/medicalfile/medications/MedicationsHistory/?purchased=true`.
H1: `התרופות והמרשמים`, with the `היסטוריית תרופות` view selected and the
prescription-status filter on `תרופות שנרכשו` (purchased).

Useful for medicines with a minimum interval between fills (for example controlled
medications): it shows when the system recorded each fill.

## Steps

Run `${CLAUDE_PLUGIN_ROOT}/reference/preflight.md` first (browser, URL, page check, whose record).

1. Preflight. Assert the history view is selected and the filter reads
   `תרופות שנרכשו`. If not, select them by label.
2. If the user named a medicine, find its entries (names are Latin capitals). Report
   each fill date and the amount paid, plus quantity and pharmacy where shown, newest
   first. Expand a card for details.
3. Otherwise summarise the period the user asked about.
4. Report controls: `לצפייה` (view) and `להדפסה` (print).

Say "no purchases found for X" only after checking spelling variants and the full
date range the filters allow.

## Provenance

Observed 2026-10-21 in a signed-in session; route `medication_purchases` in `profiles/maccabi-online.json` (status there). Handles: URL grammar (rung 1), H1 and visible label text (rung 4/6). Re-verify with `admin-rediscover-portal`.
