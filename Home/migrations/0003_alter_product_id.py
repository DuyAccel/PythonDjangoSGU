# Generated by Django 4.0.3 on 2022-05-18 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
