from django.db import models
from .category import Category
# Create your models here.
class Book(models.Model):
    name= models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE , default=1)
    desc= models.CharField(max_length=200,default='best book ever')
    image= models.ImageField(upload_to='upload/products/')
    file=models.FileField(upload_to='upload/books/', null=True, blank=True)
    author=models.CharField(max_length=50, default='NA')

    @staticmethod
    def get_books():
        return Book.objects.all()

    @staticmethod
    def get_books_by_id(category_id):
        if category_id:
            return Book.objects.filter(category=category_id)
        else:
            return Book.get_books();