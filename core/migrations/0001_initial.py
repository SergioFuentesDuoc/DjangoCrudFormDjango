# Generated by Django 4.1.5 on 2023-06-03 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre categoria')),
            ],
        ),
    ]
