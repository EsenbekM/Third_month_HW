from typing import List
from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import BlogPost, Comment
from .forms import BlogForm
# Create your views here.

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

class PostListView(ListView):
    template_name = 'index.html'
    queryset: List[BlogPost] = BlogPost.objects.all()
    context_object_name = "blogs"

class PostDetailView(DetailView):
    queryset = BlogPost.objects.all()
    template_name = "blog_detail.html"
    context_object_name = "blog"

    def get_context_data(self, **kwargs):
        context: dict = super(PostDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        comments: List[Comment] = Comment.objects.filter(post_id=pk)
        context["comments"] = comments
        return context

def blog_change_view(request, pk):
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            profile = BlogPost.objects.get(id=pk)
            data = form.cleaned_data
            if data.get("image"):
                profile.profile_pic = data.get("image")
            if data.get("title"):
                profile.age = data.get("title")
            if data.get("description"):
                profile.bio = data.get("description")

            profile.save()
            return HttpResponse("Ready!!")

        else:
            return render(request, "blog_change.html", context={"form": form})
    elif request.method == "GET":
        return render(request, "blog_change.html", context={"form": form})



def create_comment_view(request: HttpRequest, post_id):
    if request.method == "POST":
        data = request.POST
        if data.get("text"):
            Comment.objects.create(text=data["text"], post_id=post_id)
            return redirect("/blog/")
        else:
            return HttpResponse("Empty field ERROR!!!")



def create_blog_view(request: HttpRequest):
    if request.method == "POST":
        data = request.POST
        blog = BlogPost()
        form = BlogForm(request.POST, request.FILES)
            
        if data.get("title"):
            blog.title = data["title"]

        if data.get("description"):
            blog.description = data["description"]

        if form.is_valid():
            form.save()
    
        else:
            return HttpResponse("Empty field ERROR!!!")

        BlogPost.objects.create(
            title = blog.title,
            description = blog.description,
            image = blog.image,
        )

        return redirect("/blog/")

    if request.method == "GET":
        return render(request, 'create_blog.html')

def create_blog_view(request):
    if request.method == "POST":
        data = request.POST
        files = request.FILES
        title = data.get("title")
        description = data.get("description")
        image = files.get("image")
        BlogPost.objects.create(title=title, image=image, description=description)
        return redirect("/blog/")
    elif request.method == "GET":
        return render(request, "blog_create.html")
