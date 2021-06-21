# Generated by Django 3.2.4 on 2021-06-21 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=256)),
                ('brand', models.CharField(max_length=256)),
                ('shop_name', models.CharField(max_length=256)),
                ('qty_available', models.PositiveIntegerField(default=0)),
                ('user_id', models.PositiveIntegerField()),
            ],
        ),
    ]