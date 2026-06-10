RESEARCH_PROMPT = """
You are an expert researcher.

Analyze the following problem:

{problem}

Rules:
- Be concise
- Do not explain your reasoning
- Use bullet points only

Return EXACTLY:

### ROOT CAUSES
- cause 1
- cause 2
- cause 3

### EXISTING SOLUTIONS
- solution 1
- solution 2
- solution 3

### MAJOR CHALLENGES
- challenge 1
- challenge 2
- challenge 3
"""