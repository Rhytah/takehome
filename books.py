from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    """ 
    Using Django ORM, write a function that will print the book title and the author name (who wrote it) 
    for all the books we have in the database. 
    """
    def print_booke_title_and_author():
        books = Book.objects.all().values_list('title', 'author__name')
        for book in books:
            print('"{}".{}'.format(book[0], book[1]))


    """
    Write another function that will print the author’s name and all the books he wrote. For all the authors we have in the database. Like this:

    Leo Tolstoy: “War and Peace”, “Anna Karenina”, “Resurrection”
    Alexandre Dumas: “The Three Musketeers”, “The Count of Monte Cristo”
    """
    def print_authors_name_and_all_books():
        authors = Author.objects.all().values_list('name', 'book__title')
        for author in authors:
            print('{}:{}'.format(author[0], author[1]))

    """
    Implement the third function, it should print the authors name and the number of books he wrote. 
    Order by the number of books written, descending. Like this:

    Leo Tolstoy: 3
    Alexandre Dumas: 2

    """
    def print_all_authors_and_number_of_books_ordered_in_descending_order():
        authors = Author.objects.all().annotate(book_count=Count('book')).order_by('-book_count')
        for author in authors:
            print('{}:{}'.format(author.name, author.book_count))
