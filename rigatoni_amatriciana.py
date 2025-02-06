from pasta_recipe import PastaRecipe

# 🎭 Rigatoni all'Amatriciana Recipe
Rigatoni_allAmatriciana = PastaRecipe(
    name="Rigatoni all'Amatriciana",
    ingredients={
        "pasta": {"quantity": "400g", "emoji": "🍝"},
        "tomatoes": {"quantity": "400g", "emoji": "🍅"},
        "bacon": {"quantity": "200g", "emoji": "🥓"},
        "onion": {"quantity": "40g", "emoji": "🧅"},
        "chili pepper": {"quantity": "a pinch", "emoji": "🌶️"},
        "pecorino romano cheese": {"quantity": "as much as you want", "emoji": "🧀"}
    },
    recipe_steps=[
        {"action": "Boil water", "time": 10, "temperature": 100},
        {"action": "Cook pasta", "time": 10, "temperature": 90},
        {"action": "Pan fry bacon", "time": 6, "temperature": 170},
        {"action": "Chop onions", "time": 2,},
        {"action": "Remove bacon and add onion to pan to sauté", "time": 3, "temperature": 150},
        {"action": "Chop tomatoes", "time": 2},
        {"action": "Add tomatoes to pan", "time": 10, "temperature": 130},
        {"action": "Add chili pepper to sauce", "time": 1},
        {"action": "Add bacon back to sauce", "time": 1},
        {"action": "Drain pasta and mix with sauce", "time": 2},
        {"action": "Toss pasta with sauce and add pecorino romano cheese", "time": 2},
    ],
    available_ingredients=["pasta", "tomatoes", "bacon", "pecorino romano", "onion", "chili pepper"]  # Missing black pepper
)
