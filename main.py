from fastapi import FastAPI
from backend.agents.research_agent import ResearchAgent
from backend.agents.gap_analysis_agent import GapAnalysisAgent

app = FastAPI()

# Initialize our agents
researcher = ResearchAgent()
analyst = GapAnalysisAgent()

@app.post("/analyze")
async def analyze_problem(problem: str):
    # Step 1: Research
    print(f"Researching: {problem}...")
    research_results = researcher.run(problem)
    
    # Step 2: Gap Analysis
    print("Analyzing gaps...")
    gap_analysis = analyst.run(research_results)
    
    # Return both parts
    return {
        "problem": problem,
        "research": research_results,
        "innovation_gaps": gap_analysis
    }