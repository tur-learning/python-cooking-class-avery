from pasta_recipe import PastaRecipe

# 🌿 Arrabbiata Recipe
arrabbiata = PastaRecipe(
    name="Arrabbiata",
    ingredients={
        "pasta": {"quantity": "340g", "emoji": "🍝"},
        "fresh basil": {"quantity": "5g", "emoji": "🍃"},
        "garlic": {"quantity": "4 cloves", "emoji": "🧄"},
        "parmesan cheese": {"quantity": "30g", "emoji": "🧀"},
        "chopped parsley": {"quantity": "15g", "emoji": "🌿"},
        "olive oil": {"quantity": "60ml", "emoji": "🫒"},
        "salt and pepper": {"quantity": "to taste", "emoji": "🧂"}
        "red chili": {"quantity": "5ml", "emoji": "🌶️"}
        "canned tomatoes": {"quantity": "800g", "emoji": "🍅"}
    },
    recipe_steps=[
        {"action": "Boil water", "time": 10, "temperature": 100},
        {"action": "Cook pasta", "time": 10, "temperature": 90},
        {"action": "Heat olive oil and add garlic", "time": 0.5},
        {"action": "Add red chili and canned tomatoes", "time": 20},
        {"action": "Stir in basil and parsley", "time": 2},
        {"action": "Combine with pasta, add salt and pepper, grate parmesan", "time": 1}
    ],
    available_ingredients=["pasta", "fresh basil", "garlic", "parmesan cheese", "olive oil", "salt and pepper"]
)
