from django.urls import path, include
from django.views.generic import TemplateView, ListView

from blogs.models import Entry
from .views import BlogListView, BlogDetailView
urlpatterns = [
    path('', BlogListView.as_view()),
    path('blog/', BlogListView.as_view()),
    path('register/', TemplateView.as_view(template_name="web/register.html")),
    path('login/', TemplateView.as_view(template_name="web/login.html")),
    path('blog/<int:pk>/', BlogDetailView.as_view()),
]
