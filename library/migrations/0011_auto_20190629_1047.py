# Generated by Django 2.2.2 on 2019-06-29 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_auto_20190628_1405'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorite',
            options={'ordering': ['-date_favorited']},
        ),
    ]
