from fastapi import FastAPI
from backend.agents.research_agent import ResearchAgent
from backend.agents.gap_analysis_agent import GapAnalysisAgent
from backend.agents.innovation_agent import InnovationAgent
from backend.agents.roadmap_agent import RoadmapAgent

app = FastAPI()

# Initialize our agents
researcher = ResearchAgent()
analyst = GapAnalysisAgent()
innovator = InnovationAgent()
roadmapper = RoadmapAgent()


@app.post("/analyze")
async def analyze_problem(problem: str):

    # Step 1: Research
    print(f"Researching: {problem}...")
    research_results = researcher.run(problem)

    # Step 2: Gap Analysis
    print("Analyzing gaps...")
    gap_analysis = analyst.run(research_results)

    # Step 3: Innovation
    print("Generating project ideas...")
    project_ideas = innovator.run(gap_analysis)

    # Step 4: Roadmap
    print("Creating roadmap...")
    roadmap = roadmapper.run(project_ideas)

    return {
        "problem": problem,
        "research": research_results,
        "innovation_gaps": gap_analysis,
        "project_ideas": project_ideas,
        "roadmap": roadmap
    }