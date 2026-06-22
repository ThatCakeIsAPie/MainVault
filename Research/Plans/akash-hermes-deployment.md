---
title: Deploy Hermes Agent to Akash Network
created: 2026-05-16
updated: 2026-06-22
type: plan
tags: [hermes-agent, akash, deployment, infrastructure]
sources:
  - "[[SOURCE-MANIFEST]]"
  - "[[OKF-COMPATIBILITY]]"
---

# Deploy Hermes Agent to Akash Network

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Run Hermes Agent (Telegram gateway) on Akash Network so Lyle's bot stays online 24/7, independent of his laptop. Vault memory stack context: see [[SOURCE-MANIFEST]] and [[OKF-COMPATIBILITY]].

**Architecture:** Official Hermes Docker image (`nousresearch/hermes-agent:latest`) deployed via Akash Console. Persistent 50GB volume at `/opt/data` for all user data (config, sessions, skills, memory). No custom Dockerfile, no Docker installation needed on Lyle's machine.

**Tech Stack:** Akash Console, official Hermes Docker image, Akash persistent storage

---

## What Changed From Original Plan

The original plan assumed we needed to build a custom Docker image. Nous Research maintains an official `nousresearch/hermes-agent:latest` image on Docker Hub (1.2M+ pulls). This eliminates:
- ❌ Docker installation on Lyle's laptop
- ❌ Custom Dockerfile
- ❌ Building and pushing an image
- ❌ SSH server setup
- ❌ Custom entrypoint script

All we need is the Akash SDL and Lyle's API keys.

---

## What Lyle Needs to Do

**Total time: ~15 minutes**

### Step 1: Log into Akash Console
Go to console.akash.network and log in (Lyle already has an account).

### Step 2: Click "Deploy" → "Custom" (or "SDL Builder")
Paste this SDL into the editor:

```yaml
---
version: "2.0"

services:
  hermes:
    image: nousresearch/hermes-agent:latest
    env:
      - OPENROUTER_API_KEY=PASTE-YOUR-KEY-HERE
      - TELEGRAM_BOT_TOKEN=PASTE-YOUR-TOKEN-HERE
    command: ["sh", "-c", "mkdir -p /opt/data && echo \"OPENROUTER_API_KEY=$OPENROUTER_API_KEY\" > /opt/data/.env && echo \"TELEGRAM_BOT_TOKEN=$TELEGRAM_BOT_TOKEN\" >> /opt/data/.env && hermes gateway run"]
    params:
      storage:
        data:
          mount: /opt/data
    expose:
      - port: 8642
        as: 80
        to:
          - global: true

profiles:
  compute:
    hermes:
      resources:
        cpu:
          units: 2
        memory:
          size: 2Gi
        storage:
          - size: 50Gi
            attributes:
              persistent: true
              class: beta3
  placement:
    akash:
      attributes:
        host: akash
      signedBy:
        anyOf:
          - akash1365yvmc4s7awdyw3n8z5zluhtp0l6j8t0dk97y
      pricing:
        hermes:
          denom: uakt
          amount: 100000

deployment:
  hermes:
    akash:
      profile: hermes
      count: 1
```

**⚠️ Replace** `PASTE-YOUR-KEY-HERE` and `PASTE-YOUR-TOKEN-HERE` with your actual values before submitting.

### Step 3: Submit and Accept a Bid
- Click "Create Deployment"
- Akash will show provider bids (typically $5-15/month for these resources)
- Accept the lowest bid
- Wait 1-3 minutes for the container to start

### Step 4: Verify
- The deployment status should show "active"
- Your Telegram bot should respond to messages within 2-3 minutes (first boot takes longer as the image initializes)
- Check the deployment logs in Akash Console to confirm the gateway started

### Step 5 (Optional): Test the API Server
After deployment, you'll get a public URL like `http://<akash-ip>:<mapped-port>`. This exposes the Hermes API server (OpenAI-compatible). You can test it with:
```
curl http://<akash-ip>:<mapped-port>/health
```

---

## How CLI Access Works (No SSH Needed)

Since the Telegram bot IS your primary interface, you don't need SSH for daily use. Here's how to handle different scenarios:

### Daily Use → Telegram
Just talk to the bot. Everything works the same as when it was on your laptop.

### Configuration Changes → Telegram Slash Commands
- `/model` — change the AI model
- `/config` — view config
- `/status` — check session info
- `/tools` — manage tools
- `/skills` — manage skills

### Advanced CLI Access → Akash Console Shell
Akash Console provides a **web terminal** for running deployments. In your deployment dashboard:
1. Click on the running deployment
2. Look for "Shell" or "Exec" tab
3. This gives you a terminal inside the container
4. Run `hermes` for interactive CLI, `hermes config edit`, etc.

### If You Need Full SSH Later
We can add an SSH server to a custom image in a follow-up deployment. But for now, the Telegram interface + Akash Console shell covers 99% of use cases.

---

## What's Running

| Component | Details |
|-----------|---------|
| Image | `nousresearch/hermes-agent:latest` (official, auto-updated) |
| CPU | 2 vCPUs |
| Memory | 2 GB RAM |
| Storage | 50 GB persistent (survives restarts) |
| Port 8642 | Hermes API server (OpenAI-compatible) |
| Model | xiaomi/mimo-v2.5-pro via OpenRouter |
| Gateway | Telegram bot (24/7) |

## Cost Estimate

~$5-15/month depending on provider bids. The $100 free trial credits should last 2+ months.

## Post-Deployment

### Updating Hermes
When a new version is released:
1. Go to Akash Console → your deployment
2. Close the current deployment
3. Redeploy with the same SDL (pulls the latest `:latest` tag)
4. Your persistent volume data is preserved

### Adding More API Keys Later
1. Akash Console → your deployment → Shell
2. Edit `/opt/data/.env` to add new keys
3. Restart the gateway: `hermes gateway restart`

### Monitoring
- Check deployment logs in Akash Console
- Telegram: `/status` for session info
- Telegram: `/usage` for token usage

---

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Akash provider goes offline | Bot down temporarily | Redeploy; accept new bid |
| Lease expires | Deployment stops | Set calendar reminder to renew |
| First boot slow | 2-3 min wait | Normal; only happens once |
| No SSH access | Can't debug remotely | Akash Console shell + Telegram commands cover most cases |
