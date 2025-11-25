import base64
import json

def generate_html_report(text, components, flows, threat_model, diagram_path="diagram.png", ollama_json=None):
    """
    Generate HTML report including STRIDE, diagram, components, flows, and optional Ollama JSON refinement.
    """
    # Encode PNG for embedding
    with open(diagram_path, "rb") as f:
        encoded_img = base64.b64encode(f.read()).decode("utf-8")

    html = f"""
<html>
<head>
<title>AI Threat Model Report</title>
<style>
body {{
    font-family: Arial, sans-serif;
    padding: 40px;
}}
h1, h2 {{
    color: #333;
}}
pre {{
    background: #f5f5f5;
    padding: 10px;
    border-radius: 5px;
    overflow-x: auto;
}}
table {{
    border-collapse: collapse;
    width: 100%;
    margin-top: 20px;
}}
th, td {{
    padding: 8px;
    border: 1px solid #ccc;
    text-align: left;
}}
</style>
</head>
<body>

<h1>AI Threat Model Report</h1>

<h2>System Description</h2>
<p>{text}</p>

<h2>Components</h2>
<ul>
{"".join(f"<li>{c}</li>" for c in components)}
</ul>

<h2>Data Flows</h2>
<ul>
{"".join(f"<li>{src} → {dst}</li>" for src, dst in flows)}
</ul>

<h2>STRIDE Threat Analysis</h2>
<table>
<tr><th>Component</th><th>STRIDE Categories</th><th>Risk Scores</th></tr>
"""

    for comp, d in threat_model["components"].items():
        stride = ", ".join(d["stride"])
        scores = ", ".join(f"{k}: {v}" for k, v in d["scores"].items())
        html += f"<tr><td>{comp}</td><td>{stride}</td><td>{scores}</td></tr>"

    html += f"""
</table>

<h2>System Diagram</h2>
<img src="data:image/png;base64,{encoded_img}" style="max-width: 100%;">

"""

    if ollama_json:
        # Pretty-print JSON in HTML <pre>
        formatted_json = json.dumps(ollama_json, indent=2)
        html += f"""
<h2>AI-Refined Threat Model (Ollama)</h2>
<pre>{formatted_json}</pre>
"""

    html += """
</body></html>
"""
    return html


def save_html_report(html, path="report.html"):
    with open(path, "w") as f:
        f.write(html)
    return path
