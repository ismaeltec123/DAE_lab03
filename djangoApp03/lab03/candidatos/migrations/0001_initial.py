# Generated by Django 5.1.1 on 2024-09-06 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('dni', models.CharField(max_length=20)),
            ],
        ),
    ]
