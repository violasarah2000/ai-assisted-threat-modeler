# AI-Assisted Threat Modeler

**A local-first, privacy-focused threat modeling program combining rule-based STRIDE analysis with LLM refinement—designed for security teams that won't compromise on data privacy. Contact SperksWerks.ai to learn more!**

I built this Python-based security analysis tool to demonstrate how to integrate AI into real security workflows **without sending architecture data to third-party APIs**. It transforms natural language architecture descriptions into structured STRIDE threat models with visual attack graphs, automated analysis, and comprehensive HTML reports—all running locally. This project demonstrates my expertise in **AI-assisted security engineering**, **secure architecture analysis**, **production-grade Python automation**, and understanding how to apply AI responsibly in enterprise security.

### Why This Matters
Organizations face a security paradox: cloud-based threat modeling tools accelerate analysis, but risk exposing sensitive architecture data to external APIs. This tool solves that problem. By combining deterministic rule-based threat detection with local LLM refinement (via Ollama), it delivers AI-assisted insights while maintaining full data sovereignty—appealing to security-conscious enterprises and companies building AI security infrastructure that demands accountability and explainability.

---

## Purpose

- **Demonstrate AI-assisted security engineering** at scale—combining local LLM integration with established threat modeling frameworks while maintaining data privacy.
- **Showcase production-grade Python development** with modular architecture designed for extensibility (MITRE ATT&CK, CVSS scoring, threat simulation).
- **Highlight secure design thinking** through hybrid rule-based + AI analysis with full explainability and auditability.
- **Illustrate practical AI/LLM application** beyond chatbots—showing how to integrate local models into security workflows without compromising data sovereignty.

---

## Key Differentiators

### 🔒 Local-First, Privacy-Focused
- **Zero cloud API calls:** Self-hosted LLM via Ollama means your architecture never leaves your infrastructure.
- **No data leakage:** Unlike cloud-based threat modelers (e.g., STRIDE-GPT), architecture designs and threat models stay internal.
- **Ideal for:** Organizations with strict data sovereignty requirements, enterprises modeling sensitive systems, and security-first companies.

### 🔍 Full-Stack Visibility + Automation
- **Text Parsing:** Extract system components and data flows from natural language descriptions.
- **STRIDE Threat Modeling:** Deterministic rule-based analysis ensures consistent, auditable threat detection.
- **Visualization:** Directed graph diagram (PNG) showing component interactions and potential attack paths.
- **HTML Report:** Actionable security artifact for design reviews, documentation, and compliance.
- **AI Refinement:** Local LLM refines and prioritizes threats—augmenting, not replacing, deterministic analysis.

### 🎯 Explainability + Transparency
- **Hybrid approach:** Threats generated via deterministic STRIDE rules first, then refined by AI.
- **Auditable:** Security teams can review both rule logic and AI reasoning—appealing to organizations skeptical of "just GPT" solutions.
- **Trustworthy AI:** Clear separation between algorithmic and AI-driven insights.

### 📦 Modular Architecture
- **Extensible framework:** Designed to integrate MITRE ATT&CK mapping, CVSS scoring, threat simulation, and additional analysis modules.
- **Production-ready:** Not a toy or academic experiment—a real proof-of-concept for AI-enhanced security workflows.
- **Scalable:** Ready for integration into dev, architecture review, and compliance workflows.

---

## Technical Highlights

- **Language & Environment:** Python 3.11+, Conda for reproducibility
- **NLP & Analysis:** SpaCy for component extraction, NetworkX for threat graph analysis
- **Visualization:** Matplotlib for directed attack graphs
- **AI:** Local LLM via Ollama (Gemma2) for threat refinement—no cloud dependencies
- **Performance:** Runs on commodity hardware with low latency, suitable for iterative threat modeling
- **Data Privacy:** 100% local execution; no external API calls or data transmission
- **Extensible Design:** Modular codebase supports future integrations (MITRE ATT&CK, CVSS, threat simulation)

---

## Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/ai-threat-modeler.git
cd ai-threat-modeler

# Conda environment (recommended)
conda env create -f environment.yml
conda activate ai-threat-modeler

# Or pip/venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Download SpaCy English model
python -m spacy download en_core_web_sm
```

## Quick Start

```bash
python main.py
```

**Example Input:**
```
"The web-app connects to the database. The API gateway uses the web-app. The admin-portal connects to the database."
```

**Output:** Threat model, visual graph, and comprehensive HTML report with AI-refined recommendations.

- Terminal summary of components and data flows
- STRIDE threat model
- Graph diagram (PNG) showing arrows for data flow
- Full HTML report including AI-refined threats

---

## What This Demonstrates

This project showcases my core AI Security Engineer competencies:

- **Responsible AI Integration:** Practical integration of local LLMs into security workflows with data privacy as a first-class concern—not just prompt engineering.
- **Threat Modeling Mastery:** Deep understanding of STRIDE, attack vectors, risk scoring, and how to automate deterministic analysis.
- **Explainable AI:** Hybrid rule-based + AI approach that maintains auditability and transparency—critical for enterprise security tools.
- **Software Architecture:** Modular, extensible Python design with clear separation of concerns, ready for production deployment and future enhancements.
- **Full-Stack Security Engineering:** From NLP parsing to graph analysis to visualization to report generation—end-to-end security tool development.
- **Enterprise Security Mindset:** Understanding real organizational constraints (data sovereignty, compliance, auditability) and designing solutions that respect them.
- **DevOps Rigor:** Reproducible environments, clear documentation, automated workflows, and local-first design for scalable deployment.

---

## Roadmap: Extensibility by Design

The modular architecture anticipates future enhancements:

- **Visual Diagram Parsing:** Integration with Visio/Lucidchart/draw.io for automated architecture import—no manual re-entry.
- **Risk Quantification:** CVSS scoring integration for severity prioritization and real threat intelligence feeds.
- **MITRE ATT&CK Mapping:** Automated mapping of detected threats to MITRE ATT&CK tactics and techniques for framework-aligned analysis.
- **Threat Simulation:** Local threat scenario modeling and attack path analysis.
- **CI/CD Integration:** Automated threat modeling as part of secure SDLC pipelines—shift left security to architecture phase.
- **Enterprise Compliance:** Audit logging, compliance reporting, and multi-team workflows for scaled security reviews.
- **Performance Optimization:** Batch processing and caching for large architecture portfolios.

These enhancements demonstrate forward-thinking architecture suitable for teams building security tools at scale.

---

## Why This Matters to Security Leaders

1. **AI + Privacy:** Demonstrates how to leverage AI for security automation while respecting data sovereignty—solving the enterprise dilemma of "cloud AI vs. internal secrets."
2. **Auditable AI:** Shows understanding that security teams need transparency: deterministic rules + AI insights, not "black box" model output.
3. **Defense at Scale:** Automating threat modeling enables security reviews for every deployment, not just critical systems—with tools security teams can actually use and trust.
4. **Secure-by-Design Culture:** Tools that embed security thinking early in the architecture phase, with extensible frameworks for future AI security innovations.
5. **Production Mindset:** Not academic—this is a real tool for real workflows, designed with enterprise constraints in mind.

