from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length= 100)
    instruction = models.TextField()
    imagefile = models.ImageField(upload_to= 'images')
    ingredients = models.TextField()
    time_took = models.IntegerField()
    calory = models.IntegerField()
    serving = models.IntegerField()
    category_ref = models.ForeignKey("Category", on_delete = models.CASCADE, null=True)



class Category(models.Model):
    name = models.CharField(max_length=100,choices = (('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Bevarages', 'Bevarages'), ('Breakfast', 'Breakfast')))




