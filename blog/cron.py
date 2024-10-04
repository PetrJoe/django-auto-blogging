import random
from .models import BlogPost
from .ai_generator import generate_blog_post

def generate_hourly_post():
    topics = [
        "Technology trends",
        "Artificial Intelligence",
        "Climate change",
        "Health and wellness",
        "Space exploration",
        "Sustainable living",
        "Cybersecurity",
        "Quantum computing",
        "Renewable energy",
        "Future of work"
    ]
    
    topic = random.choice(topics)
    content = generate_blog_post(topic)
    BlogPost.objects.create(title=f"Hourly Update: {topic}", content=content)
    print(f"Generated new blog post: {topic}")