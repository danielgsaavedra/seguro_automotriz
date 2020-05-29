# Generated by Django 3.0.6 on 2020-05-28 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20200527_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='poliza',
            name='usuario_rut_usuario',
            field=models.ForeignKey(db_column='usuario_rut_usuario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Rut Usuario'),
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='usuario_rut_usuario',
            field=models.ForeignKey(db_column='usuario_rut_usuario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Rut Usuario'),
        ),
    ]
