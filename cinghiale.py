from pasta_recipe import PastaRecipe

# 🐗 Ragu' di Cinghiale Recipe
cinghiale = PastaRecipe(
    name="Ragu' di Cinghiale",
    ingredients={
        "pasta": {"quantity": "200g", "emoji": "🍝"},
        "Polpa di Cinghiale": {"quantity": "400g", "emoji": "🐗"},
        "onion": {"quantity": "1/2", "emoji": "🧅"},
        "peeled tomatoes": {"quantity": "300g", "emoji": "🍅"},
        "carrot": {"quantity": "1", "emoji": "🥕"},
        "olive oil": {"quantity": "60ml", "emoji": "🫒"},
        "laurel": {"quantity": "2 leaves", "emoji": "🌿"},
        "salt": {"quantity": "a pinch", "emoji": "🧂"}
    },
    recipe_steps=[
        {"action": "Boil water", "time": 10, "temperature": 100},
        {"action": "Cook pasta", "time": 10, "temperature": 90},
        {"action": "Put in a container Polpa di Cinghiale, Carrot, laurel, Onion", "time": 300},
        {"action": "Mix with peeled tomato, olive oil, salt", "time": 5},
        {"action": "Combine with pasta", "time": 1}
    ],
    available_ingredients=["pasta", "basil", "garlic", "parmesan cheese", "pine nuts", "olive oil", "salt"]
)
