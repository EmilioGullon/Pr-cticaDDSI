# Generated by Django 4.2.7 on 2024-01-15 16:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('Alm', models.CharField(max_length=7, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^ALM-[0-9]{3}$', message='Código format like ALM-###.')])),
                ('NombreA', models.CharField(max_length=20)),
                ('Direccion', models.CharField(max_length=40, unique=True)),
                ('Provincia', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaC', models.DateField(default=django.utils.timezone.now)),
                ('CantidadC', models.PositiveIntegerField()),
                ('Alm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.almacen')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('DNIE', models.CharField(max_length=9, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('[0-9]{8}[a-zA-Z]$', message='Formato de DNI no válido')])),
                ('NombreE', models.CharField(max_length=20)),
                ('Apellido1E', models.CharField(max_length=20)),
                ('Apellido2E', models.CharField(max_length=20)),
                ('TelefonoE', models.PositiveIntegerField(unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=9)])),
            ],
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('Ref_pago', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('Emisor', models.CharField(max_length=20)),
                ('TipoI', models.CharField(max_length=20)),
                ('CantI', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(limit_value=0.01, message='El campo debe ser un número mayor que 0')])),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('Prod', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('NombreP', models.CharField(max_length=20)),
                ('DescripcionP', models.TextField(max_length=320)),
                ('Precio', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(limit_value=0.01, message='El campo debe ser un número mayor que 0')])),
            ],
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('DNIS', models.CharField(max_length=9, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('[0-9]{8}[a-zA-Z]$', message='Formato de DNI no válido')])),
                ('NombreS', models.CharField(max_length=20)),
                ('Apellido1S', models.CharField(max_length=20)),
                ('Apellido2S', models.CharField(max_length=20)),
                ('TelefonoS', models.IntegerField(unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=9)])),
                ('E_mailS', models.EmailField(max_length=320, unique=True)),
                ('Productos', models.ManyToManyField(through='app.compra', to='app.producto')),
            ],
        ),
        migrations.CreateModel(
            name='produce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Compra', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.compra')),
                ('Ref_pago', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.ingreso')),
            ],
        ),
        migrations.CreateModel(
            name='Nomina_tiene',
            fields=[
                ('Nomina', models.BigIntegerField(primary_key=True, serialize=False)),
                ('Bruto', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(limit_value=0.01, message='El campo debe ser un número mayor que 0')])),
                ('Impuesto', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('DNIE', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='GastoP',
            fields=[
                ('Num_factura', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Receptor', models.CharField(max_length=20)),
                ('CantG', models.DecimalField(decimal_places=2, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(limit_value=0.01, message='El campo debe ser un número mayor que 0')])),
                ('Fecha', models.DateField(default=django.utils.timezone.now)),
                ('CantidadC', models.PositiveIntegerField()),
                ('Almacen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.almacen')),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GastoN',
            fields=[
                ('Num_factura', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Receptor', models.CharField(max_length=20)),
                ('CantG', models.DecimalField(decimal_places=2, max_digits=12, null=True, validators=[django.core.validators.MinValueValidator(limit_value=0.01, message='El campo debe ser un número mayor que 0')])),
                ('Fecha', models.DateField(default=django.utils.timezone.now)),
                ('Nomina_tiene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.nomina_tiene')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='contiene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CantidadC', models.PositiveIntegerField()),
                ('Alm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.almacen')),
                ('Prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
            ],
            options={
                'unique_together': {('Prod', 'Alm')},
            },
        ),
        migrations.AddField(
            model_name='compra',
            name='DNIS',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.socio'),
        ),
        migrations.AddField(
            model_name='compra',
            name='Prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto'),
        ),
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('CodigoA', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('TipoA', models.CharField(max_length=20)),
                ('DescripcionA', models.TextField(max_length=100)),
                ('LocalizacionA', models.CharField(max_length=20, unique=True)),
                ('Productos', models.ManyToManyField(db_table='anuncia', to='app.producto')),
            ],
        ),
        migrations.AddField(
            model_name='almacen',
            name='Productos',
            field=models.ManyToManyField(through='app.contiene', to='app.producto'),
        ),
        migrations.AlterUniqueTogether(
            name='compra',
            unique_together={('Prod', 'DNIS', 'FechaC')},
        ),
    ]
