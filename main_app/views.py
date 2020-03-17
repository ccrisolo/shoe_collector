from django.shortcuts import render
from .models import Shoe
from django.http import HttpResponse



# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello SneakerHeads</h1>')

def about(request):
    return render (request, 'about.html')

def shoes_index(request):
    shoes = Shoe.objects.all()
    return render(request, 'shoes/index.html', { 'shoes': shoes })

def shoes_detail(request, shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)
    return render(request, 'shoes/details.html', { 'shoe': shoe })