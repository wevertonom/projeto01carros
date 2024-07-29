from django.shortcuts import render, redirect
#
from cars.models import Car
from cars.form import CarModelForm
from django.views import View
from django.urls import reverse_lazy
#
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#
from django.views.generic import ListView, CreateView, UpdateView, DeleteView , DetailView

# Create your views here.
# def cars(request): #
#     cars = Car.objects.all().order_by('Model')
#     # carsF = Car.objects.filter(Model__contains='F').order_by('-Model')
#     # carsF2 = Car.objects.filter(Brand__Name='Fiate')
#     #
#     search = request.GET.get('search')
#     if search is not None:
#         cars = cars.filter( Model__icontains = search )
#     # else:
#     #     search = ''
#     #
#     return render(request, 'cars.html', {
#         'cars': cars ,
#         # 'carsF':carsF,
#         # 'carsF2':carsF2,
#     } )
# def new_cars(request):
#     if request.method == 'POST':
#         NewCarsForm = CarModelForm(request.POST, request.FILES)
#         if NewCarsForm.is_valid():
#             NewCarsForm.save()
#             return redirect('cars_list')
#     if request.method == 'GET':
#         NewCarsForm = CarModelForm()
#     #
#     return render(request, 'new_cars.html', {'NewCarsForm': NewCarsForm } )
# class CarsView(View):
#     def get(self, request):
#         cars = Car.objects.all().order_by('Model')
#         search = request.GET.get('search')
#         if search is not None:
#             cars = cars.filter( Model__icontains = search )
#         return render(request, 'cars.html', { 'cars': cars , })
# class NewCarView(View):
#     def get(self, request):
#         NewCarsForm = CarModelForm()
#         return render(request, 'new_cars.html', {'form': NewCarsForm})
#     def post(self, request):
#         NewCarsForm = CarModelForm(request.POST, request.FILES)
#         if NewCarsForm.is_valid():
#             NewCarsForm.save()
#             return redirect('cars_list')
class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    ordering = ['Model']
    def get_queryset(self):
        queryset = super().get_queryset().order_by('Model')
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(Model__icontains=search)
        return queryset

@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_cars.html'
    success_url = '/cars'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('cars_detail', kwargs={'pk': self.object.pk})
@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    success_url = '/cars'
    template_name = 'car_delete.html'
