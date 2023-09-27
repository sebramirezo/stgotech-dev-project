from django.db import models
from django.core.validators import MinValueValidator
from .choices import *

# Create your models here.
#Tabla Comat 
class Comat(models.Model):
    id_stdf = models.AutoField(auto_created=True, primary_key=True, unique=True)
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

    class Meta:
        db_table = 'comat'

    def __str__(self):
        return str(self.id_stdf)
    
#Tabla Incoming
class Incoming(models.Model):
    id_sn_batch = models.AutoField(auto_created=True, primary_key=True, unique=True)
    categoria = models.CharField(max_length=50)
    f_incoming = models.DateField(blank=True, null=True)
    po = models.CharField(blank=True, null=True, max_length=50)
    qty = models.IntegerField(blank=True, null=True)
    u_purchase_cost = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    total_u_purchase_cost = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    f_vencimiento = models.DateField(blank=True, null=True)
    saldo = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])

    class Meta:
        db_table = 'incoming'



class Consumos(models.Model):
    id_consumo = models.AutoField(auto_created=True, primary_key=True, unique=True)
    orden_consumo = models.CharField(blank=True, null=True, max_length=50)
    f_transaccion = models.DateField(blank=True, null=True)
    qty_extraida = models.IntegerField(blank=True, null=True)
    matricula_aeronave = models.CharField(blank=True, null=True, max_length=50)
    # eincoming_id = models.ForeignKey(Incoming, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "consumos"

    def __str__(self):
        return str(self.id_consumos)