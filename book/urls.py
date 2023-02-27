from django.urls import path
from .views import sample, Listview

urlpatterns = [
    path("sample",sample,name='sample'),
    path("list", Listview.as_view()),
    
]
