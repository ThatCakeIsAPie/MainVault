---
title: Spring-Damper Undulation for Procedural Secondary Motion (2026)
created: 2026-08-12
updated: 2026-08-12
type: concept
tags: [software, systems, architecture, skills]
sources:
  - raw/x-bookmarks/2026-08-11/2086988399085584510.md
confidence: medium
---

# Spring-Damper Undulation for Procedural Secondary Motion (2026)

## Concept

Natural-looking tails, ropes, antennae, tentacles, and bone chains do not inherently require generative animation. A compact physical system can create reusable wave-like follow-through:

1. Pull each bone endpoint toward its parent's target position with a spring.
2. Apply damping so retained velocity settles instead of oscillating forever.
3. Enforce segment-length constraints.
4. Derive procedural bone rotation from the constrained positions.
5. Propagate the delayed response down the hierarchy.

Inertia, lag, and overshoot then emerge from continuous integration rather than being authored frame by frame. The method can run in real time or offline and is inspectable: stiffness and damping are explicit controls, not latent behavior hidden inside generated motion.

## Why it matters

This is a clean example of choosing the **smallest causal model** that solves the problem. Generative AI is useful when the motion prior is complex or underspecified; simple secondary motion is often better served by deterministic physics that is cheap, editable, repeatable, and renderer-independent. That makes it compatible with [[faleth/process/image-to-3d-asset-compilation-agent-loops-2026]]: an agent can generate and tune procedural rigs while objective constraints remain available for verification.

It also illustrates [[faleth/process/demonstration-to-skill-capture-2026]] from the opposite direction. Instead of learning an opaque behavior from examples, encode the few dynamics that produce the behavior, then expose those parameters as a reusable skill.

## Implementation cautions

- Stability depends on time step, stiffness, damping, integration method, and constraint iterations.
- Real-time use should test behavior across frame rates or use a fixed simulation step.
- Collision, self-intersection, joint limits, and extreme acceleration are outside the simple demonstration.
- The bookmarked post and linked tutorial establish a practical MaxScript example, not a controlled comparison against keyframing, cloth/rope solvers, or learned animation.

## Provenance

- [[raw/x-bookmarks/2026-08-11/2086988399085584510]] — Japanese demonstration post, video, and link to the MaxScript tutorial
- [Physics-Based Animation: Undulation](https://shirzadbahrami.com/physics-based-animation-undulation/)
