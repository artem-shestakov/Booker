from django.db import models
from django.contrib import auth


class Publisher(models.Model):
    """A book's publisher"""
    name = models.CharField(
        max_length=100, 
        help_text="The name of the Publisher"
        )
    website = models.URLField(
        help_text="The Publisher's website"
        )
    email = models.EmailField(
        help_text="The Publisher's email address"
        )
    address = models.CharField(
        max_length=255, 
        help_text="The Publisher's address"
        )

    def __str__(self) -> str:
        return self.name


class Contributor(models.Model):
    first_name = models.CharField(
        max_length=50, 
        help_text="The contributor's first name"
        )
    last_name = models.CharField(
        max_length=50, 
        help_text="The contributor's last name"
        )
    email = models.EmailField(
        help_text="The contact email of the contributor"
        )

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


class Book(models.Model):
    """A published book"""
    title = models.CharField(
        max_length=100, 
        help_text="The title pf the book")
    publication_date = models.DateField(
        verbose_name="Date the book was published"
        )
    isbn = models.CharField(
        max_length=20, 
        verbose_name="ISBN numver of the book"
        )
    publisher = models.ForeignKey(
        Publisher, 
        on_delete=models.PROTECT
        )
    contributors = models.ManyToManyField(
        'Contributor', 
        through="BooksContributors"
        )
    
    def __str__(self) -> str:
        return self.title


class BooksContributors(models.Model):
    class ContrubutionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"
    book = models.ForeignKey(
        Book, on_delete=models.PROTECT
        )
    contributor = models.ForeignKey(
        Contributor, 
        on_delete=models.PROTECT
        )
    role = models.CharField(
        max_length=20, 
        verbose_name="The role of the contributor", 
        choices=ContrubutionRole.choices
        )


class Review(models.Model):
    content = models.TextField(
        help_text="The book's review"
        )
    rating = models.IntegerField(
        help_text="The given by review rating"
        )
    date_created = models.DateTimeField(
        auto_now_add=True, 
        help_text="The date and time the review was created"
        )
    date_edited = models.DateTimeField(
        auto_now_add=True, 
        help_text="The date and time the review was last edited"
        )
    author = models.ForeignKey(
        auth.get_user_model(), 
        on_delete=models.PROTECT
        )
    book = models.ForeignKey(
        Book, 
        help_text="The book that was reviewed",
        on_delete=models.PROTECT
        )