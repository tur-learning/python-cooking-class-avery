from pasta_recipe import PastaRecipe

# Norma Recipe
norma = PastaRecipe(
    name="Norma",
    ingredients={
        "pasta": {"quantity": "120g", "emoji": "🍝"},
        "eggplants": {"quantity": "60g", "emoji": "🌿"},
        "garlic": {"quantity": "1 clove", "emoji": "🧄"},
        "tomato": {"quantity": "60g", "emoji": "🧀"},
        "basil": {"quantity": "10g", "emoji": "🌰"},
        "olive oil": {"quantity": "50ml", "emoji": "🫒"},
        "salt": {"quantity": "a pinch", "emoji": "🧂"}
    },
    recipe_steps=[
        {"action": "Boil water", "time": 20, "temperature": 100},
        {"action": "Cook pasta", "time": 13, "temperature": 90},
        {"action": "Cook fresh tomato", "time": 15},
        {"action": "Mix with olive oil and parmesan cheese", "time": 2},
        {"action": "Add eggplants and cook it", "time": 15}
        {"action": "Combine with pasta", "time": 1}
    ],
    available_ingredients=["pasta", "basil", "garlic", "fresh tomato", "eggplants", "olive oil", "salt"]
)
