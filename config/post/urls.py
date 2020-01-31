from django.urls import path

from post.views import post_list

urlpatterns = [
    path('', post_list, name='post-list')
]