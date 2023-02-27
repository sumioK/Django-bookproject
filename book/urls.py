from django.urls import path
from .views import sample, ListBookview, DetailBookView, CreateBookView, DeleteBookView

urlpatterns = [
    path("sample",sample,name='sample'),
    path("book/", ListBookview.as_view(), name='list-book'),
    path("book/detail/<int:pk>", DetailBookView.as_view(),name='detail'),
    path("book/create/", CreateBookView.as_view(), name='create'),
    path("book/delete/<int:pk>", DeleteBookView.as_view(), name='delete'),
]
