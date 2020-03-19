from django.urls import path
from . import views
# from shoes.views import ShoeList

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shoes/', views.shoes_index, name='index'),
    path('shoes/<int:shoe_id>/', views.shoes_detail, name='detail'),
    # path('shoes/', ShoeList.as_view(), name='shoes_index'),
    path('shoes/create/', views.ShoeCreate.as_view(), name='shoes_create'),
    path('shoes/<int:pk>/update/', views.ShoeUpdate.as_view(), name='shoes_update'),
    path('shoes/<int:pk>/delete/', views.ShoeDelete.as_view(), name='shoes_delete'),
    path('shoes/<int:shoe_id>/add_lastworn/', views.add_lastworn, name='add_lastworn'),
    # path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('stores/<int:pk>/', views.StoreDetail.as_view(), name='stores_detail'),
    # path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    # path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    # path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]