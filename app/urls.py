"""
URL configuration for app project.

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
from django.urls import path
#
from django.conf.urls.static import static
from django.conf import settings
#
# from django.http import HttpResponse
from django.shortcuts import render
#
# from cars.views import cars , new_cars , CarListView , NewCarView
from cars.views import  CarListView , NewCarCreateView , CarDetailView , CarUpdateView , CarDeleteView
from accounts.views import register_views, login_views, logout_views

def home(request): #
    return render(request, 'base.html', {})
    # return HttpResponse("Hello World")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), #
    # path('cars', cars ,name='cars_list' ), #
    # path('cars', CarsView.as_view() ,name='cars_list' ), #
    path('cars', CarListView.as_view() ,name='cars_list' ), #
    # path('new_cars', new_cars ,name='new_cars' ), #
    # path('new_cars', NewCarView.as_view() ,name='new_cars' ), #
    path('new_cars', NewCarCreateView.as_view() ,name='new_cars' ), #
    path('cars/<int:pk>/', CarDetailView.as_view() ,name='cars_detail' ), #
    path('cars/<int:pk>/update', CarUpdateView.as_view() ,name='cars_update' ), #
    path('cars/<int:pk>/delete', CarDeleteView.as_view() ,name='cars_delete' ), #
    path('register', register_views ,name='register' ), #
    path('login', login_views ,name='login' ), #
    path('logout', logout_views ,name='logout' ), #
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
