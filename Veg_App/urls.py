from django.urls import path
from Veg_App.views import RecipeView, DemoView, Delete_recipe, Update_recipe, All_recipe


urlpatterns = [
    path('recipe/', RecipeView, name = 'recipe-view' ),
    path('all-recipe/', All_recipe, name ='all-recipe'),
    path('demo/', DemoView, name='demo-view'),
    path('delete/<id>/', Delete_recipe, name='delete-recipe'),
    path('update/<id>/', Update_recipe, name='update-recipe'),
]
