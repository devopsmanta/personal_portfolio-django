from django.shortcuts import render
from django.views import generic

from .models import Post, Comment
from .forms import CommentForm


class IndexView(generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/index.html'

    def get_queryset(self):
        return Post.objects.all().order_by('-created_on')


def detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog/detail.html", context)


def category(request, category_name):
    posts = Post.objects.filter(
        categories__name__contains=category_name
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category_name,
        "posts": posts
    }
    return render(request, "blog/category.html", context)

