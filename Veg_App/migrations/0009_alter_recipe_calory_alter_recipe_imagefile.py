# Generated by Django 4.2.2 on 2024-02-28 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Veg_App', '0008_alter_recipe_calory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='calory',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='imagefile',
            field=models.ImageField(upload_to='static/image'),
        ),
    ]
