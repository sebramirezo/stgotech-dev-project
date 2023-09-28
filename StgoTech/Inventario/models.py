from django.db import models
from django.core.validators import MinValueValidator
from .choices import *

# Create your models here.
#TABLA CATEGORIA INCOMING
class Categotia_incoming(models.Model):
    id_categoria = models.AutoField(primary_key=True, unique=True)   
    name_categoria = models.CharField(choices=CATEGORIA_INCOMING , blank=True , null=True, max_length=50)

    class Meta:
        db_table = "categoria_incoming"
    
    def __str__(self):
        return self.id_categoria

#TABLA ESTADO  
class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True, unique=True)
    estado = models.CharField(choices=ABONA_CANCELA, blank=True, null=True, max_length=50)

    class Meta:
        db_table = "estado"
    
    def __str__(self):
        return self.id_estado
    
#TABLA DESCRIPCIÓN
class Descripcion(models.Model):
    id_descripcion = models.AutoField(primary_key=True, unique=True)
    name_descripcion = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        db_table = "descripcion"
    
    def __str__(self):
        return self.id_descripcion

#TABLA UBICACION
class Ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True, unique= True)
    ubicacion = models.CharField(choices=UBICACIONES ,blank=True, null=True, max_length=50)

    class Meta:
        db_table = "ubicacion"
    
    def __str__(self):
        return self.ubicacion
    
#TABLA USER
class User(models.Model):
    id_user = models.AutoField(primary_key=True, unique=True)
    nombre_user = models.CharField(blank=True, null=True, max_length=50)
    correo_user =  models.CharField(blank=True, null=True, max_length=50)
    n_telefono = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "user"
    
    def __str__(self):
        return self.nombre_user

#TABLA UOM
class Uom(models.Model):
    id_uom = models.AutoField(primary_key=True, unique=True)
    name_uom = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = "uom"

    def __str__(self):
        return self.name_uom
    
#TABLA OWNER
class Owner(models.Model):
    id_owner = models.AutoField(primary_key=True, unique=True)
    name_owner = models.CharField(choices=OWNER, blank=True, null=True, max_length=50)

    class Meta:
        db_table = "owner"
    
    def __str__(self):
        return self.name_owner

#TABLA N_FICHA
class Ficha(models.Model):
    id_ficha = models.AutoField(primary_key=True, unique=True)
    name_ficha = models.CharField(choices=N_FICHA, blank=True, null=True, max_length=50)

    class Meta:
        db_table = "n_ficha"
    
    def __str__(self):
        return self.name_ficha

#TABLA CONDICION
class Condicion(models.Model):
    id_condicion = models.AutoField(primary_key=True, unique=True)
    name_condicion = models.CharField(choices=CONDITION, blank=True, null=True, max_length=50)

    class Meta:
        db_table = "condicion"
    
    def __str__(self):
        return self.name_condicion

#TABLA CLASIFICACION
class Clasificacion(models.Model):
    id_clasificacion = models.AutoField(primary_key=True, unique=True)
    name_clasificacion = models.CharField(choices=CLASIF_CONSUMO, blank=True, null=True, max_length=50)

    class Meta:
        db_table = "clasificacion"
    
    def __str__(self):
        return self.name_clasificacion

#TABLA BODEGA
class Bodega(models.Model):
    id_bodega = models.IntegerField(primary_key=True, unique=True)
    name_bodega = models.CharField(choices=BODEGA , blank=True, null=True, max_length=50)

    class Meta:
        db_table = "bodega"

    def __str__(self):
        return self.name_bodega

#TABLA ORIGEN
class Origen(models.Model):
    id_origen = models.AutoField(primary_key=True, unique=True)
    name_origen = models.CharField(choices=ORIGEN,blank=True, null=True, max_length=50)

    class Meta:
        db_table = "origen"

    def __str__(self):
        return self.name_origen
    
#TABLA OBSERVACION
class Observacion(models.Model):
    id_observacion = models.AutoField(primary_key=True, unique=True)
    observacion = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        db_table = "observacion"
    
    def __int__(self):
        return self.id_observacion

#Tabla Comat 
class Comat(models.Model):
    id_stdf = models.IntegerField(primary_key=True, unique=True)
    awb = models.CharField(blank=True, null=True, max_length=50)
    hawb = models.CharField(blank=True, null=True, max_length=50)
    num_manifiesto = models.CharField(blank=True, null=True, max_length=50)
    corr_interno = models.CharField(blank=True, null=True, max_length=50)
    pcs = models.IntegerField(blank=True, null=True)
    peso = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2, default="0")
    f_control = models.DateTimeField(null=True, blank=True)
    f_manifiesto = models.DateTimeField(null=True, blank=True)
    f_recepcion = models.DateTimeField(null=True, blank=True)
    f_stdf = models.DateField(null=True, blank=True)
    fob = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2, default="0")
    flete = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2, default="0")
    seguro = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2, default="0")
    sum_cif = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2, default="0")
    #Claves Foraneas
    id_bodega = models.ForeignKey(Bodega , on_delete=models.CASCADE)
    id_observacion = models.ForeignKey(Observacion , on_delete=models.CASCADE)
    id_origen = models.ForeignKey(Origen, on_delete=models.CASCADE)

    class Meta:
        db_table = 'comat'

    def __int__(self):
        return self.id_stdf
    
#Tabla Incoming
class Incoming(models.Model):
    id_sn_batch = models.CharField(primary_key=True, unique=True)
    part_number = models.CharField(blank=True, null=True, max_length=50)
    f_incoming = models.DateField(blank=True, null=True)
    po = models.CharField(blank=True, null=True, max_length=50)
    qty = models.IntegerField(blank=True, null=True)
    u_purchase_cost = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    total_u_purchase_cost = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    f_vencimiento = models.DateField(blank=True, null=True)
    saldo = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    #Llaves foraneas
    id_categoria = models.ForeignKey(Categotia_incoming, on_delete=models.CASCADE)
    id_clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE)
    id_ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    id_descripcion = models.ForeignKey(Descripcion, on_delete=models.CASCADE)
    id_uom = models.ForeignKey(Uom, on_delete=models.CASCADE)
    id_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    id_condicion = models.ForeignKey(Condicion, on_delete=models.CASCADE)
    id_ficha = models.ForeignKey(Ficha, on_delete=models.CASCADE)
    id_observacion = models.ForeignKey(Observacion, on_delete=models.CASCADE)
    id_stdf = models.ForeignKey(Comat, on_delete=models.CASCADE)

    class Meta:
        db_table = 'incoming'
    
    def __str__(self):
        return self.id_sn_batch



class Consumos(models.Model):
    id_consumo = models.CharField(primary_key=True, unique=True)
    orden_consumo = models.CharField(blank=True, null=True, max_length=50)
    f_transaccion = models.DateField(blank=True, null=True)
    qty_extraida = models.IntegerField(blank=True, null=True)
    matricula_aeronave = models.CharField(blank=True, null=True, max_length=50)
    incoming_id = models.ForeignKey(Incoming, null=True, blank=True, on_delete=models.CASCADE)
    id_observacion = models.ForeignKey(Observacion, on_delete=models.CASCADE)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE)


    class Meta:
        db_table = "consumos"

    def __str__(self):
        return self.id_consumos