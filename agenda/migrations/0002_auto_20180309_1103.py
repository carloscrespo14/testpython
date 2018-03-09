# Generated by Django 2.0.3 on 2018-03-09 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='correo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='apellidos',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='cowner',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='organizacion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='red',
            field=models.CharField(blank=True, choices=[('FB', 'Facebook'), ('TW', 'Twitter'), ('IN', 'Instagram'), ('YT', 'Youtbe'), ('OT', 'Otros')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='sowner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='social', to='agenda.Contacto'),
        ),
        migrations.AlterField(
            model_name='social',
            name='urln',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='telefono',
            name='numero',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='telefono',
            name='tipo',
            field=models.CharField(blank=True, choices=[('C', 'Celular'), ('P', 'Particular'), ('L', 'Laboral'), ('F', 'Principal'), ('O', 'Otros')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='telefono',
            name='towner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telefono', to='agenda.Contacto'),
        ),
    ]
