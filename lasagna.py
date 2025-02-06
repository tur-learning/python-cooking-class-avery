from pasta_recipe import PastaRecipe

# 🥘 Lasagna Recipe

lasagna = PastaRecipe(
    name="Lasagna",
    ingredients = {
        'Lasagna Noodles': {'quantity': '12 sheets', 'emoji': '🍝'},
        'Ground Beef': {'quantity': '500g', 'emoji': '🥩'},
        'Tomato Sauce': {'quantity': '2 cups', 'emoji': '🍅'},
        'Cheese': {'quantity': '200g', 'emoji': '🧀'},
        'Garlic': {'quantity': '2 cloves', 'emoji': '🧄'}
    },

    recipe_steps=[
        {"action": "Boil lasagna noodles", "time": 10, "temperature": "High"},
        {"action": "Cook ground beef with garlic and spices", "time": 8, "temperature": "Medium"},
        {"action": "Layer sauce, noodles, and cheeses in a baking dish", "time": 5},
        {"action": "Bake in oven", "time": 30, "temperature": "180°C"}
    ],
    available_ingredients=["Lasagna noodles", "Ground beef", "Tomato sauce", "Cheese", "Garlic", "Salt", "Pepper"]
)
