from django.urls import path
from . import views  # import your views

urlpatterns = [
    path('', views.api_view, name='api'),
]