from django.urls import path
from .views import sample, Listview, DetailBookView

urlpatterns = [
    path("sample",sample,name='sample'),
    path("book/", Listview.as_view()),
    path("book/detail/<int:pk>", DetailBookView.as_view()),
]
