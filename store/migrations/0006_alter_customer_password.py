# Generated by Django 3.2.4 on 2021-12-15 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20211215_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Password',
            field=models.CharField(max_length=200),
        ),
    ]