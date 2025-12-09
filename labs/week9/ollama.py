## This uses the llava llm, avaialble at: https://ollama.com/library/llava
from ollama import chat
from ollama import ChatResponse

response = ChatResponse = chat(model="llava", messages=[
    {"role": "user",
     "content": "Why is the sky blue?"}
])
print(response['message']['content'])
print(response.message.content)