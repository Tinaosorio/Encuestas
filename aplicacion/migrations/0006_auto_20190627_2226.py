# Generated by Django 2.2.1 on 2019-06-27 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0005_auto_20190625_2022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipopregunta',
            options={'verbose_name': 'Tipo de Pregunta', 'verbose_name_plural': 'Tipos de Preguntas'},
        ),
        migrations.AddField(
            model_name='estudiante',
            name='documento',
            field=models.CharField(default=None, max_length=15, unique=True),
            preserve_default=False,
        ),
    ]
