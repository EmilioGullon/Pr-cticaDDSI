# Generated by Django 4.2.7 on 2024-01-15 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_genera_unique_together_remove_genera_nomina_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='DNIS',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.socio'),
        ),
    ]
