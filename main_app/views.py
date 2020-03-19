from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Shoe, Store
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
    stores_shoe_isnt_sold_in = Store.objects.exclude(id__in = shoe.stores.all().values_list('id'))
    lastworn_form = LastWornForm()
    return render(request, 'shoes/detail.html', {
         'shoe': shoe,
         'lastworn_form': lastworn_form,
         'stores': stores_shoe_isnt_sold_in,
        })

def add_lastworn(request, shoe_id):
    form = LastWornForm(request.POST)
    if form.is_valid():
        new_lastworn = form.save(commit=False)
        new_lastworn.shoe_id = shoe_id
        new_lastworn.save()
    return redirect('detail', shoe_id=shoe_id)

def assoc_store(request, shoe_id, store_id):
  Shoe.objects.get(id=shoe_id).stores.add(store_id)
  return redirect('detail', shoe_id=shoe_id)

def unassoc_store(request, shoe_id, store_id):
  Shoe.objects.get(id=shoe_id).store.remove(store_id)
  return redirect('detail', shoe_id=shoe_id)


class StoreList(ListView):
  model = Store

class StoreDetail(DetailView):
  model = Store

class StoreCreate(CreateView):
  model = Store
  fields = '__all__'

class StoreUpdate(UpdateView):
  model = Store
  fields = ['name', 'address']

class StoreDelete(DeleteView):
  model = Store
  success_url = '/stores/'