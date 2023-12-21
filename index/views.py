from django.shortcuts import render, get_object_or_404, redirect
from index.forms import BookForm

from index.models import Book

def indexView(request):
    qs = Book.objects.all()
    context = {'qs':qs}
    return render(request, 'index.html', context)

def createBook(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index:index')  # Redirect to a view that displays a list of books
    else:
        form = BookForm()

    return render(request, 'create_book.html', {'form': form})

def editBook(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index:index')  # Redirect to a view that displays a list of books
    else:
        form = BookForm(instance=book)

    return render(request, 'create_book.html', {'form': form, 'book': book})

def detailsView(request, id):
    qs = get_object_or_404(Book, id=id)    
    context = {'qs':qs}
    return render(request, 'details.html', context)


def deleteView(request, book_id):
    qs = get_object_or_404(Book, id=book_id)
    qs.delete()
    return redirect('index:index')


