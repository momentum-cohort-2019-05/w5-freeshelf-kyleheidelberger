# Generated by Django 2.2.2 on 2019-06-24 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Author of the book', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the book', max_length=100)),
                ('url', models.URLField(help_text='Unique URL for the book', unique=True)),
                ('description', models.TextField(help_text='A description of the book', max_length=2000)),
                ('date_added', models.DateField(auto_now_add=True, help_text='Date added to the database')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.Author')),
            ],
        ),
    ]