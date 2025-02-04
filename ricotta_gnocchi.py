from pasta_recipe import PastaRecipe

# 🧀 Ricotta Gnocchi Recipe
ricotta_gnocchi = PastaRecipe(
    name="Ricotta Gnocchi",
    ingredients={
        "flour": {"quantity": ".75-1 cup", "emoji": "🌾"},
        "ricotta cheese": {"quantity": "15 oz", "emoji": "🧀"},
        "eggs": {"quantity": "2 eggs", "emoji": "🥚"},
        "parmesan cheese": {"quantity": "1.25 cups", "emoji": "🧀"},
        "black pepper": {"quantity": "to taste", "emoji": "🌶️"},
        "butter": {"quantity": "3 tablespoons", "emoji": "🧈"},
        "salt": {"quantity": "a pinch", "emoji": "🧂"},
        "sage leaves": {"quantity": "10 or more", "emoji": "🍃"}
    },
    recipe_steps=[
        {"action": "Boil water", "time": 10, "temperature": 100},
        {"action": "Combine ricotta, eggs, Parmesan, salt, and pepper in a bowl", "time": 1},
        {"action": "Add 1/2 cup flour, stir, add more flour until dough forms, boil dough to test that it holds it's shape", "time": 3},
        {"action": "Heat butter in skillet, add sage, add ricotta mixture into water in rotations", "time": 15, "temperature": 100},
        {"action": "Wait for gnocchi to rise to surface, remove and transfer to skillet", "time": 10},
        {"action": "Toss, taste, and adjust seasoning", "time": 5},
        {"action": "Serve immediately", "time": 2}
    ],
    available_ingredients=["flour", "ricotta cheese", "eggs", "parmesan cheese", "black pepper", "butter", "salt", "sage leaves"]
)
