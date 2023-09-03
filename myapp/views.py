from django.shortcuts import render, HttpResponse
from .models import Student

# Create your views here.
def index(request):
    list = Student.objects.all()
    return render(request, "index.html", {'list':list})