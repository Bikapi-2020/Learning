from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import redirect

# Create your views here.

def homepage(request):
    template = get_template('myblog/index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())


    return HttpResponse(html)

def detail(request, slug):
    template = get_template('myblog/post.html')

    post = Post.objects.get(slug=slug)
    if post != None:
        html = template.render(locals())
        return HttpResponse(html)
    # try:
    #     post = Post.object.get(sulg=slug)
    #     if post != None:
    #         html = template.render(locals())
    #         return HttpResponse(html)
    #
    # except:
    #     return redirect('/')



