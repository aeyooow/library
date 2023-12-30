from django.forms import ModelForm
from django import forms
from .models import Book, User, Librarian, BorrowBook, ReturnBook


class UserForm(ModelForm):
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = "__all__"

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class LibrarianForm(ModelForm):
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Librarian
        fields = "__all__"

class BorrowBookForm(ModelForm):
    borrow_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = BorrowBook
        fields = "__all__"

class ReturnBookForm(ModelForm):
    return_date= forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = ReturnBook
        fields = "__all__"