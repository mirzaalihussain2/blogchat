import os
from together import Together
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
model = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"

def chat_completion(system_prompt, messages, max_tokens=None):
    # Add system prompt to the beginning of messages
    full_messages = [{"role": "system", "content": system_prompt}] + messages[-5:]  # Only keep last 5 messages
    
    response = client.chat.completions.create(
        model=model,
        messages=full_messages,
        # max_tokens=max_tokens or 100,
        temperature=0.5,
        top_p=0.9,
        top_k=40,
        presence_penalty=0.5,
        frequency_penalty=0.5,
        stop=["<|eot_id|>", "Human:", "Assistant:"]
    )
    return response.choices[0].message.content

def stream_chat_completion(system_prompt, messages, max_tokens=None):
    # Add system prompt to the beginning of messages
    full_messages = [{"role": "system", "content": system_prompt}] + messages[-5:]  # Only keep last 5 messages
    
    stream = client.chat.completions.create(
        model=model,
        messages=full_messages,
        stream=True,
        # max_tokens=max_tokens or 100,
        temperature=0.5,
        top_p=0.9,
        top_k=40,
        presence_penalty=0.5,
        frequency_penalty=0.5,
        stop=["<|eot_id|>", "Human:", "Assistant:"]
    )
    
    for chunk in stream:
        try:
            if chunk.choices and len(chunk.choices) > 0:
                if hasattr(chunk.choices[0].delta, 'content'):
                    yield chunk.choices[0].delta.content or ""
        except Exception as e:
            print(f"Error processing chunk: {e}")
            continue