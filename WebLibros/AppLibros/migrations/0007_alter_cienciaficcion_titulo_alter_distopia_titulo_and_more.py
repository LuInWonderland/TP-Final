# Generated by Django 4.1.3 on 2022-12-08 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLibros', '0006_alter_cienciaficcion_sinopsis_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cienciaficcion',
            name='titulo',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='distopia',
            name='titulo',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='fantasia',
            name='titulo',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='terror',
            name='titulo',
            field=models.CharField(max_length=255),
        ),
    ]