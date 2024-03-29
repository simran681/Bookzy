# Generated by Django 3.2.4 on 2021-12-15 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_book_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
