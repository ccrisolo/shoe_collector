from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Shoe, Store, Photo
from .forms import LastWornForm
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'shoecollector'


#CBV
class ShoeList(ListView):
    model = Shoe
    template_name = 'shoes/index.html'

class ShoeCreate(LoginRequiredMixin, CreateView):
    model = Shoe
    fields = ['model', 'brand', 'color', 'price']
    success_url = '/shoes/'

    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class ShoeUpdate(LoginRequiredMixin, UpdateView):
    model = Shoe
    fields = ['model', 'brand', 'color', 'price']

class ShoeDelete(LoginRequiredMixin, DeleteView):
    model = Shoe
    success_url = '/shoes/'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render (request, 'about.html')

@login_required
def shoes_index(request):
    shoes = Shoe.objects.filter(user=request.user)
    return render(request, 'shoes/index.html', { 'shoes': shoes })

@login_required
def shoes_detail(request, shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)
    stores_shoe_isnt_sold_in = Store.objects.exclude(id__in = shoe.stores.all().values_list('id'))
    lastworn_form = LastWornForm()
    return render(request, 'shoes/detail.html', {
         'shoe': shoe,
         'lastworn_form': lastworn_form,
         'stores': stores_shoe_isnt_sold_in,
        })

@login_required
def add_lastworn(request, shoe_id):
    form = LastWornForm(request.POST)
    if form.is_valid():
        new_lastworn = form.save(commit=False)
        new_lastworn.shoe_id = shoe_id
        new_lastworn.save()
    return redirect('detail', shoe_id=shoe_id)

@login_required
def add_photo(request, shoe_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, shoe_id=shoe_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', shoe_id=shoe_id)

@login_required
def assoc_store(request, shoe_id, store_id):
  Shoe.objects.get(id=shoe_id).stores.add(store_id)
  return redirect('detail', shoe_id=shoe_id)

@login_required
def unassoc_store(request, shoe_id, store_id):
  Shoe.objects.get(id=shoe_id).stores.remove(store_id)
  return redirect('detail', shoe_id=shoe_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class StoreList(LoginRequiredMixin, ListView):
  model = Store

class StoreDetail(LoginRequiredMixin, DetailView):
  model = Store

class StoreCreate(LoginRequiredMixin, CreateView):
  model = Store
  fields = '__all__'

class StoreUpdate(LoginRequiredMixin, UpdateView):
  model = Store
  fields = ['name', 'address']

class StoreDelete(LoginRequiredMixin, DeleteView):
  model = Store
  success_url = '/stores/'