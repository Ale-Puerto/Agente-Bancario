from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Cliente(models.Model):
    CHOICES_GENRES = (
    ('M' , 'Masculino'),
    ('F' , 'Femenino')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    IdCliente = models.CharField(primary_key = True, max_length = 30)
    Nombres = models.CharField(max_length = 50)
    Apellidos = models.CharField(max_length = 50)
    Nacionalidad = models.CharField(max_length = 30)
    Ciudad = models.CharField(max_length = 50)
    Direccion = models.CharField(max_length = 50)
    Sexo = models.CharField(max_length = 1, choices = CHOICES_GENRES)
    Fecha_Nac = models.DateField(auto_now_add = False )
    
    
    def __str__(self):
        return '%s''%s' %(self.Nombres, self.Apellidos)
    
    
    
    
    
    
    
    
class Cuenta(models.Model):
    CHOICES_KIND = (
        ('$ DLS' , 'Dolares'),
        ('CORD, NIO', 'Cordoba')
    )
    IdCuenta = models.CharField(primary_key = True, max_length = 50)
    PIN = models.IntegerField()
    Tipo = models.CharField(max_length = 10, choices = CHOICES_KIND)
    Fecha_Apertura = models.DateField(auto_now_add = True)
    interes = models.FloatField()
    Monto = models.FloatField()
    ClientAsig =  models.ForeignKey(Cliente, on_delete = models.CASCADE)
    
    
    
    
    
class Transaccion(models.Model):
    slug  = models.SlugField(primary_key = True, max_length = 50)
    Id_Cuenta =  models.CharField(max_length = 50)
    Tipo = models.CharField(max_length = 50)
    Monto = models.FloatField()
    Saldo_anterior = models.FloatField()
    Saldo_nuevo =  models.FloatField()
    Fecha_Transaccion = models.DateField(auto_now_add = True)
    
    
    def __str__(self):
        return self.IdTransaccion
    
    def get_absolute_url(self):
        return reverse("core:transaccion_detail", kwargs={"slug": self.slug})
    
    
    
    
    

