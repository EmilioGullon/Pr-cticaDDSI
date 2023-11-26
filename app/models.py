# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
# Create your models here.
class Empleado(models.Model):
    DNIE = models.CharField(max_length=9, primary_key=True)
    NombreE = models.CharField(max_length=20, null=False)
    Apellido1E = models.CharField(max_length=20, null=False)
    Apellido2E = models.CharField(max_length=20, null=False)
    TelefonoE = models.IntegerField(null=False, unique=True)
    
    def __str__(self):
        return self.nombre

class Gasto(models.Model):
    Num_factura = models.CharField(max_length=20, primary_key=True)
    Receptor = models.CharField(max_length=20, null=False)
    TipoG = models.CharField(max_length=20, null=False)
    CantG = models.DecimalField(max_digits=5, decimal_places=2, null=False)

class Producto(models.Model):
    Prod = models.BigIntegerField(primary_key=True)
    NombreP = models.CharField(max_length=20, null=False)
    DescripcionP = models.CharField(max_length=320, null=False)
    Precio = models.DecimalField(max_digits=4, decimal_places=2, null=False, validators=[MinValueValidator(0.01)])

    Gasto = models.OneToOneField(Gasto, on_delete=models.CASCADE, null=False, blank=False)

class Anuncio(models.Model):
    CodigoA = models.CharField(max_length=9, primary_key=True)
    TipoA = models.CharField(max_length=20, null=False)
    DescripcionA = models.CharField(max_length=100, null=False)
    LocalizacionA = models.CharField(max_length=20, null=False, unique=True)

    #Producto = models.ManyToManyField(Producto)

class Socio(models.Model):
    DNIS = models.CharField(max_length=9, primary_key=True)
    NombreS = models.CharField(max_length=20, null=False)
    Apellido1S = models.CharField(max_length=20, null=False)
    Apellido2S = models.CharField(max_length=20, null=False)
    TelefonoS = models.IntegerField(null=False, unique=True)
    E_mailS = models.EmailField(max_length=320, null=False, unique=True)

    #Producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=False, blank=False)

class Ingreso(models.Model):
    Ref_pago = models.BigIntegerField(primary_key=True)
    Emisor = models.CharField(max_length=20, null=False)
    TipoI = models.CharField(max_length=20, null=False)
    CantI = models.FloatField(null=False)

class Almacen(models.Model):
    Alm = models.CharField(max_length=7, primary_key=True, validators=[RegexValidator(r'^ALM-[0-9]{3}$', 'Formato de Alm no válido')])
    NombreA = models.CharField(max_length=20, null=False)
    Direccion = models.CharField(max_length=40, null=False, unique=True)
    Provincia = models.CharField(max_length=10, null=False)

    Productos = models.ManyToManyField(Producto, through='Contiene')
    
class Nomina_tiene(models.Model):
    Nomina = models.BigIntegerField(primary_key=True)
    Bruto = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    Impuesto = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    DNIE = models.CharField(max_length=9, null=True)  # Puede ser nulo si así lo deseas
    Empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=False)  # Es nulo devido a que no puede existir nomina sin empleado

class Genera(models.Model):
    Nomina = models.OneToOneField(Nomina_tiene, on_delete=models.CASCADE, primary_key=True)
    Num_factura = models.IntegerField(unique=True, null=False)
    Fecha = models.DateField(null=False)
    class Meta:
        unique_together = ('Nomina', 'Num_factura', 'Fecha')

class Contiene(models.Model):
    Alm = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    Prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    CantidadP = models.IntegerField(default=1)

    class Meta:
        unique_together = ('Prod', 'Alm')

