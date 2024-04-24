from django.shortcuts import render, redirect
from Veg_App.models import Recipe, Category
from django.contrib import messages

def RecipeView(request):
    if request.method=='POST':
        data = request.POST
        imagefile = request.FILES['imagefile']
        name = data.get('name')
        instruction = data.get('instruction')
        ingredients = data.get('ingredients')
        time_took = data.get('time_took')
        calory = data.get('calory')
        serving = data.get('serving')
        # category_name = data.get('category')

        # category, _ = Category.objects.get_or_create(name=category_name)

        Recipe.objects.create(
            name = name,
            instruction = instruction,
            imagefile = imagefile,
            ingredients = ingredients,
            time_took = time_took,
            calory = calory,
            serving = serving,
            # category_ref = category
        )
        messages.success(request, 'Recipe added successfully!')
        return redirect('/recipe/')

    # context['name'] = Category.get_name_display()

    queryset = Recipe.objects.all()
    # categories = Category.objects.all()
    context = {'recipe': queryset} #, 'categories': categories}

    return render(request, 'recipe.html', context)

def All_recipe(request):
    queryset = Recipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains = request.GET.get('search'))

    context = {'recipe': queryset}
    return render(request, 'all_recipe.html', context)

def Delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    messages.success(request, 'Recipe deleted successfully!')
    return redirect('/all-recipe/')

def Update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST

        name = data.get("name")
        instruction = data.get("instruction")
        imagefile = request.FILES.get('imagefile')
        ingredients = data.get('ingredients')
        time_took = data.get('time_took')
        calory = data.get('calory')
        serving = data.get('serving')

        queryset.name = name
        queryset.instruction = instruction
        queryset.ingredients = ingredients
        queryset.time_took = time_took
        queryset.calory = calory
        queryset.serving = serving

        if imagefile:
            queryset.imagefile = imagefile

        queryset.save()
        return redirect('/all-recipe/')
    messages.success(request, 'Recipe updated successfully!')
        
    context = {'recipe': queryset}
    
    return render(request, 'update.html', context)


def DemoView(request):
    data=[
        {'name' : 'deeppriya', 'age' : 20},
          {'name' : 'gupta', 'age': 22},
          {'name' : 'deep', 'age': 21},
          {'name' : 'priya', 'age': 23}
    ]

    return render(request, 'demo.html', context={'data':data})