from django.shortcuts import render, get_object_or_404, redirect
from library.models import Book, Author, Category, Favorite
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from .forms import FavForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):
    """
    View function for home page of site.
    """
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_categories = Category.objects.count()
    recent_book_list = Book.objects.order_by('date_added')[:3]

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_categories': num_categories,
        'recent_book_list': recent_book_list,
    }

    return render(request, 'index.html', context=context)

# class BookListView(generic.ListView):
#     model = Book


def book_list(request):
    valid_sorts = ['title', 'author', 'date_added']

    sort = request.GET.get('sort', default='date_added')
    if sort not in valid_sorts:
        sort = 'date_added'
    book_list = Book.objects.all().order_by(sort)

# did some pagination but it won't save sort across pages without cookies...
    # page = request.GET.get('page', 1)

    # paginator = Paginator(book_list, 2)
    # try:
    #     book_list = paginator.page(page)
    # except PageNotAnInteger:
    #     users = paginator.page(1)
    # except EmptyPage:
    #     users = paginator.page(paginator.num_pages)

    return render(request, 'library/book_list.html', {
        'book_list': book_list,
        'sort': sort,
        'valid_sorts': valid_sorts,
    })


# class BookDetailView(generic.DetailView):
#     model = Book


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author


class CategoryListView(generic.ListView):
    model = Category


class CategoryDetailView(generic.DetailView):
    model = Category


@login_required
def favorites(request, pk):
    valid_sorts = ['title', 'author', 'date_added', 'date_favorited']
    user = User.objects.get(id=pk).username
    sort = request.GET.get('sort', default='date_favorited')
    if sort not in valid_sorts:
        sort = 'date_favorited'

    book_list = []
    favorites_list = request.user.favorite_set.all()
    for favorite in favorites_list:
        book_list.append(favorite.book)

    return render(request, 'library/favorites.html', {
        'user': user,
        'book_list': book_list,
        'sort': sort,
        'valid_sorts': valid_sorts,
        'favorites_list': favorites_list,
    })


@login_required
def book_detail(request, pk):
    if request.method == 'POST':
        form = FavForm(request.POST)
        if form.is_valid():
            favorited = form.cleaned_data['favorited']
            book = Book.objects.get(pk=pk)
            if favorited:
                new_fav = Favorite(user=request.user, book=book)
                book.num_favorited += 1
                book.save()
                new_fav.save()
            else:
                old_fav = Favorite.objects.filter(
                    user=request.user).filter(book=book).first()
                book.num_favorited -= 1
                book.save()
                old_fav.delete()

        return redirect(to='book-detail', pk=pk)

    else:
        form = FavForm()
        book = Book.objects.get(pk=pk)
        fave_list = book.favorite_set.all()
        favorite_users = []
        for favorite in fave_list:
            favorite_users.append(favorite.user)
        return render(request, 'library/book_detail.html', {
            'book': book,
            'favorite_users': favorite_users,
            'form': form
        })


# FAILED ATTEMPT AT USING SAME CODE FROM BOOK LIST TO SORT CATEGORIES
# def category_detail(request, pk):
#     valid_sorts = ['title', 'author', 'date_added']

#     sort = request.GET.get('sort', default='date_added')
#     if sort not in valid_sorts:
#         sort = 'date_added'
#     book_list = Book.objects.all().order_by(sort)

#     return render(request, 'library/book_list.html', {
#         'book_list' : book_list,
#         'sort' : sort,
#         'valid_sorts' : valid_sorts,
#     })

# MAY REUSE THIS PART
# class FavoriteListView(View):

#     def get(self, request):
#         form = FavForm()
#         return self.favorites_view(request, form)

#     def favorites_view(self, request, form):
#         if request.user.is_authenticated:
#             user_favorites = Book.objects.filter(favorite_of=request.user)
#         else:
#             user_favorites = []

#         return render(request, 'library/favorites.html', {
#             "user_favorites": user_favorites,
#             "form": form,
#         })


# ALL MY FAILED ATTEMPTS AT ADDING FAVORITES WHILE STILL USING MY MANY TO MANY MODEL
# def add_to_favorites(request, user_favorites, pk):
#     if request.method == 'POST':
#         form = FavForm(request.POST)
#         if form.is_valid():
#             favorited = form.cleaned_data['favorited']
#             favorite = Book.objects.get(pk=pk)
#             if favorited:
        #         add_to_favorites(book, favorite_of=request.user)
        #         user_favorites.append(book)
        #         user_favorites.save()
        #         messages.success(
        #             request, f"The book '{book.title}' was added to your Favorites list.")

        # return redirect(to='book-detail', pk=pk)

    # else:
    #     form = FavForm()

    # if user.is_authenticated and book not in user_favorites:
    #     form = FavForm(data=request.POST)
    #     if form.is_valid():
    #         favorite = form.cleaned_data['favorite']
    #         book.add_to_favorites(favorite, request.user)
    #         book += user_favorites
    #         user_favorites.save()
    #         messages.success(
    #             request, f"The book '{book.title}' was added to your Favorites list.")
    #         return redirect(to='book-detail')
    #     elif book in user_favorites:
    #         messages.warning(
    #             request, "You already added that book as a favorite!")
    # else:
    #     form = FavForm()

    # return self.favorites_view(request, form)

# class FavoriteListView(generic.ListView):
#     model = Favorite
