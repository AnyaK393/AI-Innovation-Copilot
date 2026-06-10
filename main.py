from fastapi import FastAPI
from backend.agents.research_agent import ResearchAgent
from backend.agents.gap_analysis_agent import GapAnalysisAgent
from backend.agents.innovation_agent import InnovationAgent

app = FastAPI()

# Initialize our agents
researcher = ResearchAgent()
analyst = GapAnalysisAgent()
innovator = InnovationAgent()


@app.post("/analyze")
async def analyze_problem(problem: str):
    # Step 1: Research
    print(f"Researching: {problem}...")
    research_results = researcher.run(problem)
    
    # Step 2: Gap Analysis
    print("Analyzing gaps...")
    gap_analysis = analyst.run(research_results)
    
    # Return both parts
    print("Generating project ideas...")

    project_ideas = innovator.run(gap_analysis)

    return {
    "problem": problem,
    "research": research_results,
    "innovation_gaps": gap_analysis,
    "project_ideas": project_ideas
    }