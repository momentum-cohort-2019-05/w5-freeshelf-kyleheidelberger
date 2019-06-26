from django.shortcuts import render
from library.models import Book, Author, Category
from django.views import generic

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


class BookListView(generic.ListView):
    model = Book


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author


class CategoryListView(generic.ListView):
    model = Category


class CategoryDetailView(generic.DetailView):
    model = Category
