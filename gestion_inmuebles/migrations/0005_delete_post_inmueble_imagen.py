# Generated by Django 5.1.3 on 2024-11-19 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inmuebles', '0004_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='inmueble',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='static/img'),
        ),
    ]
