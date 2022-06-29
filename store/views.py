
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View
from django.shortcuts import render, HttpResponse
from .models.book import Book
from .models.category import Category
from .models.customer import Customer
from django.contrib import messages
# Create your views here.
def index(request):
    book = None
    categories = Category.get_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        book = Book.get_books_by_id(categoryID)
    else:
        book = Book.get_books()
    data = {}
    data['books']=book
    data['categories']=categories
    return render(request, 'index.html', data)

def book(request):
    return render(request,'book.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        Password = request.POST.get('Password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email
        }

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            Password=Password)


        customer.save()
        messages.success(request, 'Contact request submitted successfully.')
        return render(request, 'signup.html', value)



        # saving