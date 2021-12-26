from django.shortcuts import render
from .models import  *
# Create your views here.

def blog_site(request):
    blogs = Blog.objects.all()
    return render(request,'blog/blogs.html',{'blog':blogs})


def blog_details_view(request,blog_slug):
    blog = Blog.objects.filter(blog_slug=blog_slug).order_by('-id')
    blog_details = []
    for i in blog :
        temp = {}
        temp['title']       = i.blog_title
        temp['photo']       = i.blog_image.url
        temp['desc']        = i.description
        temp['created_at']  = i.created_date
        temp['added_by']    = i.blog_author.name
        blog_details.append(temp)
    return render(request,'blog/blogs_details.html',{'blog_details':blog_details})
