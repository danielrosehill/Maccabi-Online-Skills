# Maccabi-Online-Skills — notes for agents

Public plugin (`maccabi-online-skills`), listed in the `danielrosehill` marketplace.
It drives the user's signed-in Maccabi Online session through Claude in Chrome.

## Hard rules

1. **No personal data in this repo, ever.** Discovery runs on a real member's
   account. Commit routes, H1 titles, option labels and structure only. Never commit
   names, ID numbers, `relative=`/`sr_id=`/`req=` values, 6+ digit path segments,
   doctor names, visit dates, medication names from the account, or screenshots.
   Run `python3 scripts/pii_check.py` before every commit. Put real names to guard
   against in `local/pii-denylist.txt` (gitignored).
2. **Facts go in `profiles/maccabi-online.json`**, method in `skills/*/SKILL.md`.
   When the UI changes, fix the profile first, then grep the skills for the old label.
3. **Element references only.** Use `find`/`read_page` refs, never pixel coordinates.
   Doctrine: `Claude-Site-Skill-Builder-Plugin/references/durability-doctrine.md`.
4. **Read only while mapping.** Writes go through `reference/write-actions.md`, and
   only on the user's explicit instruction for that specific action. Do not open the
   travel-insurance route during discovery; it shares medical data with a third party.

## Verified facts (2026-10-21)

- Routes are `/sonline/<section>/<page>/`. The side-menu hrefs omit `/sonline` and
  return the portal's 404 page when typed directly; with the prefix, direct
  navigation works.
- It is an SPA: wait 3–5 s after navigating. `StatusRequest/Lobby` is slower.
- The H1 is `<title> - <selected member's first name>`, except Vaccinations (`חיסונים`, no suffix).
- Patient switcher: the header button `מציג פרטים של …` opens a list of linked members.
- `serguide.maccabi4u.co.il` returns a bot-wall page at HTTP 200 to plain fetch; use the browser.
- Not yet opened: the screens after the first choice in the new-request, booking,
  commitment and refund flows, plus travel insurance. Their status is `U` in the profile.

## Skills IL (agentskills.co.il)

All skills except `admin-rediscover-portal` are submitted to Skills IL, the Israeli skills
directory (2026-10-21, category Health Services). Its format applies to every skill here:
frontmatter only `name`, `description` (single-quoted, no `<` `>`, says "Use for/when"),
`license`, `compatibility`; plus `metadata.json` (bilingual name, description, tags;
`supported_agents: ["claude-code"]`, since everything runs through Claude in Chrome) and
`SKILL_HE.md` (Hebrew body, same headings in the same order, code blocks byte-identical).
**A change to a `SKILL.md` body goes into its `SKILL_HE.md` in the same commit**; bump
`version` in its `metadata.json`. Check with `skillsil_check.py` and record submissions in
`references/skillsil-submissions.json`, both in the software-publisher plugin
(`skillsil-submit` skill). A `v*` tag makes a signed release (`.github/workflows/release.yml`).

## Shipping

Bump `.claude-plugin/plugin.json` `version`, push, then update the entry in
`ai-claude-marketplaces/Claude-Code-Plugins/.claude-plugin/marketplace.json` if the
description or version changed, and run `catalogue__sync plugin=maccabi-online-skills`.
