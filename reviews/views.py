from reviews.utils import average_raring
import reviews
from reviews.models import Book
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, "base.html")

def books_list(request):
    books = Book.objects.all()
    books_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            number_of_review = len(reviews)
            rating = average_raring([review.rating for review in reviews])
        else:
            number_of_review = 0
            rating = 0
        books_list.append({
            'book': book,
            'number_of_review': number_of_review,
            'rating': rating
        })
    context = {
        'books_list': books_list
    }
    return render(request, 'books_list.html', context)

def book_detail(request, id):
    book = get_object_or_404(Book, pk=id)
    reviews = book.review_set.all()
    if reviews:
        rating = average_raring([review.rating for review in reviews])
    else:
        rating = 0
    context = {
        'book': book,
        'rating': rating,
        'reviews': reviews
    }
    return render(request, "book.html", context)

def search(request):
    search_text = request.GET.get("search", "") 
    return render(request, "search.html", {
        "search_item": search_text
    })