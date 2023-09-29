from django.forms import ModelForm
from .models import *
from django import forms

class CategoriaForm(ModelForm):

    class Meta:
        model = Categotia_incoming
        fields = '__all__'

class EstadoForm(ModelForm):

    class Meta:
        model = Estado
        fields = '__all__'

class UbicacionForm(ModelForm):

    class Meta:
        model = Ubicacion
        fields = '__all__'

class UserForm(ModelForm):
    
    class Meta:
        model = User
        fields = '__all__'

class UomForm(ModelForm):
    
    class Meta:
        model = Uom
        fields = '__all__'

class OwnerForm(ModelForm):

    class Meta:
        model = Owner
        fields = '__all__'

class FichaForm(ModelForm):

    class Meta:
        model = Ficha
        fields = '__all__'

class ConditionForm(ModelForm):

    class Meta:
        model = Condicion
        fields = '__all__'

class BodegaForm(ModelForm):

    class Meta:
        model = Bodega
        fields = '__all__'

class OrigenForm(ModelForm):

    class Meta:
        model = Origen
        fields = '__all__'

class ComatForm(ModelForm):

    f_control = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    f_manifiesto = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    f_recepcion = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    f_stdf = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'type': 'date'}))

    class Meta:
        model = Comat
        fields = '__all__'

class IncomingForm(ModelForm):

    f_incoming = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'type': 'date'}))
    f_vencimiento = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'type': 'date'}))

    class Meta:
        model = Incoming
        fields = '__all__'

class ConsumosForm(ModelForm):

    f_transaccion = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'type': 'date'}))

    class Meta:
        model = Consumos
        fields = '__all__'