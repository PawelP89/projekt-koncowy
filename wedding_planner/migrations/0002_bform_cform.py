# Generated by Django 3.1.1 on 2020-09-05 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_planner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wearf', models.DecimalField(decimal_places=2, max_digits=8)),
                ('wearm', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=8)),
                ('plate_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('music', models.DecimalField(decimal_places=2, max_digits=8)),
                ('movie', models.DecimalField(decimal_places=2, max_digits=8)),
                ('photo', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='CForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wearf', models.DecimalField(decimal_places=2, max_digits=8)),
                ('wearm', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=8)),
                ('plate_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('music', models.DecimalField(decimal_places=2, max_digits=8)),
                ('movie', models.DecimalField(decimal_places=2, max_digits=8)),
                ('photo', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
