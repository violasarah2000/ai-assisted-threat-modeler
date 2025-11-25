import os
from datetime import datetime

def generate_html_report(text, components, flows, threat_model, diagram_path, ollama_json):
    html = f"""
    <html>
    <head>
        <title>AI Threat Model Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            h1, h2, h3 {{ color: #333; }}
            pre {{ background: #f4f4f4; padding: 10px; border-radius: 6px; }}
            .section {{ margin-bottom: 40px; }}
            img {{ max-width: 800px; border: 1px solid #ccc; }}
        </style>
    </head>
    <body>

        <h1>AI Threat Model Report</h1>

        <div class="section">
            <h2>Original System Description</h2>
            <pre>{text}</pre>
        </div>

        <div class="section">
            <h2>Components</h2>
            <ul>
                {''.join(f'<li>{c}</li>' for c in components)}
            </ul>
        </div>

        <div class="section">
            <h2>Data Flows</h2>
            <ul>
                {''.join(f'<li>{src} → {dst}</li>' for src, dst in flows)}
            </ul>
        </div>

        <div class="section">
            <h2>Threat Model (STRIDE)</h2>
            <pre>{threat_model}</pre>
        </div>

        <div class="section">
            <h2>System Architecture Diagram</h2>
            <img src="{diagram_path}" />
        </div>

        <div class="section">
            <h2>AI-LMM Refinements (Ollama)</h2>
            <pre>{ollama_json}</pre>
        </div>

    </body>
    </html>
    """
    return html


def save_html_report(html, output_dir="artifacts/reports"):
    os.makedirs(output_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"report-{timestamp}.html"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w") as f:
        f.write(html)

    return filepath
