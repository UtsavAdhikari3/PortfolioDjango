from django.views.generic import ListView,DetailView
from .models import Project
from django.http import HttpResponse


class HomePageView(ListView):
    model = Project
    template_name = "portfolio/home.html"
    context_object_name = "projects"



class ProjectDetailView(DetailView):
    model = Project
    template_name = "portfolio/project_detail.html"
    context_object_name = "project"

def api_view(response):
    return HttpResponse("Api_view")