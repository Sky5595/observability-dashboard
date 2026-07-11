import gradio as gr
import random
from datetime import datetime, timedelta

def generate_mock_metrics(hours):
    now = datetime.now()
    logs = []
    for i in range(hours):
        ts = now - timedelta(hours=hours - i)
        latency = round(random.uniform(80, 220), 1)
        error_rate = round(random.uniform(0, 1.5), 2)
        drift_score = round(random.uniform(0, 0.08), 3)
        if random.random() < 0.12:
            latency = round(random.uniform(360, 520), 1)
            error_rate = round(random.uniform(3.5, 7), 2)
            drift_score = round(random.uniform(0.22, 0.42), 3)
        logs.append((ts.strftime("%Y-%m-%d %H:%M"), latency, error_rate, drift_score))
    return logs

def build_dashboard(hours, latency_threshold, error_threshold, drift_threshold):
    logs = generate_mock_metrics(int(hours))
    alerts = [l for l in logs if l[1] > latency_threshold or l[2] > error_threshold or l[3] > drift_threshold]

    table_md = "| Timestamp | Latency (ms) | Error Rate (%) | Drift Score | Status |\n"
    table_md += "|---|---|---|---|---|\n"
    for row in logs:
        flag = "ALERT" if (row[1] > latency_threshold or row[2] > error_threshold or row[3] > drift_threshold) else "OK"
        table_md += f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} | {flag} |\n"

    summary = f"### Summary\n{len(alerts)} of {len(logs)} windows triggered an alert threshold.\n\n"
    if alerts:
        summary += "### Alerts Detail\n"
        for a in alerts:
            summary += f"- {a[0]}: latency={a[1]}ms, error_rate={a[2]}%, drift={a[3]}\n"
    else:
        summary += "No alerts in this window."

    return summary + "\n\n" + table_md

with gr.Blocks(title="Observability Dashboard") as demo:
    gr.Markdown("## AI Observability Dashboard\nPart 4 of the AI Governance series")
    with gr.Row():
        hours = gr.Slider(minimum=6, maximum=48, value=24, step=1, label="Hours of History")
        latency_threshold = gr.Slider(minimum=100, maximum=500, value=300, step=10, label="Latency Alert Threshold (ms)")
    with gr.Row():
        error_threshold = gr.Slider(minimum=0, maximum=10, value=3, step=0.5, label="Error Rate Alert Threshold (%)")
        drift_threshold = gr.Slider(minimum=0, maximum=0.5, value=0.2, step=0.01, label="Drift Score Alert Threshold")
    run_btn = gr.Button("Run Observability Check")
    output = gr.Markdown()
    run_btn.click(fn=build_dashboard, inputs=[hours, latency_threshold, error_threshold, drift_threshold], outputs=output)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
