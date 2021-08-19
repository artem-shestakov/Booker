from django.contrib import admin
from reviews.models import Publisher, Contributor, Book, BooksContributors, Review

admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book)
admin.site.register(BooksContributors)
admin.site.register(Review)
