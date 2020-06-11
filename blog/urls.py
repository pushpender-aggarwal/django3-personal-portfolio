from django.urls import path
from . import views

app_name = 'blog' # use to distinguish between different apps in the project for the redirection of the url from the project urls.py

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>', views.detail, name='detail'),
]