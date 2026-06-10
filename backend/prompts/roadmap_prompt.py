ROADMAP_PROMPT= """
You are a senior software architect.

Project Ideas:

{project_ideas}

Select the BEST project idea.

Create an implementation roadmap.

Return EXACTLY:

### PROJECT SELECTED

Project Name

### PHASE 1
Objectives
Deliverables

### PHASE 2
Objectives
Deliverables

### PHASE 3
Objectives
Deliverables

### TECH STACK

Frontend:
Backend:
Database:
AI:
Deployment:

### ESTIMATED TIMELINE

Week 1:
Week 2:
Week 3:
Week 4:

IMPORTANT:
Return only the requested output.
Do not explain.
Do not add introductions.
Do not add conclusions.
Do not add conversational text.
"""