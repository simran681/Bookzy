# Generated by Django 3.2.4 on 2021-12-15 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='password',
        ),
        migrations.AddField(
            model_name='customer',
            name='Password',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]