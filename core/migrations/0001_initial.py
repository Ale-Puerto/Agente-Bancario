# Generated by Django 3.0.3 on 2020-02-22 00:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('IdCliente', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Nombres', models.CharField(max_length=50)),
                ('Apellidos', models.CharField(max_length=50)),
                ('Nacionalidad', models.CharField(max_length=30)),
                ('Ciudad', models.CharField(max_length=50)),
                ('Direccion', models.CharField(max_length=50)),
                ('Sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('Fecha_Nac', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('Id_Cuenta', models.CharField(max_length=50)),
                ('Tipo', models.CharField(max_length=50)),
                ('Monto', models.FloatField()),
                ('Saldo_anterior', models.FloatField()),
                ('Saldo_nuevo', models.FloatField()),
                ('Fecha_Transaccion', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('IdCuenta', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('PIN', models.IntegerField()),
                ('Tipo', models.CharField(choices=[('$ DLS', 'Dolares'), ('CORD, NIO', 'Cordoba')], max_length=10)),
                ('Fecha_Apertura', models.DateField(auto_now_add=True)),
                ('interes', models.FloatField()),
                ('Monto', models.FloatField()),
                ('ClientAsig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Cliente')),
            ],
        ),
    ]
