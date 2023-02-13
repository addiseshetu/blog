from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'post_list.html', context)

def post_detail(request, id):
    context = {
        'post': Post.objects.get(pk=id)
    }
    return render(request, 'post_detail.html', context)
