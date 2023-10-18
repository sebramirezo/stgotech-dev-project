#from django.contrib.admin.widgets import AutocompleteSelect
#from django.contrib import admin
from django.forms import ModelForm, ValidationError
from .models import *
from django import forms
from django.contrib.auth.models import Permission
from django.contrib.admin.widgets import AdminDateWidget

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
    stdf_pk = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa STDF"}),label='STDF')
    awb = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa AWB"}),label='AWB')
    hawb = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa HAWB"}),label='HAWB')
    num_manifiesto = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Número de Manifiesto"}),label='Número Manifiesto')
    corr_interno = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Correlativo Interno"}),label='Correlativo Interno')
    pcs = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa Cantidad de Piezas"}),label='Piezas')
    peso = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa el Peso"}),label='Peso')

    f_control = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control", 'type': 'datetime-local', 'id':'id_f_control'}), required=False, label='Fecha de Control')
    # f_control = forms.DateTimeField(widget=AdminDateWidget())
    f_manifiesto = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control", 'type': 'datetime-local'}), required=False, label='Fecha de Manifiesto')
    f_recepcion = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control", 'type': 'datetime-local'}), required=False, label='Fecha de Recepción')
    f_stdf = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control", 'type': 'date'}), required=False, label='Fecha del STDF')

    fob = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa el valor del FOB Formato - Utilice coma para separar  00,00"}),label='FOB')
    flete = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa el valor del Flete - Utilice coma para separar  00,00"}),label='Flete')
    seguro = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa el valor del Seguro - Utilice coma para separar  00,00"}),label='Seguro')
    observaciones = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa la observación"}),label='Observaciones' , required=False)
    prioridad = forms.ChoiceField(choices=Prioridad,widget=forms.Select(attrs={"class": "form-control", "placeholder": "Ingresa la Prioridad"}),label='Prioridad',required=True)
    
    bodega_fk = forms.ModelChoiceField(queryset=Bodega.objects.all(), widget=forms.Select(attrs={"class": "form-control","placeholder": "Ingresa la Bodega"}), label='Bodega')
    origen_fk = forms.ModelChoiceField(queryset=Origen.objects.all(), widget=forms.Select(attrs={"class": "form-control","placeholder": "Ingresa el Origen"}), label='Origen')
    class Meta:
        model = Comat
        fields = [ 
        'stdf_pk',
        'awb',
        'hawb',
        'num_manifiesto',
        'corr_interno',
        'pcs',
        'peso',
        'f_control',
        'f_manifiesto',
        'f_recepcion',
        'f_stdf',
        'fob',
        'flete',
        'seguro',
        'bodega_fk',
        'origen_fk',
        'observaciones',
        'prioridad',
        ]
        #widget = AutocompleteSelect(Comat._meta.get_field('id_bodega').remote_field,admin.site,attrs={'placeholder': 'seleccionar...'},)


        
   



class IncomingForm(ModelForm):

    sn_batch_pk = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Serial Number"}),label='Serial Number')
    part_number = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Part Number"}),label='Part Number')
    f_incoming = forms.DateField(widget=forms.DateTimeInput(attrs={"class":"form-control", 'type': 'date'}), required=False, label='Fecha Ingreso Incoming')
    po = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Product Order"}),label='Orden del Repuesto')
    qty = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa Cantidad"}),label='Quantity')
    u_purchase_cost = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa Unit Purchase Cost"}),label='Unit Purchase Cost')
    f_vencimiento = forms.DateField(widget=forms.DateTimeInput(attrs={"class":"form-control", 'type': 'date'}), required=False, label='Fecha Vencimiento')
    descripcion = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Descripción"}),label='Descripción')
    observaciones = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Observaciones"}),label='Observaciones',required=False)
    categoria_fk = forms.ModelChoiceField(queryset=Categotia_incoming.objects.all(), widget=forms.Select(attrs={"class": "form-control","placeholder": "Ingresa la Categoria SN o BN"}), label='Categoria')
    clasificacion_fk = forms.ModelChoiceField(queryset=Clasificacion.objects.all(), widget=forms.Select(attrs={"class": "form-control","placeholder": "Ingresa la Clasificación"}), label='Clasificación')
    ubicacion_fk = forms.ModelChoiceField(queryset=Ubicacion.objects.all(), widget=forms.Select(attrs={"class": "form-control","placeholder": "Ingresa la Ubicacion"}), label='Ubicación')
    uom_fk = forms.ModelChoiceField(queryset=Uom.objects.all(), widget=forms.Select(attrs={"class": "form-control","placeholder": "Ingreso Uom"}), label='Uom')
    owner_fk = forms.ModelChoiceField(queryset=Owner.objects.all(), widget=forms.Select(attrs={"class": "form-control","placeholder": "Ingreso Owner"}), label='Owner')
    condicion_fk = forms.ModelChoiceField(queryset=Condicion.objects.all(), widget=forms.Select(attrs={"class": "form-control","placeholder": "Ingresa Condicion"}), label='Condicion')
    ficha_fk = forms.ModelChoiceField(queryset=Ficha.objects.all(), widget=forms.Select(attrs={"class": "form-control","placeholder": "Ingreso N° Ficha"}), label='N° Ficha')

    #stdf_fk = forms.CharField(widget=forms.Select(attrs={"class": "form-control","placeholder": "Ingresa STDF", "id":"id_stdf_fk"}), label='STDF')
    stdf_fk = forms.ModelChoiceField(queryset=Comat.objects.all(), widget=forms.Select(attrs={"class": "form-control","placeholder": "Ingresa STDF", "id":"id_stdf_fk"}), label='STDF')

    class Meta:
        model = Incoming
        fields = [
        'sn_batch_pk',
        'categoria_fk',
        'part_number',
        'f_incoming',
        'po',
        'qty',
        'u_purchase_cost',
        'f_vencimiento',
        'descripcion',
        'clasificacion_fk', 
        'ubicacion_fk', 
        'uom_fk' , 
        'owner_fk' , 
        'condicion_fk', 
        'ficha_fk' , 
        'stdf_fk',
        'observaciones',    
    ]
    
class ConsumosForm(ModelForm):

    orden_consumo = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Orden de Consumo"}),label='Orden de Consumo')
    qty_extraida = forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Cantidad Extraida"}),label='Cantidad Extraida')
    matricula_aeronave = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Matricula"}),label='Matricula Aeronave')
    observaciones = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Observaciones"}),label='Observaciones',required=False)
    f_transaccion = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control",'type': 'date'}), required=False, label='Fecha de Transacción')
    incoming_fk = forms.ModelChoiceField(queryset=Incoming.objects.all(), widget=forms.Select(attrs={"class": "form-control","placeholder": "Ingresa Serial Number o Batch Number"}), label='Serial Number o Batch Number')
    
    # incoming_id = forms.CharField(widget=forms.ChoiceField(attrs={"class":"form-control"}),label='Serial Number')
    # id_estado = forms.CharField(widget=forms.ChoiceField(attrs={"class":"form-control"}),label='Estado')
    class Meta:
        model = Consumos
        fields = [
        'orden_consumo',
        'qty_extraida',
        'matricula_aeronave',
        'f_transaccion',
        'incoming_fk',
        'observaciones',
        
        
        ]