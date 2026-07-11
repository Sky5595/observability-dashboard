---
title: Observability Dashboard
emoji: 📊
colorFrom: purple
colorTo: yellow
sdk: gradio
sdk_version: "5.4.0"
python_version: "3.10"
app_file: app.py
pinned: false
---

# AI Observability Dashboard

Part 4 of the AI Governance series. A Gradio dashboard that simulates production monitoring for an AI system, flagging latency spikes, error rate increases, and model drift against configurable thresholds.

## Live Demo
https://huggingface.co/spaces/crimemastergogo22/observability-dashboard

## What it does
Set thresholds for latency, error rate, and drift score, choose a lookback window, and the dashboard generates a monitoring report flagging any window that breaches a threshold.

## Example Usage

**Input:**

- Hours of History: 24
- Latency Alert Threshold: 300ms
- Error Rate Alert Threshold: 3%
- Drift Score Alert Threshold: 0.2

**Output:**

    ### Summary
    2 of 24 windows triggered an alert threshold.

    ### Alerts Detail
    - 2026-07-11 13:43: latency=370.5ms, error_rate=6.35%, drift=0.375
    - 2026-07-11 17:43: latency=488.8ms, error_rate=6.21%, drift=0.317

    | Timestamp        | Latency (ms) | Error Rate (%) | Drift Score | Status |
    |-------------------|--------------|-----------------|-------------|--------|
    | 2026-07-11 12:43  | 105.3        | 0.26            | 0.028       | OK     |
    | 2026-07-11 13:43  | 370.5        | 6.35            | 0.375       | ALERT  |
    | 2026-07-11 14:43  | 132.5        | 1.03            | 0.054       | OK     |
    | 2026-07-11 17:43  | 488.8        | 6.21            | 0.317       | ALERT  |

## Run Locally

```bash
git clone https://github.com/Sky5595/observability-dashboard.git
cd observability-dashboard
pip install -r requirements.txt
python app.py
```

## Tech Stack
- Python 3.10
- Gradio 5.4.0
- Hugging Face Spaces (ZeroGPU-compatible via @spaces.GPU decorator)

## Part of the AI Governance Series
1. LLM Use-Case Risk Radar
2. Prompt Red-Team Harness
3. Model Card Generator
4. Observability Dashboard (this project)
5. Explainable Credit RAG

---
Built as part of a hands-on AI governance portfolio. Feedback and forks welcome.
