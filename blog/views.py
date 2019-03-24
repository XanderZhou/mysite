from django.shortcuts import render_to_response, get_object_or_404
from .models import Blog

# Create your views here.

def blog_list (request):
    context = {}
    context['blogs'] = Blog.objects.all()
    return render_to_response('blog_list.html', context)


def blog_detail (request,pk):
    context = {}
    context['blog'] = get_object_or_404(Blog, id=pk)
    return render_to_response('blog_detail.html', context)