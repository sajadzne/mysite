from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.

def blog_View(request):
    posts = Post.objects.filter(status = 1)
    context = {"posts" : posts}
    return render(request, 'blog/blog-home.html',context)

def blog_single(request,pid):
    posts = list(Post.objects.filter(status = 1))
    post = get_object_or_404(Post,pk=pid)
    index = posts.index(post)
    previous_post = None

    if index > 0:
        previous_post = posts[index - 1]
    next_post = None

    if index < len(posts) - 1:
        next_post = posts[index + 1]
    context = {
    "post": post,
    "previous_post": previous_post,
    "next_post": next_post,
    }
    return render(request, 'blog/blog-single.html', context)

def test(request,pid):
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post,pk=pid)
    context = {"post" : post}
    return render(request, 'test.html',context)