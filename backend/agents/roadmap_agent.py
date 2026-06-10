from backend.prompts.roadmap_prompt import ROADMAP_PROMPT
from backend.services.ollama_service import query_model

class RoadmapAgent:

    def run(self, project_ideas):

        prompt = ROADMAP_PROMPT.format(
            project_ideas=project_ideas
        )

        return query_model(prompt)