# QualityForge AI

**AI-Powered Software Quality & Test Automation Platform**

QualityForge AI is a Python-based software quality and test automation project designed to validate APIs, automate browser workflows, execute tests in CI/CD pipelines, and generate structured test reports.

## 1. Project Overview

Software teams need reliable ways to verify application quality before releasing software. QualityForge AI combines automated API testing, browser automation, containerized execution, and continuous integration to support reliable software delivery.

## 2. Project Goals

- Automate API testing using Python, Requests, and pytest.
- Automate user journeys using Playwright.
- Validate application behavior across browsers.
- Execute automated tests through GitHub Actions.
- Run tests consistently inside Docker containers.
- Generate JUnit XML test reports.
- Explore flaky test detection and AI-assisted testing.

## 3. Technology Stack

| Category | Technology |
|---|---|
| Programming language | Python 3.12 |
| API testing | Requests, pytest |
| UI automation | Playwright |
| JSON validation | jsonschema |
| Configuration | python-dotenv |
| Version control | Git, GitHub |
| CI/CD | GitHub Actions |
| Containerization | Docker |
| Test reporting | JUnit XML |

## 4. Project Structure

```text
QualityForge-AI/
├── .github/
│   └── workflows/
│       └── tests.yaml
├── docs/
├── pages/
├── reports/
├── src/
├── tests/
│   ├── api/
│   └── ui/
├── test_data/
├── .dockerignore
├── .gitignore
├── Dockerfile
├── pytest.ini
├── requirements.txt
└── README.md
```

## 5. Prerequisites

- Python 3.12
- Git
- Docker Desktop (for containerized execution)
- Windows, Linux, or macOS

## 6. Local Setup

Clone the repository:

```bash
git clone https://github.com/Rahul183269/QualityForge-AI.git
cd QualityForge-AI
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
python -m playwright install chromium firefox
```

## 7. Running Tests Locally

Run the complete test suite:

```bash
python -m pytest -v
```

Generate a JUnit XML report:

```bash
python -m pytest -v --junitxml=reports/junit.xml
```

The generated report is saved at `reports/junit.xml`.

## 8. Docker Execution

Build the Docker image:

```powershell
docker build -t qualityforge-ai:latest .
```

Run the automated test suite:

```powershell
docker run --rm qualityforge-ai:latest
```

Run tests and persist the JUnit report on the Windows host:

```powershell
docker run --rm -v "${PWD}/reports:/app/reports" qualityforge-ai:latest
```

The report will be available locally at `reports/junit.xml`.

## 9. CI/CD Pipeline

QualityForge AI uses GitHub Actions to automate test execution.

The workflow runs when:

- Code is pushed to the `main` branch.
- A pull request targets the `main` branch.

Pipeline stages:

1. Check out the repository.
2. Configure Python 3.12.
3. Install project dependencies.
4. Install Playwright Chromium and Firefox.
5. Execute pytest.
6. Generate a JUnit XML report.
7. Upload the report as a GitHub Actions artifact.

Artifact name: `junit-test-results`.

## 10. Current Project Status

Implemented and verified:

- API automation tests.
- JSON schema validation.
- Playwright UI automation.
- Chromium and Firefox testing.
- GitHub Actions CI pipeline.
- Docker image creation and containerized test execution.
- JUnit XML report generation and persistence.
- Docker reproducibility verification.

Latest verified Docker test execution:

| Metric | Result |
|---|---:|
| Total tests | 41 |
| Passed | 41 |
| Failed | 0 |
| Errors | 0 |
| Skipped | 0 |

## 11. Future Enhancements

- Flaky test detection.
- Test execution analytics.
- AI-assisted test generation.
- AI response evaluation.
- Advanced quality gates.
- MLOps and LLMOps testing capabilities.

## 12. Learning Objectives

QualityForge AI is developed as a practical engineering project to build expertise in:

- Software testing and automation.
- API and UI validation.
- Python test framework development.
- CI/CD and DevOps practices.
- Docker and containerization.
- Software reliability engineering.
- AI-assisted software quality engineering.

---

**Project:** QualityForge AI
**Repository:** https://github.com/Rahul183269/QualityForge-AI
