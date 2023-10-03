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


    id_stdf = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa STDF"}),label='STDF')
    awb = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa AWB"}),label='AWB')
    hawb = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa HAWB"}),label='HAWB')
    num_manifiesto = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Número de Manifiesto"}),label='Número Manifiesto')
    corr_interno = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Correlativo Interno"}),label='Correlativo Interno')
    pcs = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa Cantidad de Piezas"}),label='Piezas')
    peso = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa el Peso"}),label='Peso')

    f_control = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control", 'type': 'datetime-local'}), required=False, label='Fecha de Control')
    f_manifiesto = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control", 'type': 'datetime-local'}), required=False, label='Fecha de Manifiesto')
    f_recepcion = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control", 'type': 'datetime-local'}), required=False, label='Fecha de Recepción')
    f_stdf = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control", 'type': 'date'}), required=False, label='Fecha del STDF')

    fob = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa el valor del FOB"}),label='FOB')
    flete = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa el valor del Flete"}),label='Flete')
    seguro = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa el valor del Seguro"}),label='Seguro')
    sum_cif = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa el CIF (Podría calcularse auto)"}),label='Suma CIF')
    observaciones = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder": "Ingresa la observación"}),label='Observaciones')

    # id_bodega = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-select m-2"}), label='Bodega (FK)')
    # id_origen = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-select m-2"}), label='Origen (FK)')



    class Meta:
        model = Comat
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ComatForm, self).__init__(*args, **kwargs)
        
        self.fields['id_bodega'].queryset = Bodega.objects.all()
        # self.fields['id_bodega'].widget = forms.Select(attrs={'class': 'form-select'})

        self.fields['id_origen'].queryset = Origen.objects.all()

        # self.fields['id_origen'].widget = forms.Select(attrs={'class': 'form-select'})



class IncomingForm(ModelForm):

    id_sn_batch = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Serial Number"}),label='Serial Number')
    part_number = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Part Number"}),label='Part Number')
    f_incoming = forms.DateField(widget=forms.DateTimeInput(attrs={"class":"form-control", 'type': 'date'}), required=False, label='Fecha Ingreso Incoming')
    po = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa AWB"}),label='Producto Order')
    qty = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa Cantidad"}),label='Quantity')
    u_purchase_cost = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa Unit Purchase Cost"}),label='Unit Purchase Cost')
    total_u_purchase_cost = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa Total Unit Purchase Cost"}),label='Total Unit Purchase Cost')
    f_vencimiento = forms.DateField(widget=forms.DateTimeInput(attrs={"class":"form-control", 'type': 'date'}), required=False, label='Fecha Vencimiento')
    saldo = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa Stock"}),label='Saldo')
    descripcion = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder": "Ingresa Descripción"}),label='Descripción')
    observaciones = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder": "Ingresa Observaciones"}),label='Observaciones')

    
    class Meta:
        model = Incoming
        fields = '__all__'

class ConsumosForm(ModelForm):

    f_transaccion = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'type': 'date'}))

    class Meta:
        model = Consumos
        fields = '__all__'