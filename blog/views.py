from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .ai_generator import generate_blog_post
from .models import BlogPost
from django.core.paginator import Paginator
from django.shortcuts import render, redirect


def generate_post(request):
    if request.method == 'POST':
        topic = request.POST.get('topic')
        content = generate_blog_post(topic)
        post = BlogPost.objects.create(title=topic, content=content)
        return redirect('post_detail', pk=post.pk)
    return render(request, 'generate_post.html')

def post_detail(request, pk):
    post = BlogPost.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'post_list.html', {'page_obj': page_obj})


@require_http_methods(["GET"])
def api_post_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')[:10]
    data = [{"id": post.id, "title": post.title, "content": post.content} for post in posts]
    return JsonResponse(data, safe=False)

@csrf_exempt
@require_http_methods(["POST"])
def api_generate_post(request):
    data = json.loads(request.body)
    topic = data.get('topic')
    if not topic:
        return JsonResponse({"error": "Topic is required"}, status=400)
    content = generate_blog_post(topic)
    post = BlogPost.objects.create(title=topic, content=content)
    return JsonResponse({"id": post.id, "title": post.title, "content": post.content})