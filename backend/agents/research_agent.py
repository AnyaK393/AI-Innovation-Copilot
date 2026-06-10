from backend.prompts.research_prompt import RESEARCH_PROMPT
from backend.services.ollama_service import query_model

class ResearchAgent:

    def run(self, problem):

        prompt = RESEARCH_PROMPT.format(
            problem=problem
        )

        return query_model(prompt)