from backend.prompts.gap_prompt import GAP_PROMPT
from backend.services.ollama_service import query_model

class GapAnalysisAgent:

    def run(self, research_data):

        prompt = GAP_PROMPT.format(
            research_data=research_data
        )

        return query_model(prompt)