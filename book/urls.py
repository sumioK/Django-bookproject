from django.urls import path
from .views import sample, Listview, DetailBookView, CreateBookView

urlpatterns = [
    path("sample",sample,name='sample'),
    path("book/", Listview.as_view(), name='list-book'),
    path("book/detail/<int:pk>", DetailBookView.as_view(),name='detail'),
    path("book/create/", CreateBookView.as_view(), name='create')
]
