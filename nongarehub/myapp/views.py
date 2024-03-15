from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
        return render(request, 'dashboard.html',)
def home(request):
        return render(request, 'home.html',)
def blog(request):
        return render(request, 'blog.html',)
def about(request):
        return render(request, 'about.html',)
def contact(request):
        return render(request, 'contact.html',)

