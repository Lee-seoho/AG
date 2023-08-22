# Generated by Django 4.2.4 on 2023-08-16 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=10)),
                ('city_image', models.ImageField(upload_to='CityHeader/%Y/%m/%d')),
            ],
            options={
                'db_table': 'tbl_city_header',
            },
        ),
        migrations.CreateModel(
            name='CityDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_detail_name', models.CharField(max_length=10)),
                ('city_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='region.cityheader')),
            ],
            options={
                'db_table': 'tbl_city_detail',
            },
        ),
    ]