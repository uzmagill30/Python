"""
URL configuration for restaurantsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from customer.views import Index, Menu, login_view, register, LogoutView, product_list, user_orders, add_to_cart, remove_from_cart, view_cart, view_order
from store.views import Revenue_Products, Revenue_Categories
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('menu/', Menu.as_view(), name='menu'),
    
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView, name='logout'),
    path('order/', product_list, name='order'),
    
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('viewOrder/', view_order, name='view_order'),
    path('userOrders/', user_orders, name='user_orders'),
    path('revenue_products/', Revenue_Products.as_view(), name='revenue_products'),
    path('revenue_categories/', Revenue_Categories.as_view(), name='revenue_categories'),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
