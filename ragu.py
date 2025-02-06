from pasta_recipe import PastaRecipe

# 🍝 Ragu Recipe
ragu = PastaRecipe(
    name="Ragu Bolognese",
    ingredients={
        "pasta": {"quantity": "200g", "emoji": "🍝"},
        "ground beef": {"quantity": "450g", "emoji": "🥩"},
        "tomato sauce": {"quantity": "1 jar", "emoji": "🍅"},
        "parmesan cheese": {"quantity": "50g", "emoji": "🧀"},
        "salt": {"quantity": "a pinch", "emoji": "🧂"}
    },
    recipe_steps=[
        {"action": "Boil water", "time": 10, "temperature": 100},
        {"action": "Cook pasta", "time": 10, "temperature": 90},
        {"action": "Cook beef", "time": 5, "temperature": 90},
        {"action": "Mix tomato sauce and parmesan cheese into beef", "time": 2},
        {"action": "Let simmer", "time": 15, "temperature": 80},
        {"action": "Combine with pasta", "time": 1}
    ],
    available_ingredients=["pasta", "ground beef", "tomato sauce", "parmesan cheese", "salt"]
)
