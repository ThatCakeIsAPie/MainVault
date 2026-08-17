---
title: Contacts Index
type: contact-index
tags:
  - business/contacts
---

# Contacts Index

A queryable directory of people gathered from business cards, introductions, events, referrals, and active business relationships.

Each company gets one folder under `Companies/`. Its canonical company profile stores organization-wide research once, while each individual inside that folder gets a person-specific contact note for card details, background, relationship context, influence, and follow-up.

## Add a Company and Contact

1. Under `Companies/`, create a folder named for the organization.
2. Copy [[Company Profile Template]] into that folder and rename it `Company Name.md`.
3. Copy [[Contact Template]] into the same folder and rename it `First Last — Company Name.md`.
4. Transcribe the business card under **Business Card Information** exactly as printed.
5. Add the card image or scan to `_Cards/` and embed it in the contact note.
6. Research the company once in its company profile; keep only person-specific background, access, influence, and relationship research in the individual's note.
7. Link every person from the company profile's **People at This Company** section.
8. Complete vendor, customer, and strategic fit in the company profile; assess access and influence in each person's note.
9. Record uncertainties rather than quietly converting guesses into facts—the internet already has enough confidence theater.
10. Add the company to [[Companies Index]] and the person under **Contact Directory** below.

## Contact Directory

- Add contacts here as `[[First Last — Company Name]]`.

## Organization Directory

- [[Companies Index]]

## Query Fields

The YAML properties make contacts filterable by:

- `contact_roles`: vendor, customer, prospect, partner, subcontractor, prime-contractor, referral-source, advisor, or other
- `relationship_status`: unreviewed, researched, warm, active, dormant, or do-not-contact
- `organizations` and `company_profile`: the person's employer and canonical company note
- `job_titles` and `personal_specialties`: person-specific role and expertise
- `contact_geographies`: locations specifically relevant to this person
- `relevance_to`: Faleth Capital, VXE, LibreTech, LTD/Amway, or another operation
- `relationship_value`: none, low, medium, or high
- `influence_level`: unknown, low, medium, or high
- `decision_role`: unknown, influencer, recommender, decision-maker, or owner
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
