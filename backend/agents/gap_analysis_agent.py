import ollama

class GapAnalysisAgent:
    def run(self, research_data):
        prompt = f"""
        Analyze the following research:
        {research_data}
        
        Identify the 'Gaps'—what are the problems that existing solutions are failing to address?
        Propose 3 specific, novel, and high-impact innovation opportunities based on these gaps.
        """
        
        response = ollama.chat(model='qwen3:4b', messages=[
            {'role': 'user', 'content': prompt},
        ])
        return response['message']['content']