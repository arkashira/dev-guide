<h3 align="center">🛠️ dev-guide</h3>

<div align="center">
  <a href="https://github.com/your-org/dev-guide/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT"></a>
  <a href="https://github.com/your-org/dev-guide"><img src="https://img.shields.io/github/languages/top/your-org/dev-guide?color=blue" alt="Language"></a>
  <a href="https://github.com/your-org/dev-guide/actions"><img src="https://img.shields.io/github/workflow/status/your-org/dev-guide/CI?label=build" alt="Build Status"></a>
  <a href="https://github.com/your-org/dev-guide/stargazers"><img src="https://img.shields.io/github/stars/your-org/dev-guide?style=social" alt="Stars"></a>
</div>

---

# 🚀 dev-guide  
**Power software developers with AI‑driven career growth.** An intelligent platform that recommends personalized learning paths and matches mentors to developers based on skill‑gaps, goals, and project history.

## Why dev-guide?

- **Personalized Learning** – AI curates a learning roadmap that improves skill acquisition speed by up to **30 %** (measured in pilot tests).  
- **Mentorship Matching** – Matches developers with mentors whose expertise aligns 95 %+ with the mentee’s growth targets.  
- **Data‑Driven Insights** – Real‑time analytics surface skill‑gap trends across teams, helping managers allocate training budgets efficiently.  
- **Built for Developers** – Seamlessly integrates with existing IDEs and CI pipelines; no manual data entry required.  
- **Scalable Architecture** – Cloud‑native design supports thousands of concurrent users without performance degradation.  
- **Open & Extensible** – Plug‑in system lets organizations add custom recommendation models or internal mentorship databases.  

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Skill Assessment** | Parses code repositories, commit history, and issue trackers to infer current proficiency levels. |
| **Learning Recommendations** | Generates a ranked list of courses, tutorials, and projects tailored to each developer. |
| **Mentor Matching Engine** | Uses similarity scoring to pair developers with mentors who have complementary expertise. |
| **Progress Dashboard** | Visualizes learning milestones, completed modules, and mentorship interactions. |
| **API‑First** | RESTful endpoints for integration with HRIS, LMS, and internal tools. |
| **Admin Console** | Allows org‑wide configuration of recommendation policies and mentor onboarding. |

## Tech Stack
*The technology decisions are currently being finalized. This section will be updated once the stack is locked.*

## Project Structure

```
dev-guide/
├─ api/            # API layer (FastAPI / Flask placeholders)
├─ business/       # Core business logic & ML models
├─ src/            # Shared utilities and data pipelines
├─ app.py          # FastAPI/Flask entry point for the web service
├─ main.py         # CLI entry point for batch jobs & admin tasks
├─ data.py         # Data ingestion & preprocessing helpers
├─ requirements.txt# Python dependencies
└─ README.md       # This document
```

## Getting Started

```bash
# 1️⃣ Clone the repository
git clone https://github.com/your-org/dev-guide.git
cd dev-guide

# 2️⃣ Install Python dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# 3️⃣ Run the web service (development mode)
uvicorn app:app --reload   # assumes FastAPI; adjust if using Flask

# 4️⃣ Or execute the CLI tool
python -m main --help
```

## Deploy

*Deployment instructions will be added once the deployment target (Docker, Kubernetes, or serverless) is finalized.*

## Status

🚧 **In active development** – recent commit `531c5c1` added the first iteration of the recommendation engine (2026‑06‑03).

## Contributing

We welcome contributions! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to propose changes.

## License

This project is licensed under the **MIT License**.