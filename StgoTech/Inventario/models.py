from django.db import models

# Create your models here.
#TABLA ESTADO  
class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True, unique=True)
    estado = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = "estado"
    
    def __str__(self):
        return str(self.eid_estado)
    
#TABLA DESCRIPCIÓN
class Descripcion(models.Model):
    id_descripcion = models.AutoField(primary_key=True, unique=True)
    name_descripcion = models.CharField(blank=True, null=True, max_length=50)
    incoming_id_sn_batch = models.ForeignKey()

    class Meta:
        db_table = "descripcion"
    
    def __str__(self):
        return str(self.eid_descripcion)

#TABLA UBICACION
class Ubicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True, unique= True)
    ubicacion = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = "ubicacion"
    
    def __str__(self):
        return str(self.eid_ubicacion)
    
#TABLA USER
class User(models.Model):
    id_user = models.AutoField(primary_key=True, unique=True)
    nombre_user = models.CharField(blank=True, null=True, max_length=50)
    correo_user =  models.CharField(blank=True, null=True, max_length=50)
    n_telefono = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "user"
    
    def __str__(self):
        return str(self.eid_user)

#TABLA UOM
class Uom(models.Model):
    id_uom = models.AutoField(primary_key=True, unique=True)
    name_uom = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = "uom"

    def __str__(self):
        return str(self.eid_uom)
    
#TABLA OWNER
class Owner(models.Model):
    id_owner = models.AutoField(primary_key=True, unique=True)
    name_owner = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = "owner"
    
    def __str__(self):
        return str(self.eid_owner)

#TABLA N_FICHA
class Ficha(models.Model):
    id_ficha = models.AutoField(primary_key=True, unique=True)
    name_ficha = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = "ficha"
    
    def __str__(self):
        return str(self.eid_ficha)

#TABLA CONDICION
class Condicion(models.Model):
    id_condicion = models.AutoField(primary_key=True, unique=True)
    name_condicion = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = "condicion"
    
    def __str__(self):
        return str(self.eid_condicion)

#TABLA CLASIFICACION
class Clasificacion(models.Model):
    id_clasificacion = models.AutoField(primary_key=True, unique=True)
    name_clasificacion = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = "clasificacion"
    
    def __str__(self):
        return str(self.eid_clasificacion)

#TABLA BODEGA
class Bodega(models.Model):
    id_bodega = models.AutoField(primary_key=True, unique=True)
    name_bodega = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = "bodega"

    def __str__(self):
        return str(self.eid_bodega)

#TABLA ORIGEN
class Origen(models.Model):
    id_origen = models.AutoField(primary_key=True, unique=True)
    name_origen = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = "origen"

    def __str__(self):
        return str(self.eid_origen)
    
#TABLA OBSERVACION
class Observacion(models.Model):
    id_observacion = models.AutoField(primary_key=True, unique=True)
    observacion = models.CharField(blank=True, null=True, max_length=50)
    comat_id_stdf = models.IntegerField(blank=True, null=True)
    incoming_id_sn_batch = models.IntegerField(blank=True, null=True)
    consumo_id_consumo = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "observacion"
    
    def __str__(self):
        return str(self.eid_observacion)
    
