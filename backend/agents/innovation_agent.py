from backend.prompts.innovation_prompt import INNOVATION_PROMPT
from backend.services.ollama_service import query_model

class InnovationAgent:

    def run(self, gap_analysis):

        prompt = INNOVATION_PROMPT.format(
            gap_analysis=gap_analysis
        )

        return query_model(prompt)