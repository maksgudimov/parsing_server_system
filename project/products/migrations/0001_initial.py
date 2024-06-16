# Generated by Django 5.0.4 on 2024-05-04 17:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parsing', '0001_initial'),
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField(blank=True, null=True)),
                ('img_url', models.URLField(blank=True, null=True)),
                ('price', models.DecimalField(db_index=True, decimal_places=2, max_digits=10)),
                ('last_price', models.DecimalField(blank=True, db_index=True, decimal_places=2, max_digits=10, null=True)),
                ('discount', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('validity_date', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parsing.parsingsetting')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.shop')),
            ],
        ),
    ]
