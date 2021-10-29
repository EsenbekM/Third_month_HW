from typing import List
from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import BlogPost, Comment

# Create your views here.

def blog_view(request):
    user = request.user
    blogs: List[BlogPost] = BlogPost.objects.all()
    return render(request, 'index.html', context={'blogs':blogs})

def blog_detail_view(request: HttpRequest, id: int):
    blog = BlogPost.objects.get(id=id)
    comments = Comment.objects.filter(post_id = id)
    return render(request, 'blog_detail.html', context={'blog':blog, 'comments':comments})   

def create_comment_view(request: HttpRequest, post_id):
    if request.method == "POST":
        data = request.POST
        if data.get("text"):
            Comment.objects.create(text=data["text"], post_id=post_id)
            return redirect("/blog/")
        else:
            return HttpResponse("Empty field ERROR!!!")
