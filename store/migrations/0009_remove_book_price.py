# Generated by Django 3.2.4 on 2022-02-03 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='price',
        ),
    ]
