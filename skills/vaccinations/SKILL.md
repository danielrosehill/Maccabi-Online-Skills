---
name: vaccinations
description: 'Read the vaccination record (חיסונים) in Maccabi Online and download the vaccination booklet PDF. Use for ''what vaccines has my son had'', ''download my vaccination record'', ''when was the last tetanus shot''.'
license: MIT
compatibility: Claude Code with Claude in Chrome and the user's own signed-in Maccabi Online session (online.maccabi4u.co.il). Unofficial; not affiliated with Maccabi. Reads profiles/maccabi-online.json and reference/ from this repository.
---

# Vaccinations

Route: `/sonline/medicalfile/Vaccinations/Lobby/`. H1: `חיסונים`. This page has
**no** member suffix in the H1; read the member from the switcher or from the card
label `חיסונים עבור <name>`.

## Steps

Run `${CLAUDE_PLUGIN_ROOT}/reference/preflight.md` first (browser, URL, page check, whose record).

1. Preflight. Read the member from the switcher.
2. Per card report the vaccine name and date, newest first (the page's order).
3. The full booklet is `פנקס החיסונים שלי` → `לצפייה` (PDF).

For children, Tipat Halav (טיפת חלב, the Ministry of Health's well-baby clinics)
keeps a parallel record. If a childhood vaccine is missing here, say it may be
recorded there.

## Provenance

Observed 2026-10-21 in a signed-in session; route `vaccinations` in `profiles/maccabi-online.json` (status there). Handles: URL grammar (rung 1), H1 and visible label text (rung 4/6). Re-verify with `admin-rediscover-portal`.
