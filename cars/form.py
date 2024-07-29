from django import forms
from cars.models import Brand, Car

# class CarForm(forms.Form):
#     Model = forms.CharField( label='Model', max_length=100 )
#     Brand = forms.ModelChoiceField( queryset=Brand.objects.all() )
#     FactoryYear = forms.IntegerField( label='Factory Year' )
#     ModelYear = forms.IntegerField( label='Model Year' )
#     Place = forms.CharField( label='Place', max_length=10 )
#     Value = forms.FloatField( label='Value' )
#     Photo = forms.ImageField( label='Photo' )
#
#     def save(self):
#         car = Car(
#             Model=self.cleaned_data['Model'],
#             Brand=self.cleaned_data['Brand'],
#             FactoryYear=self.cleaned_data['FactoryYear'],
#             ModelYear=self.cleaned_data['ModelYear'],
#             Place=self.cleaned_data['Place'],
#             Value=self.cleaned_data['Value'],
#             Photo=self.cleaned_data['Photo'],
#         )
#         car.save()
#         return car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
    def clean_Value(self):
        value = self.cleaned_data['Value']
        if value < 20000:
            self.add_error('Value','Valor minimo e de 20 000')
        return value
    def clean_FactoryYear(self):
        value = self.cleaned_data['FactoryYear']
        if value < 1975 :
            self.add_error('FactoryYear','Valor minimo e de 1975')
        return value
    def clean_ModelYear(self):
        value = self.cleaned_data['ModelYear']
        if value <= 1975 :
            self.add_error('ModelYear','Valor minimo e de 1975')
        return value
    # def clean_Photo(self):
    #     value = self.cleaned_data['Photo']
    #     if not value:
    #         self.add_error('Photo','Precisa de Photo')
    #         return value
