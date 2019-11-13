from django.shortcuts import render, redirect, get_object_or_404

from .forms import PostForm
from .models import Post

from django.http import JsonResponse

# Create your views here.


def index(request):

    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'posts/index.html', context)


def create(request):

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)
            post.user = request.user
            post.save()

            return redirect('posts:index')
    else:
        form = PostForm()

    context = {
        'form': form
    }

    return render(request, 'posts/form.html', context)


def like(request, id):

    if request.is_ajax():

        post = get_object_or_404(Post, id=id)
        user = request.user

        if post.like_users.filter(id=user.id):
            post.like_users.remove(user)
            is_like = False
        else:
            post.like_users.add(user)
            is_like = True
            
        context = {
            'is_like': is_like,
            'like_users': post.like_users.count(),
        }

        return JsonResponse(context)
    else:
        return JsonResponse({'message': 'wrong request'})
