import ollama

class InnovationAgent:

    def run(self, gap_analysis):

        prompt = f"""
        You are an innovation expert.

        Based on the following innovation opportunities and gaps:

        {gap_analysis}

        Generate 3 innovative project ideas.

        For each idea provide:

        1. Project Name
        2. Problem Solved
        3. Description
        4. Key Features
        5. Potential Impact

        Return in a clean structured format.
        """

        response = ollama.chat(
            model='qwen2:1.5b',
            messages=[
                {
                    'role': 'user',
                    'content': prompt
                }
            ]
        )

        return response['message']['content']