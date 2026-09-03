---
title: PIEE solicitation email notifications — next steps after Proposal Manager activation
created: 2026-08-26
updated: 2026-08-26
type: summary
tags: [business, operations, systems]
sources: []
confidence: medium
---

# PIEE solicitation email notifications — next steps after Proposal Manager activation

**Purpose:** Indexable checklist for VXE so NECO-style **inbound solicitation emails** work in PIEE after an admin activates Lyle’s **Proposal Manager** role. Do this **after** activation — not before.

**Not this page:** BOT/RPA scraping of PIEE. Native PIEE email + SAM alignment only. Hermes driving PIEE under Lyle’s login is a separate compliance decision (`BOT/RPA` on My Account).

---

## Already true (do not redo as “setup”)

| Fact | Detail |
|------|--------|
| CAGE / location | **13KH1** (PIEE group/location on registration mail) |
| User ID | **LyleCole** |
| Email on PIEE registration | **Lyle@vxecorp.com** (same as SAM.gov — Albert’s “align emails” bar is met for this identity) |
| Roles requested (2026-08-25 mail) | **Proposal Manager** (app **SOL**), **Vendor** (WAWF), **AMT Viewer** (AMT) — all were **Activation Required** |
| Admin path | System mail **To:** VXE + **Bryan Newkirk**; Lyle Cc’d as informational |
| Outlook landing | `bids@vxecorp.com` Inbox; folder **Inbound Solicitations** already exists for routing |

**Gate:** Until admin activates **Proposal Manager / SOL**, treat solicitation email alerts as **not live**.

---

## Gate: confirm activation

1. Lyle logs into [PIEE](https://piee.eb.mil/) as **LyleCole**.
2. **My Account** / role list: **Proposal Manager** (SOL) shows **Active** (not Activation Required / pending).
3. Ideally same day: **Vendor (WAWF)** active if WAWF work is needed; AMT Viewer only if AMT is used.
4. If still pending: nudge **Bryan Newkirk** (or current CAM/admin) — he was on the activation mail. No second self-registration loop.

**Optional proof:** one successful SOL module open without “role not activated” errors.

---

## After Proposal Manager is Active — complete notification path

Order is intentional. Stop when a step fails; fix that step before inventing automation.

### 1. Identity sanity (5 minutes)

- [ ] PIEE **My Account** email still **Lyle@vxecorp.com** (or intentional shared bids mailbox if VXE standardizes on that — document which address is canonical for alerts).
- [ ] SAM.gov entity/contact for VXE still uses the **same** address you expect for opportunity mail.
- [ ] PIEE My Account **BOT/RPA** remains **N** unless you truly intend automated software on this account.

### 2. Solicitation Module — POC / Proposal Manager recipients

Albert (PIEE help, 2026-08-26): native path replaces NECO inbound email via **contractor POC + Proposal Manager recipients** in the **Solicitation Module**, not a Hermes scrape.

- [ ] Open **Solicitation (SOL)** module with activated Proposal Manager role.
- [ ] Find contractor **POC / directory / notification recipients** (labels vary by PIEE build).
- [ ] Ensure **Proposal Manager** (and any required secondary) is listed with a **live** email:
  - Prefer the address that is monitored daily (**Lyle@vxecorp.com** and/or **bids@vxecorp.com** — pick one primary, add the other only if PIEE allows multiple).
- [ ] If UI requires role + email: role Active **and** email present (Albert: if POC lacks active Proposal Manager, email can still be entered manually in some builds — verify on screen).
- [ ] Save; screenshot or note the exact screen path for Leonard/Bryan.

### 3. Mail plumbing (Outlook / Graph)

- [ ] Confirm PIEE system mail is not junked (`disa.ogden.eis.mbx.*`, WAWF/PIEE noreply domains).
- [ ] Keep **Inbound Solicitations** folder + rules: PIEE/SAM opportunity mail → that folder (and optional Teams/Telegram ping later).
- [ ] Send a **test** if PIEE offers notification test; else watch for the next real SOL notice after activation.

### 4. Operational acceptance test

Pass criteria (any one is weak; prefer two):

- [ ] At least one **PIEE-originated** solicitation-related email lands on the monitored address after activation + POC save.
- [ ] Lyle can open the linked solicitation in SOL without role errors.
- [ ] Leonard knows which inbox is authoritative for “new PIEE opportunity.”

Fail → PIEE support (do not jump to BOT/RPA):

- Email: `disa.global.servicedesk.mbx.eb-ticket-requests@mail.mil`
- Phone: **866-618-5988**
- Ticket ask: *Vendor CAGE 13KH1; Proposal Manager active; how do we receive inbound solicitation emails equivalent to retired NECO notifications? POC screens already updated.*

### 5. Explicitly out of scope until native path fails

- Hermes / RPA login to PIEE to scrape opportunities.
- Marking **BOT/RPA = Y** without a written reason and admin awareness.
- Assuming SAM.gov “Contracting Officer” language from Albert applies to vendor accounts (likely gov-side FAQ bleed).

---

## People

| Who | Role on this thread |
|-----|---------------------|
| **Bryan Newkirk** | On activation mail (To) — primary admin activate ask |
| **Lyle Cole** | User `LyleCole`; Proposal Manager consumer; monitored email |
| **Leonard / VXE** | Operator; must know inbox + that NECO ≠ auto-on in PIEE |
| **Gov Sales Desk** | Cc on system mail; shared visibility |

---

## Sources (session 2026-08-26)

- PIEE My Account (Brave): BOT/RPA field; profile email Lyle@vxecorp.com; CAGE 13KH1.
- Albert chat (`albert-piee.eb.mil`): NECO replacement via Solicitation Module POC / Proposal Manager emails + SAM email alignment; support contacts above.
- Outlook `bids@vxecorp.com`: *ACTION NEEDED - PIEE - User Self Registered* (2026-08-25) — roles Activation Required; admin must activate.

Albert disclaimer: assistant answers can be wrong; UI labels win over this checklist.

---

## Related

- [[business/vxe/full-time-transition-research-2026]] — VXE runway / facility research context
- [[Business/Faleth Capital/VXE (partner)/AI Context/VXE — AI Reference]] — partner operating reference
- [[faleth/bridge-strategy/automation-services-2026]] — automation bridge is **not** the PIEE notification path
