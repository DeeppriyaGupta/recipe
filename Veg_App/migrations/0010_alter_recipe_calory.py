# Generated by Django 4.2.2 on 2024-02-28 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Veg_App', '0009_alter_recipe_calory_alter_recipe_imagefile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='calory',
            field=models.IntegerField(),
        ),
    ]
