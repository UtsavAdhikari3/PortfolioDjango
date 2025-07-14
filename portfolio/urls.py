from django.urls import path
from .views import HomePageView,ProjectDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  
    path('projects/<slug:slug>/',ProjectDetailView.as_view(),name='project-detail'),
]