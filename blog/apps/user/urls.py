from django.urls import path
import apps.user.views as views

app_name = 'user'

urlpatterns = [
    path('users/profile', views.UserProfileView.as_view(), name='user-profile'),
]