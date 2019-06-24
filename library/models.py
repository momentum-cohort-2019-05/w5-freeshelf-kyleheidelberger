from django.db import models
from django.urls import reverse
# from PIL import Image

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
    # cover = models.ImageField(upload_to='MEDIA_ROOT/', required=False)
    # category = models.ManyToManyField('Category', help_text='Select categories for this book')

    def get_absolute_url(self):
        """
        A function to return a link to book's unique page.
        """
        return reverse('book', args=[str(self.id)])

    def __str__(self):
        """
        Returns the book's title as a string.
        """
        return self.title

    class Meta:
        ordering = ['-date_added']


# class Category(models.Model):
#     name = models.CharField(max_length=200, help_text="Book category")

#     def get_absolute_url(self):
#         """
#         A function to return a link to book's unique page.
#         """
#         return reverse('category', args=[str(self.id)])
