# Generated by Django 4.1.3 on 2022-11-13 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CienciaFiccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('autor', models.CharField(max_length=40)),
                ('sinopsis', models.CharField(max_length=255)),
                ('url_portada', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Distopia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('autor', models.CharField(max_length=40)),
                ('sinopsis', models.CharField(max_length=255)),
                ('url_portada', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Fantasia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('autor', models.CharField(max_length=40)),
                ('sinopsis', models.CharField(max_length=255)),
                ('url_portada', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Terror',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('autor', models.CharField(max_length=40)),
                ('sinopsis', models.CharField(max_length=255)),
                ('url_portada', models.CharField(max_length=40)),
            ],
        ),
    ]
