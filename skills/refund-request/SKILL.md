---
name: refund-request
description: Start a refund request (בקשה להחזר כספי) in Maccabi Online — the 11 service categories, the 6,000 ₪ per-invoice cap and the receipt/invoice requirements — and submit after confirmation. Use for 'claim a refund from Maccabi', 'get reimbursed for <service>'.
---

# Refund request

Route: `/sonline/requestsAndApprovals/RefundRequest/TopicSelect/`. H1:
`בקשה להחזר עבור החזרים כספיים`. Prompt: `עבור איזה שירות ברצונך לקבל החזר?`

**Limits and requirements (page text, 2026-10-21):**
- Invoices up to **6,000 ₪** each.
- Attach the original receipt and tax invoice (קבלה וחשבונית מס מקור) plus supporting
  documents as required.
- Eligibility is assessed from what is entered. The page links to eligibility terms
  (`לתנאי הזכאות באתר מכבי`) and to the phone line 3555*.

**Service categories (exact labels):**

| Label | English |
|---|---|
| `רפואת נשים / חבילת הריון ולידה` | Women's health / pregnancy & birth package |
| `ילדים / התפתחות הילד` | Children / child development |
| `התייעצות עם רופא/ה` | Doctor consultation |
| `הסעות ונסיעות` | Transport & travel |
| `פיזיותרפיה נשימתית` | Respiratory physiotherapy |
| `רפואת ספורט` | Sports medicine |
| `שיניים פה ולסת` | Dental, oral & maxillofacial |
| `הבראה / החלמה ושיקום` | Convalescence, recovery & rehab |
| `אביזרים רפואיים` | Medical equipment |
| `אחר` | Other |
| `תרופות` | Medications |

## Steps

Run `${CLAUDE_PLUGIN_ROOT}/reference/preflight.md` first (browser, URL, page check, whose record).

1. Preflight. Confirm the member.
2. Check the invoice is ≤ 6,000 ₪ and that the user has the receipt and tax invoice
   as files. If not, stop and say what is missing.
3. Map the expense onto a category. Ask if ambiguous.
4. Select it, press `המשך`, and fill the following screens with the user.
5. Write gate, then submit.
6. Report the confirmation. Track it in `request-status`.

If the profile's option list no longer matches the page, report
`CHANGED: refund categories differ` and list what the page shows now.

## Write gate

This skill reaches a **write** control. Follow `${CLAUDE_PLUGIN_ROOT}/reference/write-actions.md`: fill, read back, get an explicit yes for this action, submit once.

## Provenance

Observed 2026-10-21 in a signed-in session; route `refund_request` in `profiles/maccabi-online.json` (status there). Handles: URL grammar (rung 1), H1 and visible label text (rung 4/6). Re-verify with `admin-rediscover-portal`.
