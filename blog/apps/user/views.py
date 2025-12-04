from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView as LoginViewDjango
from django.contrib.auth.models import Group
from apps.user.forms import LoginForm
from django.urls import reverse_lazy

class UserProfileView(TemplateView):
    template_name = "user/user-profile.html"

class LoginView(LoginViewDjango):
    template_name = 'auth/auth-login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        registered_group = Group.objects.get(name='registered')
        self.object.groups.add(registered_group)

        return response