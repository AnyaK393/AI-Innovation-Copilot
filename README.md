# AI Innovation Copilot

## Overview

AI Innovation Copilot is an Agentic AI system that transforms a real-world problem statement into research-backed innovation opportunities.

Instead of functioning as a traditional chatbot, the system follows a multi-step reasoning workflow:

Problem → Research → Gap Analysis → Innovation Opportunities

The goal is to help students, researchers, innovators, and startups identify high-impact project ideas from complex real-world challenges.

---

## Features

### Research Agent

Analyzes a user-provided problem and generates:

- Root Causes
- Existing Solutions
- Major Challenges

### Gap Analysis Agent

Consumes the research output and identifies:

- Unsolved problems
- Missing capabilities in current solutions
- High-impact innovation opportunities

### Multi-Agent Workflow

The output of one AI agent becomes the input for another agent.

Workflow:

Problem Statement
      ↓
Research Agent
      ↓
Gap Analysis Agent
      ↓
Innovation Opportunities

### Local LLM Execution

Runs entirely on the user's machine using:

- Ollama
- Qwen3:4B

Benefits:

- No API costs
- Full privacy
- Offline capable

---

## Tech Stack

### Backend

- Python
- FastAPI

### AI Layer

- Ollama
- Qwen3:4B

### Data Validation

- Pydantic

---

## Project Structure

AI_Innovation_Copilot/

├── backend/

│   └── agents/

│       ├── research_agent.py

│       └── gap_analysis_agent.py

│

├── docs/

├── models/

├── rag/

├── workflows/

│

├── main.py

├── requirements.txt

└── README.md

---

## Architecture

User Problem
      ↓
FastAPI Endpoint
      ↓
Research Agent
      ↓
Research Report
      ↓
Gap Analysis Agent
      ↓
Innovation Opportunities
      ↓
API Response

---

## Installation

### Clone Repository

git clone <repository-url>

cd AI_Innovation_Copilot

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

Mac/Linux:

source venv/bin/activate

Windows:

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

---

## Install Ollama

Download Ollama and install it.

Pull the model:

ollama pull qwen3:4b

Start Ollama:

ollama serve

---

## Running The Application

Start FastAPI:

uvicorn main:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs

---

## API Endpoint

### POST /analyze

Input:

Urban flooding in Indian cities

Output:

{
    "problem": "...",
    "research": "...",
    "innovation_gaps": "..."
}

---

## Example Use Cases

- Disaster Management
- Smart Cities
- Environmental Sustainability
- Healthcare Innovation
- Agricultural Technology
- Education Technology

---

## Current Status

Completed:

- FastAPI Backend
- Research Agent
- Gap Analysis Agent
- Ollama Integration
- Qwen3 Integration
- Multi-Agent Workflow

Planned:

- Innovation Agent
- Roadmap Agent
- Report Generation Agent
- RAG Integration
- PDF Upload Support
- Frontend Dashboard

---

## Future Vision

The long-term goal is to create a complete AI Innovation Copilot capable of:

- Researching complex problems
- Identifying solution gaps
- Generating project ideas
- Designing implementation roadmaps
- Producing complete project proposals

This shifts AI from simple question-answering toward autonomous innovation assistance.