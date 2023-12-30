# your_app/management/commands/create_initial_data.py

from django.core.management.base import BaseCommand
from libraryapp.models import Book, User, Librarian, BorrowBook, ReturnBook


class Command(BaseCommand):
    help = 'Creates initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_book()
        self.create_librarian()

    def create_book(self):
        # Create Book instances
        book1 = Book(title="A Midsummer Night's Dream", book_id=0001.1, author="William Shakespeare", genre="Comedy", publisher="N/A", year=1600)
        book2 = Book(title="Othello", book_id=0002.0, author="William Shakespeare", genre="Tragedy", publisher="Isaac Jaggard and Ed. Blount", year=1622)
        book3 = Book(title="To Kill a Mockingbird", book_id=0003.5, author="Harper Lee", genre="Fiction", publisher="J.B. Lippincott & Co.", year=1960)
        book4 = Book(title="The Great Gatsby", book_id=0004.25, author="F.Scott Fitzgerald", genre="Fiction", publisher="Charles Scribner's Sons", year=1925)
        book5 = Book(title="Harry Potter and the Philosopher's Stone", book_id=0005.0, author="J.K. Rowling", genre="Fantasy", publisher="Bloomsbury", year=1997)
        book6 = Book(title="The Girl with the Dragon Tattoo", book_id=0006.0, author="Stieg Larsson", genre=" Mystery, Thriller", publisher="Norstedts Förlag", year=2005)
        book7 = Book(title="The Hunger Games", book_id=0007.0, author="Suzanne Collins", genre="Young Adult, Science Fiction", publisher="Scholastic Corporation", year=2008)
        book8 = Book(title="Educated", book_id=0008.1, author="Tara Westover", genre="Memoir", publisher="Random House", year=2018)
        book9 = Book(title="The Fault in Our Stars", book_id=0009.2, author="John Green", genre="Young Adult, Contemporary", publisher="Dutton Books", year=2012)
        book10 = Book(title="The Kite Runner", book_id=0010.11, author="Khaled Hosseini", genre="Historical Fiction", publisher="Riverhead Books", year=2003)

        # Save instances to database
        # book2.save()
        book = [book1, book2, book3, book4, book5, book6, book7, book8, book9, book10]
        for books in book:
            books.save()

        self.stdout.write(self.style.SUCCESS(
            'Successfully created books.'))
        print(f"Book record count: {Book.objects.count()}")

    def create_librarian(self):
        # Create Librarian instances
        librarian1 = Librarian(name="Mary Adams", birthdate="1987-05-22",
                           gender="Female", duty_day="Monday")
        librarian2 = Librarian(name="James Johnson", birthdate="1984-08-06",
                           gender="Male", duty_day="Tuesday")
        librarian3 = Librarian(name="John Mayer", birthdate="1983-06-01",
                           gender="Male", duty_day="Wednesday")
        librarian4 = Librarian(name="Ariana Grande", birthdate="2007-12-24",
                           gender="Female", duty_day="Thursday")
        librarian5 = Librarian(name="Dwayne Johnson", birthdate="2007-07-21",
                           gender="Male", duty_day="Friday")
        librarian6 = Librarian(name="Steven Clarkson", birthdate="1974-11-02",
                           gender="Male", duty_day="Saturday")
        librarian7 = Librarian(name="Roxanne Washington", birthdate="2005-07-02",
                           gender="Female", duty_day="Sunday")

        librarians = [librarian1, librarian2, librarian3, librarian4, librarian5,
                    librarian6, librarian7]

        for lib in librarians:
            lib.save()
        self.stdout.write(self.style.SUCCESS(
            'Successfully created Librarians. '))
        print(f"Librarian record count: {Librarian.objects.count()}")