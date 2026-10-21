---
name: test-results
description: Read lab and test results in Maccabi Online (תוצאות בדיקות) — all results, latest lab values, tracked tests — and open the result PDFs. Use for 'my blood test results', 'latest lab results', 'did the results come back'.
---

# Test results

Route: `/sonline/testsResults/TestsResults/lobby/?quickAction=1`. H1: `תוצאות בדיקות`.

## Tabs

- `תוצאות בדיקות`: all results, one card per test or visit, with a PDF (`לצפייה`)
- `תוצאות מעבדה אחרונות`: latest lab values
- `בדיקות במעקב שלי`: tests the member tracks over time

Filters: `סוג בדיקה` (test type), `לפי שנים` (year), `נקה סינון` (clear).

## Steps

Run `${CLAUDE_PLUGIN_ROOT}/reference/preflight.md` first (browser, URL, page check, whose record).

1. Preflight. Name the member.
2. Pick the tab that fits the question. For "latest blood tests" use
   `תוצאות מעבדה אחרונות`.
3. Report test name, date, value, units and reference range, plus whatever flag the
   page shows for out-of-range values. Do not interpret results clinically beyond
   restating the page's own flags. Suggest the doctor for interpretation.
4. To get the PDF, click that card's `לצפייה` by reference; it opens or downloads the
   document.

## Provenance

Observed 2026-10-21 in a signed-in session; route `test_results` in `profiles/maccabi-online.json` (status there). Handles: URL grammar (rung 1), H1 and visible label text (rung 4/6). Re-verify with `admin-rediscover-portal`.
