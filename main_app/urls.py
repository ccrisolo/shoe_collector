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
    path('shoes/<int:shoe_id>/add_photo', views.add_photo, name='add_photo'),
    path('shoes/<int:shoe_id>/assoc_store/<int:store_id>/', views.assoc_store, name='assoc_store'),
    path('shoes/<int:shoe_id>/unassoc_store/<int:store_id>/', views.unassoc_store, name='unassoc_store'),
    path('stores/', views.StoreList.as_view(), name='stores_index'),
    path('stores/<int:pk>/', views.StoreDetail.as_view(), name='stores_detail'),
    path('stores/create/', views.StoreCreate.as_view(), name='stores_create'),
    path('stores/<int:pk>/update/', views.StoreUpdate.as_view(), name='stores_update'),
    path('stores/<int:pk>/delete/', views.StoreDelete.as_view(), name='stores_delete'),
]