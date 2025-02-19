from pasta_recipe import PastaRecipe

# 🎭 Cacio e Pepe Recipe
cacioepepe = PastaRecipe(
    name="Cacio e Pepe 🍝",
    ingredients={
        "pasta": {"quantity": "1 lb", "emoji": "🍝"},
        "olive oil": {"quantity": "6 tbsp", "emoji": "🫒"},
        "garlic": {"quantity": "2 cloves", "emoji": "🧄"},
        "pecorino cheese": {"quantity": "1 3/4 cups", "emoji": "🧀"},
        "black pepper": {"quantity": "2 tsp", "emoji": "🌶️"}
    },
    recipe_steps=[
        {"action": "Boil water", "time": 10, "temperature": 100},
        {"action": "Cook pasta, reserve 1 cup of pasta water", "time": 12, "temperature": 90},
        {"action": "In a large skillet, heat olive oil and cook garlic and pepper", "time": 2, "temperature": 170},
        {"action": "Add in cooked pasta and cheese", "time": 1},
        {"action": "Add 1/2 cup of the reserved pasta water and stir until cheese is melted", "time": 1},
        {"action": "If needed stir in more cooking water 1 tbsp at a time", "time": 1}
    ],
    available_ingredients=["pasta", "olive oil", "pecorino cheese", "black pepper"] 
)
