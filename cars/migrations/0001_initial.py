# Generated by Django 5.0.7 on 2024-07-25 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Model', models.CharField(max_length=200)),
                ('FactoryYear', models.IntegerField(max_length=10)),
                ('ModelYear', models.IntegerField(max_length=10)),
                ('Place', models.CharField(blank=True, max_length=10, null=True)),
                ('Value', models.FloatField(max_length=10)),
                ('Photo', models.ImageField(upload_to='cars/')),
                ('Brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='car_brand', to='cars.brand')),
            ],
        ),
    ]
