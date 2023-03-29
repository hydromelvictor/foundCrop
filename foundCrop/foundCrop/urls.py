"""foundCrop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin
from exchange.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home, name='home'),
    path('home', home, name='home'),
    path('category/<str:name>', category, name='category'),
    
    path('dashboard', dashboard, name='dashboard'),
    path('profile', profile, name='profile'),
    path('logout',  output, name='logout'),

    path('product/view',  productView, name='productView'),
    path('product/add',  productAdd, name='productAdd'),
    path('product/del/<int:prd_id>',  productDel, name='productDel'),
    path('product/update/<int:prd_id>',  productUpdate, name='productUpdate'),

    path('cmd/view',  cmdView, name='cmdView'),
    path('add_to_cart/<int:prd_id>',  add_to_cart, name='add_to_cart'),
    #path('cmd/del/<int:cmd_id>',  cmdDel, name='cmdDel'),
    #path('del_to_cart/<int:detail_id>',  del_to_cart, name='del_to_cart'),
    #path('update_to_cart/<int:details_id>',  Update_to_cart, name='update_to_cart'),
    #path('buy',  buy, name='buy'),

    path('signin',  signin, name='signin'),
    path('signup',  signup, name='signup'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
