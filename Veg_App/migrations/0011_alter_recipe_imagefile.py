# Generated by Django 4.2.2 on 2024-02-28 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Veg_App', '0010_alter_recipe_calory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='imagefile',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]