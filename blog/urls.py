from django.urls import path
from .views import generate_post, post_detail, post_list, api_post_list, api_generate_post  # Ensure all views are imported

urlpatterns = [
    path('', post_list, name='post_list'),  # URL for the list of posts
    path('generate/', generate_post, name='generate_post'),  # URL for generating a new post
    path('post/<int:pk>/', post_detail, name='post_detail'),  # URL for viewing a specific post
    path('api/posts/', api_post_list, name='api_post_list'),  # API URL for listing posts
    path('api/generate/', api_generate_post, name='api_generate_post'),  # API URL for generating a new post
]