import ollama  

class ResearchAgent:
    def run(self, problem):
        prompt = f"""
        You are a research assistant. Provide a structured report on: '{problem}'.
        DO NOT include thinking, DO NOT include conversational filler.
        Return the report in exactly this format:
        
        ### ROOT CAUSES
        [List the causes]
        
        ### EXISTING SOLUTIONS
        [List the current solutions]
        
        ### MAJOR CHALLENGES
        [List the bottlenecks]
        """
        
        response = ollama.chat(model='qwen2:1.5b', messages=[
            {'role': 'user', 'content': prompt},
        ])
        return response['message']['content']