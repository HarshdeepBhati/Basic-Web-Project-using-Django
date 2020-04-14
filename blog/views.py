from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'posts':posts})


def post(request, slug):
    print(slug)
    context = {'post': get_object_or_404(Post, slug=slug),'posts':'post'}
    return render(request, 'post.html', context)

def about(request):
    render(requests, 'about.html', {})


