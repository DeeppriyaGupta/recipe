# Generated by Django 4.2.10 on 2024-02-21 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=100)),
                ('recipe_desc', models.TextField()),
                ('recipe_image', models.ImageField(upload_to='recipe')),
            ],
        ),
    ]
