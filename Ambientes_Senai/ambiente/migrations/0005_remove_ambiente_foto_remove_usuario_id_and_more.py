# Generated by Django 5.0.6 on 2024-05-31 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambiente', '0004_alter_reserva_data_alter_reserva_horario_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ambiente',
            name='foto',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]