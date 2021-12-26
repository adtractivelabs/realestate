from .views import  *
from django.urls import path

app_name = 'rblog'

urlpatterns = [
    path('',blog_site,name='blog_site'),
    path('blog-details/<str:blog_slug>/',blog_details_view,name='blog_details_view'),
]
