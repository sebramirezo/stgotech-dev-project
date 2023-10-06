from django.db import models
from django.core.validators import MinValueValidator
from .choices import *


# Create your models here.
#TABLA CATEGORIA INCOMING
class Categotia_incoming(models.Model):
    categoria_pk = models.AutoField(primary_key=True, unique=True)   
    name_categoria = models.CharField(choices=CATEGORIA_INCOMING , blank=True , null=True, max_length=50)

    class Meta:
        db_table = "categoria_incoming"
    
    def __str__(self):

        return self.name_categoria

#TABLA ESTADO  
class Estado(models.Model):
    estado_pk = models.AutoField(primary_key=True, unique=True)
    estado = models.CharField(choices=ABONA_CANCELA, blank=True, null=True, max_length=50)

    class Meta:
        db_table = "estado"
    
    def __str__(self):
        return self.estado
    

#TABLA UBICACION
class Ubicacion(models.Model):
    ubicacion_pk = models.AutoField(primary_key=True, unique= True)
    name_ubicacion = models.CharField(choices=UBICACIONES ,blank=True, null=True, max_length=50)

    class Meta:
        db_table = "ubicacion"
    
    def __str__(self):
        return self.name_ubicacion
    
#TABLA USER
class User(models.Model):
    user_pk = models.AutoField(primary_key=True, unique=True)
    nombre_user = models.CharField(blank=True, null=True, max_length=50)
    correo_user =  models.CharField(blank=True, null=True, max_length=50)
    n_telefono = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "user"
    
    def __str__(self):
        return self.nombre_user

#TABLA UOM
class Uom(models.Model):
    uom_pk = models.AutoField(primary_key=True, unique=True)
    name_uom = models.CharField(choices=UOM , blank=True, null=True, max_length=50)

    class Meta:
        db_table = "uom"

    def __str__(self):
        return self.name_uom
    
#TABLA OWNER
class Owner(models.Model):
    owner_pk = models.AutoField(primary_key=True, unique=True)
    name_owner = models.CharField(choices=OWNER, blank=True, null=True, max_length=50)

    class Meta:
        db_table = "owner"
    
    def __str__(self):
        return self.name_owner
        
#TABLA N_FICHA
class Ficha(models.Model):
    ficha_pk = models.AutoField(primary_key=True, unique=True)
    name_ficha = models.CharField(choices=N_FICHA, blank=True, null=True, max_length=50)

    class Meta:
        db_table = "n_ficha"
    
    def __str__(self):
        return self.name_ficha

#TABLA CONDICION
class Condicion(models.Model):
    condicion_pk = models.AutoField(primary_key=True, unique=True)
    name_condicion = models.CharField(choices=CONDITION, blank=True, null=True, max_length=50)

    class Meta:
        db_table = "condicion"
    
    def __str__(self):
        return self.name_condicion
    

#TABLA CLASIFICACION
class Clasificacion(models.Model):
    clasificacion_pk = models.AutoField(primary_key=True, unique=True)
    name_clasificacion = models.CharField(choices=CLASIF_CONSUMO, blank=True, null=True, max_length=50)

    class Meta:
        db_table = "clasificacion"
    
    def __str__(self):
        return self.name_clasificacion

#TABLA BODEGA
class Bodega(models.Model):
    bodega_pk = models.AutoField(primary_key=True, unique=True)
    name_bodega = models.CharField(choices=BODEGA , blank=True, null=True, max_length=50)

    class Meta:
        db_table = "bodega"

    def __str__(self):
        return self.name_bodega

#TABLA ORIGEN
class Origen(models.Model):
    origen_pk = models.AutoField(primary_key=True, unique=True)
    name_origen = models.CharField(choices=ORIGEN,blank=True, null=True, max_length=50)

    class Meta:
        db_table = "origen"

    def __str__(self):
        return self.name_origen
    


#Tabla Comat 
class Comat(models.Model):
    stdf_pk = models.IntegerField(primary_key=True, unique=True)
    awb = models.CharField(blank=True, null=True, max_length=50)
    hawb = models.CharField(blank=True, null=True, max_length=50)
    num_manifiesto = models.CharField(blank=True, null=True, max_length=50)
    corr_interno = models.CharField(blank=True, null=True, max_length=50)
    pcs = models.IntegerField(blank=True, null=True)
    peso = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2, default="0")
    f_control = models.DateTimeField(null=True, blank=True)
    f_manifiesto = models.DateTimeField(null=True, blank=True)
    f_recepcion = models.DateTimeField(null=True, blank=True)
    f_stdf = models.DateField(null=True, blank=True)
    fob = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2, default="0")
    flete = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2, default="0")
    seguro = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2, default="0")
    sum_cif = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2, default="0")
    observaciones = models.CharField(blank=True, null=True, max_length=250)
    #Claves Foraneas
    bodega_fk = models.ForeignKey(Bodega , on_delete=models.SET_NULL, null=True)
    origen_fk = models.ForeignKey(Origen, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'comat'

    def __int__(self):
        return self.stdf_pk
    
#Tabla Incoming
class Incoming(models.Model):
    sn_batch_pk = models.CharField(primary_key=True, unique=True)
    part_number = models.CharField(blank=True, null=True, max_length=50)
    f_incoming = models.DateField(blank=True, null=True)
    descripcion = models.CharField(blank=True , null=True, max_length=250)
    po = models.CharField(blank=True, null=True, max_length=50)
    qty = models.IntegerField(blank=True, null=True)
    u_purchase_cost = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    total_u_purchase_cost = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    f_vencimiento = models.DateField(blank=True, null=True)
    saldo = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    observaciones = models.CharField(blank=True, null=True, max_length=250)
    #Llaves foraneas
    categoria_fk = models.ForeignKey(Categotia_incoming, on_delete=models.SET_NULL, null=True)
    clasificacion_fk = models.ForeignKey(Clasificacion, on_delete=models.SET_NULL, null=True)
    ubicacion_fk = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL, null=True)
    uom_fk = models.ForeignKey(Uom, on_delete=models.SET_NULL, null=True)
    owner_fk = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)
    condicion_fk = models.ForeignKey(Condicion,on_delete=models.SET_NULL, null=True)
    ficha_fk = models.ForeignKey(Ficha, on_delete=models.SET_NULL, null=True)
    stdf_fk = models.ForeignKey(Comat, on_delete=models.CASCADE)

    class Meta:
        db_table = 'incoming'
    
    def __str__(self):
        return self.sn_batch_pk



class Consumos(models.Model):
    consumo_pk = models.AutoField(primary_key=True, unique=True , validators=[MinValueValidator(1)])
    orden_consumo = models.CharField(blank=True, null=True, max_length=50)
    f_transaccion = models.DateField(blank=True, null=True)
    qty_extraida = models.IntegerField(blank=True, null=True)
    matricula_aeronave = models.CharField(blank=True, null=True, max_length=50)
    observaciones = models.CharField(blank=True, null=True, max_length=250)
    incoming_fk = models.ForeignKey(Incoming, null=True, blank=True,on_delete=models.CASCADE)
    estado_fk = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)


    class Meta:
        db_table = "consumos"

    def __str__(self):
        return str(self.incoming_fk)