"""
URL configuration for librarysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from libraryapp.views import *
from libraryapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('user_list', UserList.as_view(), name='user-list'),
    path('user_list/add', UserCreateView.as_view(), name='user-add'),
    path('user_list/<pk>', UserUpdateView.as_view(), name='user-update'),
    path('user_list/<pk>/delete', UserDeleteView.as_view(), name='user-delete'),
    path('librarian_list', LibrarianList.as_view(), name='librarian-list'),
    path('borrowbook_list', BorrowBookList.as_view(), name='borrowbook-list'),
    path('borrowbook_list/add', BorrowBookCreateView.as_view(), name='borrowbook-add'),
    path('borrowbook_list/<pk>', BorrowBookUpdateView.as_view(), name='borrowbook-update'),
    path('borrowbook_list/<pk>/delete', BorrowBookDeleteView.as_view(), name='borrowbook-delete'),
    path('returnbook_list', ReturnBookList.as_view(), name='returnbook-list'),
    path('returnbook_list/add', ReturnBookCreateView.as_view(), name='returnbook-add'),
    path('returnbook_list/<pk>', ReturnBookUpdateView.as_view(), name='returnbook-update'),
    path('returnbook_list/<pk>/delete', ReturnBookDeleteView.as_view(), name='returnbook-delete'),
    path('book_list', BookListView.as_view(), name='book-list'),
]
