# Generated by Django 2.2.2 on 2019-06-29 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_auto_20190629_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.Author', verbose_name='Book Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_added',
            field=models.DateField(auto_now_add=True, help_text='Date added to the database', verbose_name='Date Added to Library'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(help_text='Title of the book', max_length=100, verbose_name='Book Title'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='date_favorited',
            field=models.DateField(auto_now_add=True, verbose_name='Date Favorited'),
        ),
    ]
