# Generated by Django 3.2.10 on 2023-02-23 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deatilescustomer',
            name='confirmpassword',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
