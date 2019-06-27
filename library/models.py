from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    """
    A Model Class for authors of books in the database.
    """
    full_name = models.CharField(
        max_length=100, help_text="Author of the book")

    def __str__(self):
        """
        Returns the book's title as a string.
        """
        return self.full_name

    def get_absolute_url(self):
        """
        A function to return a link to book's unique page.
        """
        return reverse('author-detail', args=[str(self.id)])


class Book(models.Model):
    """
    A Model Class for books in the database.
    """
    title = models.CharField(max_length=100, help_text="Title of the book")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    url = models.URLField(max_length=200, unique=True,
                          help_text="Unique URL for the book")
    description = models.TextField(max_length=2000,
                                   help_text="A description of the book")
    date_added = models.DateField(auto_now_add=True,
                                  help_text="Date added to the database")
    cover = models.URLField(max_length=300, unique=True, blank=True,
                            null=True, help_text="Unique URL for the image of the book cover")
    category = models.ManyToManyField(
        'Category', help_text='Select categories for this book')
    favorite_of = models.ManyToManyField(
        User, blank=True, help_text="Add to favorites list for user")

    def get_absolute_url(self):
        """
        A function to return a link to book's unique page.
        """
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        """
        Returns the book's title as a string.
        """
        return self.title

    class Meta:
        ordering = ['-date_added']


class Category(models.Model):
    name = models.CharField(max_length=200, help_text="Book category")

    def get_absolute_url(self):
        """
        A function to return a link to book's unique page.
        """
        return reverse('category-detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        """
        Returns the book's title as a string.
        """
        return self.name


# class Favorite(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)

    # class Meta:
    #     unique_together = [['user', 'book']]
    
