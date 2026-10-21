# Write actions — the confirmation gate

Most skills here only read. A few reach a control that changes something at Maccabi
or sends data elsewhere. Every one of those goes through this gate.

## What counts as a write

- Sending a message or request to a doctor or the office (quota-limited for doctor messages).
- Booking or cancelling an appointment.
- Requesting a cardless-visit approval (starts a 14-hour validity window that is
  registered with Maccabi).
- Submitting a commitment (התחייבות / Form 17), refund or medicine pre-approval request.
- Changing the assigned family doctor (allowed only periodically).
- Editing personal or contact details.
- Acknowledging a doctor's message (`קראתי את ההודעה`).
- Opening the travel-insurance redirect (passes the medical record to a third party).
- Uploading a document.

Switching the displayed patient and downloading or viewing a PDF are **not** writes.

## The gate

1. Fill the form up to, but not including, the final submit / send / confirm control.
2. Read the page back and present to the user in chat:
   - which member it is for,
   - the category or option chosen (Hebrew and translation),
   - the full text or values entered,
   - any limit or consequence the page states (quota, 14-hour window, 6,000 ₪ cap).
3. Wait for an explicit yes **for this action**. A yes earlier in the session does
   not carry over.
4. Click the submit control once, by reference.
5. Read the confirmation the portal shows and report it. If no confirmation appears,
   say so plainly. Do not resubmit, because a second click can create a duplicate.

## Never

- Enter credentials, one-time codes or payment card details. Stop and ask the user to
  do that step themselves.
- Choose a category on the user's behalf when the choice changes who handles the
  request. Show the options and ask.
