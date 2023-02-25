from django.shortcuts import render
from .models import SampleModel
# Create your views here.
def sample(request):
    object_lsit = SampleModel.objects.all()
    return render(request,'sample.html',{'objects': object_lsit})