from django.shortcuts import render_to_response, get_object_or_404
from .models import Blog, BlogType

# Create your views here.

def blog_list (request):
    context = {}
    context['blogs'] = Blog.objects.all()
    return render_to_response('blog/blog_list.html', context)


def blog_detail (request,pk):
    context = {}
    context['blog'] = get_object_or_404(Blog, id=pk)
    return render_to_response('blog/blog_detail.html', context)

def blog_with_type(request,blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType, id=blog_type_pk)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type'] = blog_type
    return render_to_response ('blog/blogs_witch_type.html', context)