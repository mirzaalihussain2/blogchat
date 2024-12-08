import os
from llm import chat_completion_openai, stream_chat_completion_openai

def load_blog_posts():
    blog_content = []
    blog_posts_dir = "blog_posts"
    
    # Check if directory exists
    if not os.path.exists(blog_posts_dir):
        return "No blog posts found."
    
    # Read all .txt files in the blog_posts directory
    for filename in os.listdir(blog_posts_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(blog_posts_dir, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    blog_content.append(content)
            except Exception as e:
                print(f"Error reading {filename}: {e}")
    
    return "\n\n".join(blog_content)

def get_chat_response(messages):
    information = load_blog_posts()
    system_prompt = f"You are Paul Graham and give startup advice. You are brief but insightful. You use PG's vocabulary, style and have his peculiarities. Do not say `Here is a quote`, or `I'm quoting PG` or anything like that. You actually ARE Paul Graham and talk in first person. You must limit your answers to 100 tokens."
    return chat_completion_openai(system_prompt, messages)

def get_streaming_response(messages):
    information = load_blog_posts()
    system_prompt = f"You are Paul Graham and give startup advice. You are brief but insightful. You use PG's vocabulary, style and have his peculiarities. Do not say `Here is a quote`, or `I'm quoting PG` or anything like that. You actually ARE Paul Graham and talk in first person. You must limit your answers to 100 tokens."
    return stream_chat_completion_openai(system_prompt, messages)

if __name__ == "__main__":
    # Example conversation
    messages = [
        {"role": "user", "content": "I have an asshole cofounder. How can I deal with him?"}
    ]
    
    # Regular chat completion
    print("\nRegular response:")
    response = get_chat_response(messages)
    print(response)
    
    # Streaming chat completion
    print("\nStreaming response:")
    for chunk in get_streaming_response(messages):
        print(chunk, end="", flush=True)
    print("\n")
