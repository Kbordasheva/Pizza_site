# Generated by Django 3.0.2 on 2020-01-23 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('description', models.TextField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Pizza',
                'verbose_name_plural': 'Pizzas',
            },
        ),
        migrations.CreateModel(
            name='PizzaProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pizzas_images')),
                ('pizza_product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='pizza_products.PizzaProduct')),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
            },
        ),
    ]