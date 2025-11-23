from django.urls import path
import apps.post.views as views

app_name = 'post'

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='post-list'),
]