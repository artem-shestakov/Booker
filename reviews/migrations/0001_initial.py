# Generated by Django 3.2.6 on 2021-08-12 14:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title pf the book', max_length=100)),
                ('publication_date', models.DateField(verbose_name='Date the book was published')),
                ('isbn', models.CharField(max_length=20, verbose_name='ISBN numver of the book')),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text="The contributor's first name", max_length=50)),
                ('last_name', models.CharField(help_text="The contributor's last name", max_length=50)),
                ('email', models.EmailField(help_text='The contact email of the contributor', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the Publisher', max_length=100)),
                ('website', models.URLField(help_text="The Publisher's website")),
                ('email', models.EmailField(help_text="The Publisher's email address", max_length=254)),
                ('address', models.CharField(help_text="The Publisher's address", max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text="The book's review")),
                ('rating', models.IntegerField(help_text='The given by review rating')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='The date and time the review was created')),
                ('date_edited', models.DateTimeField(auto_now_add=True, help_text='The date and time the review was last edited')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('book', models.ForeignKey(help_text='The book that was reviewed', on_delete=django.db.models.deletion.PROTECT, to='reviews.book')),
            ],
        ),
        migrations.CreateModel(
            name='BooksContributors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('AUTHOR', 'Author'), ('CO_AUTHOR', 'Co-Author'), ('EDITOR', 'Editor')], max_length=20, verbose_name='The role of the contributor')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reviews.book')),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reviews.contributor')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='contributors',
            field=models.ManyToManyField(through='reviews.BooksContributors', to='reviews.Contributor'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reviews.publisher'),
        ),
    ]
