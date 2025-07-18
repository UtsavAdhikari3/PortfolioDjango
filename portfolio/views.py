from django.views.generic import ListView,DetailView
from .models import Project
from django.http import HttpResponse
from django.conf import settings

class HomePageView(ListView):
    model               = Project
    template_name       = "portfolio/home.html"
    context_object_name = "projects"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["intro"] = settings.PORTFOLIO_INTRO  # <‑‑ add
        return ctx



class ProjectDetailView(DetailView):
    model = Project
    template_name = "portfolio/project_detail.html"
    context_object_name = "project"

def api_view(response):
    return HttpResponse("Api_view")