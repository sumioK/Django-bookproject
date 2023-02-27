from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import SampleModel, Book
# Create your views here.
def sample(request):
    object_lsit = SampleModel.objects.all()
    return render(request,'sample.html',{'objects': object_lsit})

class ListBookview(ListView):
    template_name = 'book_list.html'
    model = Book

class DetailBookView(DetailView):
    template_name = 'book/book_detail.html'
    model = Book

class CreateBookView(CreateView):
    template_name = 'book/book_create.html'
    model = Book
    fields = ('title', 'text', 'category')
    success_url = reverse_lazy('list-book')

class DeleteBookView(DeleteView):
    template_name = 'book/delete.html'
    model = Book
    success_url = reverse_lazy('list-book')