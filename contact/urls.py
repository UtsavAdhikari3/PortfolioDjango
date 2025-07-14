from django.urls import path
from . import views  # import your views

urlpatterns = [
    path('', views.home_view, name='home'),  # add a home view
]