from fastapi import FastAPI
from backend.agents.research_agent import ResearchAgent

app = FastAPI()

research_agent = ResearchAgent()


@app.get("/")
def home():

    return {
        "message": "AI Innovation Copilot is running"
    }


@app.post("/research")
def research(problem: str):

    result = research_agent.run(problem)

    return result