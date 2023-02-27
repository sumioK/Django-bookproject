from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import SampleModel, Book
# Create your views here.
def sample(request):
    object_lsit = SampleModel.objects.all()
    return render(request,'sample.html',{'objects': object_lsit})

class Listview(ListView):
    template_name = 'book_list.html'
    model = Book

class DetailBookView(DetailView):
    template_name = 'book/book_detail.html'
    model = Book