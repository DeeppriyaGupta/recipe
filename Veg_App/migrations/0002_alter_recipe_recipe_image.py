# Generated by Django 4.2.10 on 2024-02-21 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Veg_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_image',
            field=models.ImageField(upload_to='staic/image'),
        ),
    ]
