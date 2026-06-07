from fastapi import FastAPI
from backend.agents.research_agent import ResearchAgent

app = FastAPI()
research_agent = ResearchAgent()

@app.post("/research")
async def research(problem: str):
    result = research_agent.run(problem)
    return {"research_result": result}