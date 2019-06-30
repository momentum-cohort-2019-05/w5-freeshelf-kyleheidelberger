from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='books'),
    path('book/<int:pk>', views.book_detail, name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(),
         name='category-detail'),
    path('favorites/<int:pk>', views.favorites, name='favorites'),
    path('book/<int:pk>/comment/',
         views.BookCommentCreate.as_view(),
         name='book_comment'),
    # path('book/<int:pk>/comment/<int:pk>/update/',
    #      views.BookCommentUpdate.as_view(),
    #      name='comment_update'),
    # path('book/<int:pk>/comment/<int:pk_comment>/delete/',
    #      views.BookCommentDelete.as_view(),
    #      name='comment-delete'),
    # path('book/<int:pk>/add', views.add_to_favorites, name="add-favorite"),
    # path('favorites/', views.FavoriteListView.as_view(), name='favorites'),

]
