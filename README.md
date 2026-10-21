# Maccabi Online Skills

Unofficial Claude Code skills for **Maccabi Online** (מכבי אונליין,
`online.maccabi4u.co.il`), the member self-service portal of Maccabi Healthcare
Services (מכבי שירותי בריאות), Israel's second-largest health fund (kupat holim).

The skills drive **your own signed-in Chrome** through Claude in Chrome. They read
your medical file and inbox, and can prepare requests that are sent only after you
confirm them.

> **Disclaimer.** This is **not** an official Maccabi product and is not affiliated
> with or endorsed by Maccabi Healthcare Services. The portal is in Hebrew, and its
> UI can change at any time without notice, which may break a skill. Skills are
> written to fail loudly (`CHANGED: …`) rather than return wrong data. Use
> `admin-rediscover-portal` to re-map them. Nothing here is medical advice.

## Requirements

- **An authenticated session.** Sign in to Maccabi Online in Chrome yourself before
  using a skill. The skills do not log in, and never handle passwords or one-time
  codes. (Login support may come later.)
- Claude in Chrome connected to that browser.
- Optional: the `kde-agent-workspace` plugin, to keep browsing on the agent's own
  desktop.

## Install

```
/plugin install maccabi-online-skills --marketplace danielrosehill/Claude-Code-Plugins
```

## Skills

| Skill | What it does | Writes? |
|---|---|---|
| `switch-patient` | Switch the displayed family member (מציג פרטים של) | – |
| `doctor-messages` | Inbox of requests to and messages from doctors | – |
| `new-doctor-request` | Message the doctor or office (prescription, sick note, question, Form 17…), quota-aware | gated |
| `book-appointment` | New appointment, with a clinician you saw recently or via the service search | gated |
| `upcoming-appointments` | Upcoming appointments; cancel through the gate | gated cancel |
| `request-status` | Status of commitments (hitchaivut / Form 17), refunds, pre-approvals | – |
| `new-commitment-request` | New hitchaivut, with the five sub-types explained | gated |
| `refund-request` | Refund claim: 11 categories, 6,000 ₪ per-invoice cap | gated |
| `cardless-visit` | Cardless-visit approval (valid 14 h), also used when a clinician asks for record access | gated |
| `travel-insurance` | Travel-insurance redirect that passes your medical record | gated (shares data) |
| `test-results` | Lab and test results, latest values, PDFs | – |
| `medications` | Current medications, valid or renewable prescriptions, PDF report | – |
| `medication-purchase-history` | When each medicine was dispensed and what you paid | – |
| `visit-summaries` | Clinicians' visit summaries, downloadable | – |
| `my-doctor` | Assigned doctor, clinic hours and contacts; change of doctor through the gate | gated change |
| `vaccinations` | Vaccination record and booklet PDF | – |
| `update-personal-details` | Contact and personal details | gated |
| `public-appeal` | Public enquiries form, no login needed, for following things up | gated |
| `find-branch` | Medical centres by city via the public service guide | – |
| `admin-rediscover-portal` | Maintenance: re-map the live portal and update routes, labels and skills | – |

## How it is built

- `profiles/maccabi-online.json` holds every volatile fact: routes, page titles,
  option labels, verification status and date. Skills describe method; the profile
  holds facts. A UI change is usually a one-file fix.
- `reference/preflight.md`: the checks every skill runs first (URL grammar, login
  wall vs 404 vs not-yet-rendered, whose record is shown).
- `reference/write-actions.md`: the confirmation gate for anything that sends,
  books, submits or shares.
- `scripts/pii_check.py` keeps account data out of the repo. Run it before every commit.

Key facts: every route lives under `/sonline/` (without that prefix the portal shows
a 404 page), and each page's H1 ends in ` - <member's first name>`.

Last verified against the live portal: **2026-10-21**.

## License

MIT
