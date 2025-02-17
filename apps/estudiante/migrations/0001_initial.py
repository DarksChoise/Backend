# Generated by Django 4.2.4 on 2024-10-09 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('documento_identidad', models.CharField(max_length=50, unique=True)),
                ('fecha_nacimiento', models.DateField()),
            ],
            options={
                'db_table': 'estudiante',
            },
        ),
    ]
