# Generated by Django 3.2.4 on 2022-02-03 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_customer_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='NA', max_length=50),
        ),
    ]
