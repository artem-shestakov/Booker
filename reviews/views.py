from reviews.utils import average_raring
import reviews
from reviews.models import Book, BooksContributors
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, "base.html")

def books_list(request):
    '''Get all books'''
    books = Book.objects.all()
    books_list = []
    # Prepare context for template
    for book in books:
        # Get book's reviews
        reviews = book.review_set.all()
        if reviews:
            number_of_review = len(reviews)
            rating = average_raring([review.rating for review in reviews])
        else:
            number_of_review = 0
            rating = 0
        # Get author from contributers
        authors = []
        book_contributors = book.contributors.all()
        for contributor in book_contributors:
            # If current book's contributer has author role
            if BooksContributors.objects.get(contributor=contributor).role == 'AUTHOR':
                authors.append(contributor)
        books_list.append({
            'book': book,
            'authors': authors,
            'number_of_review': number_of_review,
            'rating': rating
        })
    context = {
        'books_list': books_list
    }
    return render(request, 'books_list.html', context)

def book_detail(request, id):
    '''Get book information by ID'''
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
