# Preflight — run before every portal skill

Every skill in this plugin opens with these steps. They exist because the portal is a
single-page app that answers HTTP 200 for a login wall, a 404 page and an unhydrated
shell alike — the status code says nothing.

Facts (routes, H1 titles, option labels) live in `profiles/maccabi-online.json`. Read
the route's entry before navigating. If a skill and the profile disagree, the profile
wins.

## 1. Browser

Use Claude in Chrome against the user's own signed-in Chrome profile. If the
`kde-agent-workspace` plugin is available, run its `use-chrome` skill first so the
work happens on the agent's desktop rather than the user's. Open your own tab; do not
reuse the user's tabs.

Act on elements by **reference** (`find` / `read_page` → ref → click the ref). Never
click a pixel coordinate read off a screenshot.

## 2. Navigate by URL grammar

`https://online.maccabi4u.co.il` + the route's `path` from the profile. Every route
starts `/sonline/`. Without that prefix the portal shows its 404 page.

## 3. Wait, then classify the page

Wait 3–5 seconds after navigation, then read the H1 and classify:

| What you see | Meaning | Do |
|---|---|---|
| H1 starts with the route's `h1` | Right page | Continue |
| H1 `לא מצאנו את העמוד שחיפשת` | Route moved | Stop: `CHANGED: <route id> path returns the 404 page`. Suggest `admin-rediscover-portal`. |
| Login form / no `התנתקות` link | Not signed in | Stop: `NOT SIGNED IN — sign in to Maccabi Online in Chrome and re-run.` Never try to log in. |
| No H1 / empty main area | Not hydrated yet | Wait and re-read once or twice. An empty read is not an empty result. |
| A different H1 | UI changed | Stop: `CHANGED: expected H1 '<h1>' on <route id>, got '<actual>'`. |

## 4. Whose record is this?

The account can carry linked family members. The header button
`מציג פרטים של <first name>` and the H1 suffix (` - <first name>`) say whose record
is shown (vaccinations has no suffix; read the switcher instead).

Tell the user whose record you are reading. If they asked about someone else, run
`switch-patient` first. Never assume the account holder.

## 5. Read, report, stop

Report what the user asked for, in their language. Translate Hebrew labels when
reporting in English, but quote the Hebrew alongside for anything they may need to
find on screen.

If an expected element is missing, say `CHANGED: <what> not found on <route id>` and
stop. Never return a partial list as if it were complete.

## Privacy

What you read is the user's medical data. Show it to the user in chat. Never write it
into this plugin's repo, its profile, notes, commit messages or issues: no names, ID
numbers, request ids, doctor names, dates of specific visits or medication names from
a real account.
