from pasta_recipe import PastaRecipe

# 🌿 Amatriciana Recipe
amatriciana = PastaRecipe(
    name="Amatricana",
    ingredients={       #Change
        "pasta": {"quantity": "500g", "emoji": "🍝"},
        "guanciale": {"quantity": "250g", "emoji": "🥓"},
        "parmesan cheese": {"quantity": "120g", "emoji": "🧀"},
        "white wine": {"quantity": "120ml", "emoji": "🍷"},
        "salt": {"quantity": "to taste", "emoji": "🧂"},
        "pepper flakes": {"quantity": "5ml", "emoji": "🌶️"},
        "canned tomatoes": {"quantity": "500g", "emoji": "🍅"}
    },
    recipe_steps=[
        {"action": "Boil water", "time": 10, "temperature": 100},
        {"action": "Cook pasta", "time": 10, "temperature": 90},
        {"action": "Brown guanciale in pan, then remove", "time": 3},
        {"action": "Add pepper flakes, canned tomatoes, white wine, and salt", "time": 15},
        {"action": "Add pasta", "time": 2},
        {"action": "Re-add guanciale, add parmesean cheese", "time": 1}
    ],
    available_ingredients=["pasta", "parmesan cheese", "salt", "canned tomatoes"]
)
