from django.views import generic

from .models import Project


class IndexView(generic.ListView):
    model = Project
    template_name = 'portfolio/index.html'
    context_object_name = 'projects'


class DetailView(generic.DetailView):
    model = Project
    template_name = 'portfolio/detail.html'
