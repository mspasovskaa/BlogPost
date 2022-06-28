from django.db.models import Q
from django.shortcuts import render

from .forms import PostForm
from  .forms import BlockForm
from .models import Block, Author
from .models import Post

# Create your views here.

def posts(request):
    if request.user.is_superuser:
        return Post.objects.all()
    allposts = Post.objects.filter(~Q(author__user=request.user)).all()
    blockObjects = Block.objects.filter().all()
    if blockObjects:
        for b in blockObjects:
            for p in allposts:
                if b.bloking_user == request.user and b.bloked_user == p.author.user:
                    allposts = allposts.filter(~Q(title=p.title)).all()

    context={"posts":allposts}

    return render(request, 'posts.html',context=context)


def addpost(request):
    context = {"form":PostForm}
    return render(request, 'post.html', context=context)

def profile(request):
    posts = Post.objects.filter(author__user=request.user).all()
    author = Author.objects.filter(user=request.user).first()
    context={"posts":posts,"user":author}
    return render(request,'profile.html',context=context)

def blockedUsers(request):
    blocks=Block.objects.filter(bloking_user=request.user)
    form = BlockForm
    context = {"form": form,"blocks":blocks}
    return render(request,'blocked-users.html',context=context)

