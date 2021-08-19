from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.books_list, name='books_list'),
    path('books/<int:id>', views.book_detail, name='book_detail')
]