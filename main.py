#!/usr/bin/env python3
from modeler.parser import extract_components, extract_data_flows
from modeler.threats import generate_threats
from modeler.graph import build_graph, save_graph_png
from modeler.ai import refine_threats_with_ollama
from modeler.report import generate_html_report, save_html_report
import json
import sys

def main():
    print("AI Threat Modeler v0.3")
    print("-----------------------")

    text = input("Describe your system architecture:\n> ")

    # --- Parse components + flows ---
    components = extract_components(text)
    flows = extract_data_flows(text, components)

    print("\nComponents Found:")
    for c in components:
        print(f" - {c}")

    print("\nData Flows Found:")
    if flows:
        for src, dst in flows:
            print(f" {src} -> {dst}")
    else:
        print(" (none found)")

    # --- Build STRIDE threat model ---
    threat_model = generate_threats(components, flows)

    print("\nGenerated STRIDE (component sample):")
    for comp, data in threat_model["components"].items():
        stride_list = ", ".join(data["stride"])
        score_list = ", ".join(f"{k}: {v}" for k, v in data["scores"].items())
        print(f"\nComponent: {comp}")
        print(f"  STRIDE: {stride_list}")
        print(f"  Scores: {score_list}")

    # --- Build graph diagram ---
    G = build_graph(components, flows)
    png_path = save_graph_png(G, path="artifacts/diagrams/diagram.png")
    print(f"\nDiagram saved to {png_path}")

    # --- Ollama refinement ---
    ollama_json = None
    try:
        print("\nAsking Ollama to refine threats (this may take a while to process)...")
        ollama_json = refine_threats_with_ollama(threat_model)

        print("\nOllama suggestions (JSON):")
        print(json.dumps(ollama_json, indent=2))
    except Exception as e:
        print(f"\nOllama refine step skipped (error): {e}")
        ollama_json = None

    # --- Generate HTML Report ---
    html = generate_html_report(
        text=text,
        components=components,
        flows=flows,
        threat_model=threat_model,
        diagram_path="artifacts/diagrams/diagram.png",
        ollama_json=ollama_json
    )

    report_path = save_html_report(html)
    print(f"\nHTML Report saved to {report_path}")

if __name__ == "__main__":
    main()
