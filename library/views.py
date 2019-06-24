from django.shortcuts import render
from library.models import Book, Author#, Category

# Create your views here.


def index(request):
    """
    View function for home page of site.
    """
    num_books = Book.objects.count()

    context = {
        'num_books': num_books,
    }

    return render(request, 'index.html', context=context)
