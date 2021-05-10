from django.shortcuts import render, redirect
from .models import Post
import datetime
# Create your views here.
def home(request):
    posts = Post.objects.all().order_by("dday", "pk")

    return render(request, 'home.html', {'posts': posts})

def new(request): 

    if(request.method=='POST'):
        temp_date = datetime.datetime.strptime(request.POST['date'], "%Y-%m-%d").date()
        temp_dday = (temp_date - datetime.date.today()).days

        post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            date = temp_date,
            date_str = request.POST['date'],
            dday = temp_dday,
        )
        return redirect('detail', post.pk)

    return render(request, 'new.html')

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    return render(request, 'detail.html', {'post': post,})

def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if (request.method=='POST'):
        temp_date = datetime.datetime.strptime(request.POST['date'], "%Y-%m-%d").date()
        temp_dday = (temp_date - datetime.date.today()).days

        Post.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            date = temp_date,
            date_str = request.POST['date'],
            dday = temp_dday,
        )
        return redirect('detail', post.pk)

    return render(request, 'edit.html', {'post': post,})

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')

def delete_all(request):
    posts = Post.objects.all()
    posts.delete()

    return redirect('home')