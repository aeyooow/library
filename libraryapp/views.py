from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from libraryapp.models import Book, User, Librarian, BorrowBook, ReturnBook
from libraryapp.forms import UserForm, LibrarianForm, BorrowBookForm, ReturnBookForm, BookForm
# Create your views here.


from django.urls import reverse_lazy
import json


class HomePageView(ListView):
    model = Book
    context_object_name = 'home'
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BookListView(ListView):
    model = Book
    context_object_name = 'book'
    template_name = "book.html"
    # Update this with the correct path to your JSON file
    json_file_path = 'C:\\Users\\AsusTUF\\librarysite\\data\\book_data.json'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_data = self.get_book_data()
        context['book_data'] = book_data
        return context

    def get_book_data(self):
        with open(self.json_file_path, 'r') as file:
            data = json.load(file)
            return data.get('book', [])


class LibrarianList(ListView):
    model = Librarian
    context_object_name = 'librarian'
    template_name = 'librarian.html'
    json_file_path = 'C:\\Users\\AsusTUF\\librarysite\\data\\librarian_data.json'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        librarian_data = self.get_librarian_data()
        context['librarian_data'] = librarian_data
        return context

    def get_librarian_data(self):
        with open(self.json_file_path, 'r') as file:
            data = json.load(file)
            return data.get('librarian', [])



class BorrowBookList(ListView):
    model = BorrowBook
    context_object_name = 'borrowbook'
    template_name = 'borrowbook.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(BorrowBookList, self).get_queryset(*args, **kwargs)
        return qs


class BorrowBookCreateView(CreateView):
    model = BorrowBook
    form_class = BorrowBookForm
    template_name = 'borrowbook_add.html'
    success_url = reverse_lazy('borrowbook-list')


class BorrowBookUpdateView(UpdateView):
    model = BorrowBook
    form_class =BorrowBookForm
    template_name = 'borrowbook_edit.html'
    success_url = reverse_lazy('borrowbook-list')


class BorrowBookDeleteView(DeleteView):
    model = BorrowBook
    template_name = 'borrowbook_del.html'
    success_url = reverse_lazy('borrowbook-list')


class ReturnBookList(ListView):
    model = ReturnBook
    context_object_name = 'returnbook'
    template_name = 'returnbook.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(ReturnBookList, self).get_queryset(*args, **kwargs)
        return qs


class ReturnBookCreateView(CreateView):
    model = ReturnBook
    form_class = ReturnBookForm
    template_name = 'returnbook_add.html'
    success_url = reverse_lazy('returnbook-list')


class ReturnBookUpdateView(UpdateView):
    model = ReturnBook
    form_class = ReturnBookForm
    template_name = 'returnbook_edit.html'
    success_url = reverse_lazy('returnbook-list')


class ReturnBookDeleteView(DeleteView):
    model = ReturnBook
    template_name = 'returnbook_del.html'
    success_url = reverse_lazy('returnbook-list')

class UserList(ListView):
    model = User
    context_object_name = 'user'
    template_name = 'user.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(UserList, self).get_queryset(*args, **kwargs)
        return qs



class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'user_add.html'
    success_url = reverse_lazy('user-list')


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user_edit.html'
    success_url = reverse_lazy('user-list')


class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_del.html'
    success_url = reverse_lazy('user-list')