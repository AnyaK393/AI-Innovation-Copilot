import ollama

try:
    print("Sending request to Qwen...")
    response = ollama.chat(model='qwen3:4b', messages=[
        {'role': 'user', 'content': 'What causes urban flooding? Keep it short.'},
    ])
    print("Response received!")
    print(response['message']['content'])
except Exception as e:
    print(f"Error: {e}")