from django.contrib import admin
from django.urls import path, include
from store import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('', views.index, name='index page'),
    path('signup', views.signup, name='signup'),
    path('book',views.book,name='book',)
]
