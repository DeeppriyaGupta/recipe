# Generated by Django 4.2.2 on 2024-02-28 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Veg_App', '0011_alter_recipe_imagefile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='imagefile',
            field=models.ImageField(upload_to='images'),
        ),
    ]