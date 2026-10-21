---
name: find-branch
description: 'Find Maccabi medical centres / branches by city via the public service guide (serguide.maccabi4u.co.il). Use for ''Maccabi branches in Jerusalem'', ''nearest Maccabi clinic'', ''find a Maccabi medical centre in [city]''.'
license: MIT
compatibility: Claude Code with Claude in Chrome and the user's own signed-in Maccabi Online session (online.maccabi4u.co.il). Unofficial; not affiliated with Maccabi. Reads profiles/maccabi-online.json and reference/ from this repository.
---

# Find a branch / medical centre

Public service guide; no session needed. URL template:

```
https://serguide.maccabi4u.co.il/heb/medicalcentres/medicalcentressearchresults/?City={city_code}&PageNumber={page}&Source=SearchPage
```

- `City`: Israeli CBS locality code (סמל ישוב). `3000` = Jerusalem. Look up
  others from the CBS locality list, or use the site's own search page and read
  the code from the resulting URL.
- `PageNumber`: results page, starting at 1.
- `RequestId`: the site adds this on redirect; leave it out.

**Use the browser.** A plain fetch returned a bot-wall page with HTTP 200
(2026-10-21), which looks like an empty result and is not one.

## Steps

1. Build the URL and open it in Chrome.
2. Assert that the page lists medical centres for the requested city. If not:
   `CHANGED: branch results not found`.
3. Report name, address, phone and hours where shown. Page through while
   `PageNumber` returns results.

The results-page layout was not parsed on 2026-10-21. Describe what you see, and
add the fields to the profile on the first successful run.

## Provenance

Observed 2026-10-21 in a signed-in session; route `branch_finder` in `profiles/maccabi-online.json` (status there). Handles: URL grammar (rung 1), H1 and visible label text (rung 4/6). Re-verify with `admin-rediscover-portal`.
