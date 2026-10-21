---
name: admin-rediscover-portal
description: Admin/maintenance: re-explore the signed-in Maccabi Online portal with Claude in Chrome, detect moved or renamed routes, labels and options, and update profiles/maccabi-online.json and the affected skills — without committing any personal data. Use when a skill reports CHANGED, or periodically.
---

# Admin: rediscover the portal and update the skills

The portal's UI changes without notice. This skill re-maps it from a live signed-in
session and brings `profiles/maccabi-online.json` and the skills back in line. Run it
from a clone of this repo, not from an installed copy.

## 0. Ground rules

- Read only. Never submit, send, acknowledge, book or cancel while mapping. The
  travel-insurance route stays unopened (it shares data).
- Human pace, one tab, no parallel fan-out.
- **Nothing personal enters the repo.** The session belongs to a real member. Record
  routes, H1 titles, option labels and page structure only. Never record names, ID
  numbers, `relative=` / `sr_id=` / `req=` values, 6+ digit path segments, doctor
  names, dates or record contents. Run `scripts/pii_check.py` before every commit.

## 1. Probe the known routes

For each `routes.*.path` in the profile (skip `travel_insurance`):
1. Navigate, wait 3–5 s (8 s for `request_status`).
2. Classify the page as in `reference/preflight.md`. Record: OK / 404 page / H1 changed
   (new H1 text with the ` - <member>` suffix removed).
3. For routes with `options`, `tabs` or `filters`, read the current labels with
   `get_page_text` and diff them against the profile.

## 2. Walk the side menu for new routes

1. On the home page, `find` each collapsed section button in the side menu (for
   example `תיק רפואי`, `זימון וביטול תורים`, `החזרים אישורים והתחייבויות`,
   `פעולות נוספות`) and expand it by reference.
2. Collect every menu link as (visible text, path). Sanitise each one:
   - unwrap `/go/<encoded>` to the inner path,
   - drop the whole query string,
   - prefix `/sonline` if missing,
   - discard any link whose path contains a 6+ digit run.
3. Diff against the profile: list new links and links that disappeared.

## 3. Update

1. Edit the profile: fix paths, H1s and labels; add new routes with status `U`;
   set `verified` and each touched route's `status` to `V <today>`.
2. Edit the skills whose tables quote the changed labels (grep the old label across
   `skills/`).
3. For a new route the user wants as a skill, add `skills/<name>/SKILL.md` in the
   same shape as its neighbours (preflight, steps, write gate if any, provenance).
4. Bump `version` in `.claude-plugin/plugin.json` (minor for new skills, patch for
   fixes), and the marketplace entry if the description changed.

## 4. Check and ship

```bash
python3 scripts/pii_check.py         # must print OK
python3 -m json.tool profiles/maccabi-online.json > /dev/null
git diff                             # read it: labels and paths only
```

Commit with a message that says which routes changed (no personal data), then push.
Report to the user: routes OK / moved / gone / new, and which skills were edited.
