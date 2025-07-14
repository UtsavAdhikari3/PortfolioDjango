from django.views.generic import ListView
from .models import Project
from django.http import HttpResponse


class HomePageView(ListView):
    model = Project
    template_name = "portfolio/home.html"
    context_object_name = "projects"



def api_view(response):
    return HttpResponse("Api_view")