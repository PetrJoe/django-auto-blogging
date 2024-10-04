import os
import time
from django.conf import settings
from together import Together

# Initialize the Together client with the API key from settings
client = Together(api_key=settings.TOGETHER_API_KEY)

def generate_blog_post(topic):
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="mistralai/Mixtral-8x7B-Instruct-v0.1",             
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that writes humanized, informative and engaging blog posts."},
                    {"role": "user", "content": f"Write a blog post about {topic}. The blog post should be informative and engaging."}
                ],
                max_tokens=500,
                temperature=0.7,
                top_p=0.7,
                top_k=50,
                repetition_penalty=1,
            )
            
            return response.choices[0].message.content.strip()
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(20)  # Wait for 20 seconds before retrying
            else:
                return f"Unable to generate content for {topic} due to API error: {str(e)}"

    return f"Failed to generate content for {topic} after {max_retries} attempts."
