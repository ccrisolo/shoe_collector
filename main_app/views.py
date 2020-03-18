from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Shoe
from .forms import LastWornForm

#CBV
class ShoeList(ListView):
    model = Shoe
    template_name = 'shoes/index.html'

class ShoeCreate(CreateView):
    model = Shoe
    fields = '__all__'
    success_url = '/shoes/'

class ShoeUpdate(UpdateView):
    model = Shoe
    fields = '__all__'

class ShoeDelete(DeleteView):
    model = Shoe
    success_url = '/shoes/'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render (request, 'about.html')

def shoes_index(request):
    shoes = Shoe.objects.all()
    return render(request, 'shoes/index.html', { 'shoes': shoes })

def shoes_detail(request, shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)
    lastworn_form = LastWornForm()
    return render(request, 'shoes/detail.html', {
         'shoe': shoe,
         'lastworn_form': lastworn_form
        })

def add_lastworn(request, shoe_id):
    form = LastWornForm(request.POST)
    if form.is_valid():
        new_lastworn = form.save(commit=False)
        new_lastworn.shoe_id = shoe_id
        new_lastworn.save()
    return redirect('detail', shoe_id=shoe_id)