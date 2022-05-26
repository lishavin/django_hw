from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from django.utils import timezone

def home(request):
    posts = Post.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts':posts})

def newpost(request):
    return render(request, 'newpost.html')

def create(request):
    if(request.method == 'POST' or request.method == 'FILES'):
        post = Post()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.photo = request.FILES['photo']
        post.date = timezone.now()
        post.save()
    return redirect('home')

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form':comment_form})

def input_comment(request, post_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.save()
    return redirect('detail', post_id)
    