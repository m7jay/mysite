from django.urls import path
from .views import *

urlpatterns = [
    path("", starting_page, name="start-page"),
    path("posts", all_posts, name="all-posts"),
    path("posts/<slug:slug>", individual_post,
         name="individual-post"),  # /posts/my-first-post
]
