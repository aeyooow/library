from django.contrib import admin
from .models import Book, User, Librarian, BorrowBook, ReturnBook

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "book_id", "author", "genre", "publisher", "year")
    search_fields = ("book_id",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user_id", "last_name", "first_name", "birthdate",
                    "gender", "email", "contact_number")
    search_fields = ("user_id",)


@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate", "gender", "duty_day")
    search_fields = ("name",)


@admin.register(BorrowBook)
class BorrowBookAdmin(admin.ModelAdmin):
    list_display = ("librarian", "book", "user", "borrow_date")
    search_fields = ("borrow_date",)

@admin.register(ReturnBook)
class ReturnBookAdmin(admin.ModelAdmin):
    list_display = ("borrowed", "return_date")
    search_fields = ("return_date",)