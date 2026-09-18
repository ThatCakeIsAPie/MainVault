---
type: principle
title: 'X For You ranks predicted actions, not post quality'
status: active
related:
  - research/raw/transcripts/lyle-x-share-2087969186219778252
  - research/faleth/content/x-creator-payout-impressions-signal-2026
  - research/faleth/content/reply-led-audience-discovery-2026
  - research/faleth/content/systematic-x-voice-layer-printer-2026
  - raw/x-bookmarks/26-08-13/2087969186219778252.md
sources:
  - 'https://x.com/doganuraldesign/status/2087969186219778252'
  - raw/x-bookmarks/26-08-13/2087969186219778252.md
effective_date: '2026-08-13'
updated: 2026-08-14
tags:
  - content
  - faleth
  - twitter
  - x-ingest
  - x-algorithm
---

# X For You ranks predicted actions, not post quality

Living principle from @doganuraldesign's 2026-08-13 Grok Bot read of the re-open-sourced For You code (claimed 370,523 lines; production weights last synced 12 Aug 2026).

## Core mechanic

The ranker does **not** assign a global quality score. For each reader it predicts what that person will do to the post, multiplies each probability by a fixed weight, and sums. Highest total wins the slot.

Those weights sit **on top of** an unpublished 2560-dim, 8-layer transformer over ~1,022 items of reader history. Public code is the linear formula, not the deep model.

## What the formula pays for

High-intent export and conversation beat decoration:

- Copy-link / share externally: **+20** (~40 likes)
- Mutual reply on an **original**: **+20** (5 + 15)
- Quote / any reply / DM share: **+5**
- Follow from the post: **+4**
- Share button: **+2**
- Repost: **+1**
- Like: **+0.5**
- Click post: **+0.4**; open a link: **+0.2**
- Photo expand / video open / ≥10s quality view: **+0.05**
- Dwell time: **+0.004**; yes/no dwell: **0**
- Profile click: **0**

## What kills a post

- Report **−234** (~468 likes the other way)
- Mute **−58.8** (worse than block)
- Not interested **−43.2**
- Block **−31.2**
- Not-dwell **−0.02**

Mute/block weights hit the **target**, not the person doing the muting (same-author follow-up). Easy to game if abused; still lethal if people mute *you*.

## Haircuts after the score

1. **Same-author:** 2nd post ×0.625, 3rd ~×0.44, floor 0.25.
2. **25% tax:** non-followers ×0.75. Replies and reposts get the tax even from followers. Originals from followed accounts keep full weight.
3. **Similar-post reranker** (θ = 0.65) spreads lookalikes.

## How a post even enters

Rebuilt on every open. ~35 organic slots.

- In-network: Thunder, up to ~1,200 recent posts from follows.
- Out-of-network: Phoenix (semantic nearby) + 2020 SimClusters, ~1,000 + 800.
- Max age **48 hours**. No weekly resurrection.
- Own posts never appear in own For You.
- Stranger replies/reposts dropped **before** scoring.
- Small-account bump (<1k followers, <1k impressions, <24h): one original can land around **slot 15–16**, not #1, and only if already in the top ~85%.
- Visibility filters are a second machine. High score can still die to spam / DNA / NSFW / impersonation, harsher out-of-network.

## Faleth / Lyle application

This is **process knowledge for the public-learning flywheel**, not a new identity or a runway plan.

1. **Write originals people export.** Copy-link, quote, DM, and mutual reply are the real currency. Like-farming is almost decorative. That already matches Lyle's "usefulness over engagement bait."
2. **Conversation with mutuals is coded as quality.** Reply-led discovery still matters for *finding* people; For You will not let reply-guy tactics into a stranger's feed. Build the room, then post into it.
3. **Space the posts.** Dumping a burst taxes the second and third items in the same reader's feed.
4. **Stay inside 48 hours.** Recycle by writing the next true thing, not by waiting for last week's post to revive.
5. **Do not fuse identity to slot number.** Small-account gift is mid-feed, not the throne. Scoreboard idolatry is still the trap. Work the system; do not become it.
6. **VXE cash timing stays primary.** This note equips later outbound drafts. It does not promote X-growth into this season's KPI.

## Evidence class

Second-hand Grok Bot read of public `x-algorithm` as relayed by the post. Weights are claimed production values as of 12 Aug 2026. Transformer weights were not shipped. Do not treat a single viral summary as a forever spec.

## Related

- [[research/raw/transcripts/lyle-x-share-2087969186219778252]]
- [[raw/x-bookmarks/26-08-13/2087969186219778252]]
- [[research/faleth/content/x-creator-payout-impressions-signal-2026]]
- [[research/faleth/content/reply-led-audience-discovery-2026]]
- [[research/faleth/content/systematic-x-voice-layer-printer-2026]]
- [[research/faleth/content/hermes-grok-x-content-machine-2026]]
- [[research/faleth/content/x-ocr-to-supergrok-prosumer-2026]]
