from django.shortcuts import render, get_object_or_404, redirect
from utils import GenericCRUDManager
from .models import Book
from .forms import BookForm

bookManager = GenericCRUDManager(Book)

# List all books (Read)
def book_list(request):
    books = bookManager.get_all()
    return render(request,'book_list.html',{'books':books})

# Create a new book
def book_create(request):
    form = BookForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            bookManager.create(form.cleaned_data)
            return redirect('book_list')
    return render(request, 'book_form.html', {'form':form})

# Update an existing book
def book_update(request, id):
    book = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance=book)
    if request.method == 'POST':
        if form.is_valid():
            bookManager.update(id, form.cleaned_data)
            return redirect('book_list')
    return render(request, 'book_form.html', {'form':form})
    
# Delete a book
def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        bookManager.delete(id)
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book':book})

