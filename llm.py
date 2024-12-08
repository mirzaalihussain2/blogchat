from openai import OpenAI
import os
from together import Together
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

together_client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
openai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
llama_model = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"
openai_model = "gpt-4o-mini"

# Rename existing functions and add OpenAI versions
def chat_completion_llama(system_prompt, messages):
    full_messages = [{"role": "system", "content": system_prompt}] + messages[-5:]
    
    response = together_client.chat.completions.create(
        model=llama_model,
        messages=full_messages,
        temperature=0.5,
        top_p=0.9,
        top_k=40,
        presence_penalty=0.5,
        frequency_penalty=0.5,
        stop=["<|eot_id|>", "Human:", "Assistant:"]
    )
    return response.choices[0].message.content

def chat_completion_openai(system_prompt, messages):
    full_messages = [{"role": "system", "content": system_prompt}] + messages[-5:]
    
    response = openai_client.chat.completions.create(
        model=openai_model,
        messages=full_messages,
        temperature=0.5,
        presence_penalty=0.5,
        frequency_penalty=0.5
    )
    return response.choices[0].message.content

def stream_chat_completion_llama(system_prompt, messages):
    full_messages = [{"role": "system", "content": system_prompt}] + messages[-5:]
    
    stream = together_client.chat.completions.create(
        model=llama_model,
        messages=full_messages,
        stream=True,
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

def stream_chat_completion_openai(system_prompt, messages):
    full_messages = [{"role": "system", "content": system_prompt}] + messages[-5:]
    
    stream = openai_client.chat.completions.create(
        model=openai_model,
        messages=full_messages,
        stream=True,
        temperature=0.5,
        presence_penalty=0.5,
        frequency_penalty=0.5
    )
    
    for chunk in stream:
        try:
            if chunk.choices and len(chunk.choices) > 0:
                if hasattr(chunk.choices[0].delta, 'content'):
                    yield chunk.choices[0].delta.content or ""
        except Exception as e:
            print(f"Error processing chunk: {e}")
            continue