from django.views.generic import TemplateView

class PostListView(TemplateView):
    template_name = "post/post-list.html"