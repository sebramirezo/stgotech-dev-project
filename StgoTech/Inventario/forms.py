from django.forms import ModelForm, ValidationError
from .models import *
from django import forms
from django.contrib.auth.models import Permission
from django.contrib.admin.widgets import AdminDateWidget



class ItemForm(ModelForm):
    item1 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}), label='1) Producto conforme a lo indicado en la lista de Embarque (Packing List)', required=False)
    item2 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}), label='2) Factura del Proveedor conforme a la orden de compra o solicitud de trabajo (Invoice)', required=False)
    item3 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='3) Cartilla/Orden de Trabajo, Cartilla de prueba, Si corresponde, del taller que repara', required=False)
    item4 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='4) Producto sin daños visibles (Inspeccion Visual)', required=False)
    item5 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='5) Producto protegido en embalaje apropiado', required=False)
    item6 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='6) Placa de identificacion del componente', required=False)
    item7 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='7) Documentacion Técnica completa requerida por reglamentacion (Trazabilidad)', required=False)
    item8 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='8) Formulario FAA 8130-3', required=False)
    item9 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='9) Formulario EASA Form One o JAA Form One o CAA Form One', required=False)
    item10 =  forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='10) Formulario DGAC Chile 8130-3', required=False)
    item11 =  forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='11) Formulario ANAC Argentina 8130-3', required=False)
    item12 =  forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='12) Placa o Etiqueta para Herramientas o equipos con calibracion', required=False)
    item13 =  forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='13) Certificado de Calibración en laboratorio reconocido por el estado local', required=False)
    n_item13  = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}),label='13.5) N° de Certificado de Calibración', required=False)
    item14 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='14) Materiales con vida limite (Verificacion de Shelf life data y MSDS)', required=False)
    item15 =  forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='15) Certificado de flamabilidad, si corresponde', required=False)
    n_item15 = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}),label='15.5) N° de Certificado de Flamabilidad', required=False)
    item16 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='16) Certificado de conformidad  y/o Analisis', required=False)
    n_item16 = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}),label='16.5) N° Certificado de conformidad y/o Analisis', required=False)
    item17 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='17) Numero de lote de fabricacion, si corresponde', required=False)
    n_item17 = forms.IntegerField(widget=forms.TextInput( attrs={"class": "form-control"}),label='17.5)Numero de lote de Fabricacion', required=False)
    item18 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='18) TSO / TSN (Si Aplica)', required=False)
    item_18tsn = forms.CharField(widget=forms.Select(choices=TSN, attrs={"class": "form-control"}),label='18.5) TSN/TSO/CSN/SCO', required=False)
    n_item18tsn = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),label='18.5.1) Especifique Numero de TSN/TSO/CSN/SCO', required=False)
    item19 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='19) Material Safety Data Sheet', required=False)
    item20 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='20) Material con restriccion bajo el programa ESD', required=False)
    item21 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='21) Material con restriccion de almacenamiento (Hielo Seco)', required=False)
    item22 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='22) Cartilla Mantencion CMA Autorizado', required=False)
    n_item22 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),label='22.5) N° de Catilla Mantencion CMA Autorizado', required=False)

    class Meta:
        model = Item
        fields = [
            'item1',
            'item2',
            'item3',
            'item4',
            'item5',
            'item6',
            'item7',
            'item8',
            'item9',
            'item10',
            'item11',
            'item12',
            'item13',
            'n_item13',
            'item14',
            'item15',
            'n_item15',
            'item16',
            'n_item16',
            'item17',
            'n_item17',
            'item18',
            'item_18tsn',
            'n_item18tsn',
            'item19',
            'item20',
            'item21',
            'item22',
            'n_item22',

        ]

class DetalleForm(ModelForm):
    modelo = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Modelo"}),label='Modelo', required=False)
    Proveedor = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Proveedor del Producto"}),label='Proveedor del Producto', required=False)
    taller_reparadora = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Taller/Cia. Reparadora"}),label='Taller/Cia. Reparadora', required=False)
    trabajo_solicitado = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Trabajo Solicitado"}),label='Trabajo Solicitado', required=False)
    propiedad = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Propiedad de"}),label='Propiedad de', required=False)
    check_periodica = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Check Periodica (Si Aplica)"}),label='Check Periodica (Si Aplica)', required=False)
    ro_n = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "RO N°"}),label='RO N°', required=False)
    wo_n = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "WO N°"}),label='WO N°', required=False)
    aceptado = forms.CharField(widget=forms.Select(choices=ACEPTADO, attrs={"class": "form-control"}),label='¿Aceptado?', required=False)
    licencia = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "N° Licencia"}),label='N° Licencia', required=False)
    estado_repuesto_fk = forms.ModelChoiceField(queryset=Estado_Repuesto.objects.all(), widget=forms.Select(attrs={"class": "form-control","placeholder": "Ingresa el Estado del Repuesto"}), label='Estado del Repuesto', required=False)
    incoming_fk = forms.ModelChoiceField(queryset=Incoming.objects.all(), widget=forms.Select(attrs={"class": "form-control","placeholder": "Ingresa el SN O BN"}), label='Serial Number o Batch Number')
    class Meta:
        model = Detalle_Incoming
        fields = [
            'incoming_fk',
            'modelo',
            'Proveedor',
            'taller_reparadora',
            'trabajo_solicitado',
            'propiedad',
            'check_periodica',
            'ro_n',
            'wo_n',
            'aceptado',
            'licencia',
            'estado_repuesto_fk',
        ]




# -- # -- # -- # -- # -- # -- ## -- # -- # -- # -- # -- # -- ## -- # -- # -- # -- # -- # -- #
class ComatForm(ModelForm):
    stdf_pk = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa STDF"}),label='STDF')
    awb = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa AWB"}),label='AWB')
    hawb = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa HAWB"}),label='HAWB')
    num_manifiesto = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Número de Manifiesto"}),label='Número Manifiesto')
    corr_interno = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Correlativo Interno"}),label='Correlativo Interno')
    pcs = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa Cantidad de Piezas"}),label='Piezas')
    peso = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa el Peso"}),label='Peso')

    f_control = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control", 'type': 'datetime-local', 'placeholder':'Selecciona la fecha', 'id':'id_f_control'}), required=False, label='Fecha de Control')
    # f_control = forms.DateTimeField(widget=AdminDateWidget())
    f_manifiesto = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control", 'type': 'datetime-local', 'placeholder':'Selecciona la fecha'}), required=False, label='Fecha de Manifiesto')
    f_recepcion = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control", 'type': 'datetime-local', 'placeholder':'Selecciona la fecha'}), required=False, label='Fecha de Recepción')
    f_stdf = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control", 'type': 'date', 'placeholder':'Selecciona la fecha'}), required=False, label='Fecha del STDF')

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

# -- # -- # -- # -- # -- # -- ## -- # -- # -- # -- # -- # -- ## -- # -- # -- # -- # -- # -- #
class IncomingForm(ModelForm):

    sn_batch_pk = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Serial Number"}),label='Serial Number')
    part_number = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Part Number"}),label='Part Number')
    f_incoming = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control", 'type': 'date', 'placeholder':'Selecciona la fecha'}), required=False, label='Fecha Ingreso Incoming')
    po = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Product Order"}),label='Orden del Repuesto')
    qty = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa Cantidad"}),label='Quantity')
    u_purchase_cost = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control", "placeholder": "Ingresa Unit Purchase Cost"}),label='Unit Purchase Cost')
    f_vencimiento = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control", 'type': 'date', "placeholder":'Seleccione fecha'}), required=False, label='Fecha Vencimiento')
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

# -- # -- # -- # -- # -- # -- ## -- # -- # -- # -- # -- # -- ## -- # -- # -- # -- # -- # -- #
class ConsumosForm(ModelForm):

    orden_consumo = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Orden de Consumo"}),label='Orden de Consumo')
    qty_extraida = forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Cantidad Extraida"}),label='Cantidad Extraida')
    matricula_aeronave = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Matricula"}),label='Matricula Aeronave')
    observaciones = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Observaciones"}),label='Observaciones',required=False)
    f_transaccion = forms.DateTimeField(widget=forms.DateInput(attrs={"class":"form-control",'type': 'date', "placeholder": "Seleccione fecha"}), required=False, label='Fecha de Transacción')
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

# -- # -- # -- # -- # -- # -- ## -- # -- # -- # -- # -- # -- ## -- # -- # -- # -- # -- # -- #
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

# -- # -- # -- # -- # -- # -- ## -- # -- # -- # -- # -- # -- ## -- # -- # -- # -- # -- # -- #
class ItemForm(ModelForm):
    item1 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}), label='1) Producto conforme a lo indicado en la lista de Embarque (Packing List)', required=False)
    item2 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}), label='2) Factura del Proveedor conforme a la orden de compra o solicitud de trabajo (Invoice)', required=False)
    item3 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='3) Cartilla/Orden de Trabajo, Cartilla de prueba, Si corresponde, del taller que repara', required=False)
    item4 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='4) Producto sin daños visibles (Inspeccion Visual)', required=False)
    item5 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='5) Producto protegido en embalaje apropiado', required=False)
    item6 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='6) Placa de identificacion del componente', required=False)
    item7 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='7) Documentacion Técnica completa requerida por reglamentacion (Trazabilidad)', required=False)
    item8 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='8) Formulario FAA 8130-3', required=False)
    item9 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='9) Formulario EASA Form One o JAA Form One o CAA Form One', required=False)
    item10 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='10) Formulario DGAC Chile 8130-3', required=False)
    item11 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='11) Formulario ANAC Argentina 8130-3', required=False)
    item12 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='12) Placa o Etiqueta para Herramientas o equipos con calibracion', required=False)
    item13 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='13) Certificado de Calibración en laboratorio reconocido por el estado local', required=False)
    n_item13 = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}),label='13.5) N° de Certificado de Calibración', required=False)
    item14 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='14) Materiales con vida limite (Verificacion de Shelf life data y MSDS)', required=False)
    item15 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='15) Certificado de flamabilidad, si corresponde', required=False)
    n_item15 = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}),label='15.5) N° de Certificado de Flamabilidad', required=False)
    item16 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='16) Certificado de conformidad  y/o Analisis', required=False)
    n_item16 = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}),label='16.5) N° Certificado de conformidad y/o Analisis', required=False)
    item17 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='17) Numero de lote de fabricacion, si corresponde', required=False)
    n_item17 = forms.IntegerField(widget=forms.TextInput( attrs={"class": "form-control"}),label='17.5)Numero de lote de Fabricacion', required=False)
    item18 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='18) TSO / TSN (Si Aplica)', required=False)
    item_18tsn = forms.CharField(widget=forms.Select(choices=TSN, attrs={"class": "form-control"}),label='18.5) TSN/TSO/CSN/SCO', required=False)
    n_item18tsn = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),label='18.5.1) Especifique Numero de TSN/TSO/CSN/SCO', required=False)
    item19 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='19) Material Safety Data Sheet', required=False)
    item20 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='20) Material con restriccion bajo el programa ESD', required=False)
    item21 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='21) Material con restriccion de almacenamiento (Hielo Seco)', required=False)
    item22 = forms.CharField(widget=forms.Select(choices=True_False, attrs={"class": "form-control"}),label='22) Cartilla Mantencion CMA Autorizado', required=False)
    n_item22 = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}),label='22.5) N° de Catilla Mantencion CMA Autorizado', required=False)

    class Meta:
        model = Item
        fields = [
            'item1',
            'item2',
            'item3',
            'item4',
            'item5',
            'item6',
            'item7',
            'item8',
            'item9',
            'item10',
            'item11',
            'item12',
            'item13',
            'n_item13',
            'item14',
            'item15',
            'n_item15',
            'item16',
            'n_item16',
            'item17',
            'n_item17',
            'item18',
            'item_18tsn',
            'n_item18tsn',
            'item19',
            'item20',
            'item21',
            'item22',
            'n_item22',
        ]

class DetalleForm(ModelForm):
    modelo = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Modelo"}),label='Modelo', required=False)
    Proveedor = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Proveedor del Producto"}),label='Proveedor del Producto', required=False)
    taller_reparadora = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Taller/Cia. Reparadora"}),label='Taller/Cia. Reparadora', required=False)
    trabajo_solicitado = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Trabajo Solicitado"}),label='Trabajo Solicitado', required=False)
    propiedad = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Propiedad de"}),label='Propiedad de', required=False)
    check_periodica = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Check Periodica (Si Aplica)"}),label='Check Periodica (Si Aplica)', required=False)
    ro_n = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "RO N°"}),label='RO N°', required=False)
    wo_n = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "WO N°"}),label='WO N°', required=False)
    aceptado = forms.CharField(widget=forms.Select(choices=ACEPTADO, attrs={"class": "form-control"}),label='¿Aceptado?', required=False)
    licencia = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "N° Licencia"}),label='N° Licencia', required=False)
    estado_repuesto_fk = forms.ModelChoiceField(queryset=Estado_Repuesto.objects.all(), widget=forms.Select(attrs={"class": "form-control","placeholder": "Ingresa el Estado del Repuesto"}), label='Estado del Repuesto', required=False)
    incoming_fk = forms.ModelChoiceField(queryset=Incoming.objects.all(), widget=forms.Select(attrs={"class": "form-control","placeholder": "Ingresa el SN O BN"}), label='Serial Number o Batch Number')
    class Meta:
        model = Detalle_Incoming
        fields = [
            'incoming_fk',
            'modelo',
            'Proveedor',
            'taller_reparadora',
            'trabajo_solicitado',
            'propiedad',
            'check_periodica',
            'ro_n',
            'wo_n',
            'aceptado',
            'licencia',
            'estado_repuesto_fk',
        ]