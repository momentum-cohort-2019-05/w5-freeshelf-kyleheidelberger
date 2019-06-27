from django.shortcuts import render
from library.models import Book, Author, Category
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from .forms import FavForm
from django.contrib import messages

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


class FavoriteListView(View):

    def get(self, request):
        form = FavForm()
        return self.favorites_view(request, form)

    def add_to_favorites(self, user, user_favorites):
        if user.is_authenticated and book not in user_favorites:
            form = FavForm(data=request.POST)
            if form.is_valid():
                favorite = form.cleaned_data['favorite']
                book.add_to_favorites(favorite, request.user)
                book += user_favorites
                user_favorites.save()
                messages.success(
                    request, f"The book '{book.title}' was added to your Favorites list.")
                return redirect(to='book-detail')
            elif book in user_favorites:
                messages.warning(
                    request, "You already added that book as a favorite!")
        else:
            form = FavForm()

        return self.favorites_view(request, form)

    def favorites_view(self, request, form):
        if request.user.is_authenticated:
            user_favorites = Book.objects.filter(favorite_of=request.user)
        else:
            user_favorites = []

        return render(request, 'library/favorites.html', {
            "user_favorites": user_favorites,
            "form": form,
        })
