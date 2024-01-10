# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, RegexValidator, MinLengthValidator
from django.utils import timezone

# Create your models here.

class Empleado(models.Model):
    DNIE = models.CharField(max_length=9, primary_key=True, validators=[RegexValidator(r'[0-9]{8}[a-zA-Z]$', message='Formato de DNI no válido')])
    NombreE = models.CharField(max_length=20, null=False)
    Apellido1E = models.CharField(max_length=20, null=False)
    Apellido2E = models.CharField(max_length=20, null=False)
    TelefonoE = models.PositiveIntegerField(null=False, unique=True, validators=[MinLengthValidator(limit_value=9)])
   
    def __str__(self):
        return self.nombre
class Nomina_tiene(models.Model):
    Nomina = models.BigIntegerField(primary_key=True)
    Bruto = models.DecimalField(max_digits=12, decimal_places=2, null=False, validators=[MinValueValidator(limit_value=0.01, message='El campo debe ser un número mayor que 0')])
    Impuesto = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    DNIE = models.OneToOneField(Empleado, on_delete=models.CASCADE)
class Gasto(models.Model):
    Num_factura = models.CharField(max_length=20, primary_key=True)
    Receptor = models.CharField(max_length=20, null=False)
    CantG = models.DecimalField(max_digits=12, decimal_places=2, null=False, validators=[MinValueValidator(limit_value=0.01, message='El campo debe ser un número mayor que 0')])
    FechaN = models.DateField(default=timezone.now, null=False)

    class Meta:
        abstract = True

class GastoN(Gasto):
    Nomina_tiene = models.ForeignKey(Nomina_tiene,on_delete=models.CASCADE)
    pass

class GastoP(Gasto):
    CantidadC = models.PositiveIntegerField()
    pass

class Producto(models.Model):
    Prod = models.PositiveBigIntegerField(primary_key=True)
    NombreP = models.CharField(max_length=20, null=False)
    DescripcionP = models.TextField(max_length=320, null=False)
    Precio = models.DecimalField(max_digits=6, decimal_places=2, null=False, validators=[MinValueValidator(limit_value=0.01, message='El campo debe ser un número mayor que 0')])

class Anuncio(models.Model):
    CodigoA = models.CharField(max_length=9, primary_key=True)
    TipoA = models.CharField(max_length=20, null=False)
    DescripcionA = models.TextField(max_length=100, null=False)
    LocalizacionA = models.CharField(max_length=20, null=False, unique=True)

    Productos = models.ManyToManyField(Producto, db_table='anuncia')

class Socio(models.Model):
    DNIS = models.CharField(max_length=9, primary_key=True, validators=[RegexValidator(r'[0-9]{8}[a-zA-Z]$', message='Formato de DNI no válido')])
    NombreS = models.CharField(max_length=20, null=False)
    Apellido1S = models.CharField(max_length=20, null=False)
    Apellido2S = models.CharField(max_length=20, null=False)
    TelefonoS = models.IntegerField(null=False, unique=True,validators=[MinLengthValidator(limit_value=9)])
    E_mailS = models.EmailField(max_length=320, null=False, unique=True)

    Productos = models.ManyToManyField(Producto, through='compra')

class Ingreso(models.Model):
    Ref_pago = models.PositiveBigIntegerField(primary_key=True)
    Emisor = models.CharField(max_length=20, null=False)
    TipoI = models.CharField(max_length=20, null=False)
    CantI = models.DecimalField(max_digits=8, decimal_places=2, null=False, validators=[MinValueValidator(limit_value=0.01, message='El campo debe ser un número mayor que 0')])

class Almacen(models.Model):
    Alm = models.CharField(max_length=7, primary_key=True, validators=[RegexValidator(r'^ALM-[0-9]{3}$', message='Código format like ALM-###.')])
    NombreA = models.CharField(max_length=20, null=False)
    Direccion = models.CharField(max_length=40, null=False, unique=True)
    Provincia = models.CharField(max_length=10, null=False)

    Productos = models.ManyToManyField(Producto, through='contiene')
   

class compra(models.Model):
    Prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    DNIS = models.ForeignKey(Socio, on_delete=models.CASCADE)
    FechaC = models.DateField(default=timezone.now, null=False)
    CantidadC = models.PositiveIntegerField()

    class Meta:
        unique_together = ('Prod', 'DNIS', 'FechaC')

# class produce(models.Model):
    # Ref_pago = models.OneToOneField(Ingreso, on_delete=models.CASCADE)
    # Fecha = models.DateField(default=date.today(), null=False)
    # Prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    # DNI = models.ForeignKey(Socio, on_delete=models.CASCADE)

    # class Meta:
        # unique_together = ('Fecha', 'Prod', 'DNI')

class produce(models.Model):
    Ref_pago = models.OneToOneField(Ingreso, on_delete=models.CASCADE)
    Compra = models.OneToOneField(compra, on_delete=models.CASCADE)

class contiene(models.Model):
    Prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    Alm = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    CantidadC = models.PositiveIntegerField()

    class Meta:
        unique_together = ('Prod', 'Alm')
