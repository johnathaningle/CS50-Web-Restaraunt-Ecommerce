# Generated by Django 2.1.5 on 2019-01-26 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=20)),
                ('num_toppings', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='customer_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.User'),
        ),
    ]
