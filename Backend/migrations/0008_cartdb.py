# Generated by Django 4.1.4 on 2023-02-19 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0007_productdb_image2_productdb_image3'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Quantity', models.CharField(blank=True, max_length=30, null=True)),
                ('Total', models.ImageField(blank=True, null=True, upload_to='media')),
            ],
        ),
    ]
