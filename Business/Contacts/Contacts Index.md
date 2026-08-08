---
title: Contacts Index
type: contact-index
tags:
  - business/contacts
---

# Contacts Index

A queryable directory of people gathered from business cards, introductions, events, referrals, and active business relationships.

Each person gets one canonical note in this folder. The note preserves what the person explicitly provided, separates that from external research, and explains how the relationship may matter to Faleth, VXE, or another business.

## Add a Contact

1. Copy [[Contact Template]].
2. Name the new note `First Last — Company`.
3. Transcribe the business card under **Business Card Information** exactly as printed.
4. Add the card image or scan to `_Cards/` and embed it in the contact note.
5. Research the person and company using attributable public sources.
6. Complete **Relevance Assessment**, including vendor, customer, partner, referral, or other fit.
7. Record uncertainties rather than quietly converting guesses into facts—the internet already has enough confidence theater.
8. Add the new note under **Contact Directory** below.

## Contact Directory

- Add contacts here as `[[First Last — Company]]`.

## Query Fields

The YAML properties make contacts filterable by:

- `contact_roles`: vendor, customer, prospect, partner, subcontractor, prime-contractor, referral-source, advisor, or other
- `relationship_status`: unreviewed, researched, warm, active, dormant, or do-not-contact
- `organizations`: companies or organizations associated with the person
- `industries`: industries served
- `capabilities`: products, services, or specialties
- `geographies`: relevant locations or service areas
- `naics` and `psc`: government-contracting classifications when applicable
- `relevance_to`: Faleth Capital, VXE, LibreTech, LTD/Amway, or another operation
- `vendor_fit`, `customer_fit`, and `strategic_fit`: none, low, medium, or high
- `last_verified`: most recent date the public research was checked
- `next_action_date`: planned follow-up date

## Useful Queries

Ask Delta or GBrain questions such as:

- Which contacts are high-fit vendors for a specific product or capability?
- Who could be a customer for a named offering?
- Which contacts serve a particular industry or geography?
- Which contacts have relevant NAICS or PSC experience?
- Who should we follow up with next?
- Which contact records have stale or unverified research?

## Supporting Files

- [[Contact Template]] — canonical note schema
- [[Business Card Inbox]] — intake instructions and unprocessed-card queue
