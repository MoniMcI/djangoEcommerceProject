# Generated by Django 4.1.3 on 2022-12-02 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cat', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_prod', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(max_length=500)),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(upload_to='fotos/productos')),
                ('stock', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.categoria')),
            ],
        ),
    ]
