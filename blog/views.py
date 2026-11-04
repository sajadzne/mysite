from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.

def blog_View(request,**kwargs):
    posts = Post.objects.filter(status = 1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
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

# def test(request):
#     return render(request, 'test.html')

def test(request):
    post = Post.objects.first()
    context = {"post": post}
    return render(request, 'test.html', context)

def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {"posts": posts}
    return render(request, 'blog/blog-home.html',context)


def blog_search(request):
    # print(request.__dict__)
    posts = Post.objects.filter(status = 1)
    if request.method == 'GET':
        #  print(request.GET.get('s'))
        if s := request.GET.get("s"):
            posts = posts.filter(content__contains=s)
    
    context = {"posts" : posts}
    return render(request, 'blog/blog-home.html',context)