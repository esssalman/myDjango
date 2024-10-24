from django.shortcuts import render, redirect, get_object_or_404
from utils import GenericCRUDManager
from .models import BlogPost
from .forms import BlogPostForm

blog_manager = GenericCRUDManager(BlogPost)

# List all blogs
def blog_list(request):
    blogs=blog_manager.get_all()
    return render(request,'blog_list.html', {'blogs':blogs})

# Create blog
def blog_create(request):
    form = BlogPostForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            blog_manager.create(form.cleaned_data)
            return redirect('blog_list')
    return render(request,'blog_form.html', {'form':form})

# Update blog
def blog_update(request,id):
    blog = get_object_or_404(BlogPost, id=id)
    form = BlogPostForm(request.POST or None, instance=blog)
    if request.method=='POST':
        if form.is_valid():
            blog_manager.update(id, form.cleaned_data)
            return redirect('blog_list')
    return render(request,'blog_form.html', {'form':form})

# Delete blog
def blog_delete(request,id):
    blog = get_object_or_404(BlogPost, id=id)
    if request.method=='POST':
        blog_manager.delete(id)
        return redirect('blog_list')
    return render(request,'blog_confirm_delete.html', {'blog':blog})
