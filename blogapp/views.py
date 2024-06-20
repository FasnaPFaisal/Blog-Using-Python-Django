from django.shortcuts import render,redirect
from .forms import AddPostForm
from .models import AddPost

def index(request):
    posts = AddPost.objects.all()
    return render(request, 'index.html', {'posts': posts})

def about_me(request):
    return render(request, 'about-me.html')

def recent_posts(request):
    posts = AddPost.objects.all()
    return render(request, 'recent-posts.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = AddPostForm()
    return render(request,'add-post.html',{'form': form})

from django.shortcuts import render

def reading(request,id):
    post = AddPost.objects.get(id=id)
    return render(request, 'reading.html', {'post' : post})

def edit(request,id):
    post = AddPost.objects.get(id=id)
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddPostForm(instance=post)
    return render(request, 'edit.html', {'form': form, 'post': post})

def delete(request,id):
    post = AddPost.objects.get(id=id)
    post.delete()
    return redirect('index')  
        