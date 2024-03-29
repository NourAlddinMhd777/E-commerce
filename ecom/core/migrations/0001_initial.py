# Generated by Django 5.0.1 on 2024-02-25 04:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('discraption', models.CharField(default='', max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('category', models.CharField(choices=[('Tehnology', 'Tech'), ('Kids', 'Kids'), ('Furniture', 'Furniture'), ('Clothes', 'Clothes'), ('Books', 'Books'), ('Elegance_and_Beauty', 'Elegance And Beauty')], max_length=40)),
                ('brand', models.CharField(default='', max_length=100)),
                ('ratings', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('stock', models.IntegerField(default=0)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
