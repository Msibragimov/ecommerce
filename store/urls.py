from django.urls import path

from . import views

urlpatterns = [
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('category/', views.category_list, name="category_list"),
	path('<int:pk>/product/', views.product_detail, name="product"),
	path('<slug:slug>/category/', views.category_detail, name="category_detail"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
]