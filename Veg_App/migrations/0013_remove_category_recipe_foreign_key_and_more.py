# Generated by Django 4.2.2 on 2024-02-28 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Veg_App', '0012_alter_recipe_imagefile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='recipe_foreign_key',
        ),
        migrations.AddField(
            model_name='recipe',
            name='category_ref',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Veg_App.category'),
        ),
    ]