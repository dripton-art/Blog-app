from django.shortcuts import render, redirect
from .models import PostModel
from .forms import PostmodelForm

# Create your views here.

def index(request):
    posts = PostModel.objects.all()
    if request.method == 'POST':
        form = PostmodelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog-index')
    else:
        form = PostmodelForm()
    context = {
        'posts': posts,
        'form': form
    }

    return render(request, 'blog/index.html', context)
