---
name: doctor-messages
description: 'Read the Maccabi Online inbox of requests to and messages from doctors and the clinic office (בקשות והודעות מרופאים/ות). Use for ''any messages from the doctor?'', ''did the doctor answer?'', ''check my Maccabi inbox''.'
license: MIT
compatibility: Claude Code with Claude in Chrome and the user's own signed-in Maccabi Online session (online.maccabi4u.co.il). Unofficial; not affiliated with Maccabi. Reads profiles/maccabi-online.json and reference/ from this repository.
---

# Doctor messages (inbox)

Route: `/sonline/communicationWithDoctor/Lobby/`. H1: `בקשות והודעות מרופאים/ות`.

## Steps

Run `${CLAUDE_PLUGIN_ROOT}/reference/preflight.md` first (browser, URL, page check, whose record).

1. Preflight. Name the member whose inbox this is.
2. Use the filters as the user's question needs:
   - `כל הבקשות`: everything
   - `הודעות מהרופא/ה שלך`: messages the doctor sent
   - `שאלות לרופא/ה`: questions the member asked
   - checkbox `הציגו לי רק הודעות שלא קראתי או לא אישרת`: unread or unacknowledged only
3. For each item report date, sender/type, subject, status (answered / awaiting) and
   whether a document is attached. Open an item (chevron) only if the user wants its
   content.
4. Links of the form `?dl=true&req=<id>` open one specific item. Use them if the user
   pastes one. The id belongs to the account, so never store it.

## Do not

Click `קראתי את ההודעה` (acknowledge) unless the user asks. It changes the message
state. To reply or send something new, use `new-doctor-request`.

## Provenance

Observed 2026-10-21 in a signed-in session; route `doctor_messages` in `profiles/maccabi-online.json` (status there). Handles: URL grammar (rung 1), H1 and visible label text (rung 4/6). Re-verify with `admin-rediscover-portal`.
