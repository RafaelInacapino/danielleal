# Generated by Django 4.1.4 on 2022-12-07 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0002_reserva_inicial1_reserva_inicial2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva_Final1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observaciones1', models.CharField(blank=True, max_length=100, null=True)),
                ('foto_tacometro_final1', models.ImageField(blank=True, null=True, upload_to='reservas/media')),
                ('recarga_combustible1', models.ImageField(blank=True, null=True, upload_to='reservas/media')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva_Final2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observaciones2', models.CharField(blank=True, max_length=100, null=True)),
                ('foto_tacometro_final2', models.ImageField(blank=True, null=True, upload_to='reservas/media')),
                ('recarga_combustible2', models.ImageField(blank=True, null=True, upload_to='reservas/media')),
            ],
        ),
        migrations.RenameField(
            model_name='reserva_inicial1',
            old_name='direccion',
            new_name='direccion1',
        ),
        migrations.RenameField(
            model_name='reserva_inicial1',
            old_name='motivo',
            new_name='motivo1',
        ),
        migrations.RenameField(
            model_name='reserva_inicial2',
            old_name='direccion',
            new_name='direccion2',
        ),
        migrations.RenameField(
            model_name='reserva_inicial2',
            old_name='motivo',
            new_name='motivo2',
        ),
    ]
