GAP_PROMPT  = """
You are an innovation strategist.

Research Data:

{research_data}

Task:

1. Analyze weaknesses in current solutions.
2. Identify unmet needs.
3. Find opportunities where innovation can create significant impact.

Rules:
- Focus on gaps, not summaries.
- Avoid repeating research findings.
- Think like a startup founder.
- Keep output concise.

Return EXACTLY:

### IDENTIFIED GAPS
- gap 1
- gap 2
- gap 3

### INNOVATION OPPORTUNITIES
- opportunity 1
- opportunity 2
- opportunity 3

IMPORTANT:
Return only the requested output.
Do not explain.
Do not add introductions.
Do not add conclusions.
Do not add conversational text.
"""