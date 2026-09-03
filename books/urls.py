from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='home'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('subscribe/', views.subscribe, name='subscribe'), path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]