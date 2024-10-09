from django.shortcuts import render
from .models import Post


def post_list(request):
    category = request.GET.get('category')

    if category:
        posts = Post.objects.filter(category=category)
    else:
        posts = Post.objects.all()

    return render(request, 'blog/post_list.html', {'posts': posts, 'selected_category': category})
