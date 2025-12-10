## This uses the llava llm, avaialble at: https://ollama.com/library/llava
## llava is used for analysing images
from ollama import chat
from ollama import ChatResponse

response = ChatResponse = chat(model="llava", messages=[
    {"role": "user",
     "content": "Whats in this image?"}
])
print(response['message']['content'])
print(response.message.content)