from pasta_recipe import PastaRecipe

# 🎭 Carbonara Recipe
orechiette = PastaRecipe(
    name="Orecchiette con Cime di Rapa",
    ingredients={
        "orecchiette pasta": {"quantity": "1kg", "emoji": "🍝"},
        "cime di rapa": {"quantity": "1 kg", "emoji": "🥬"},
        "breadcrumbs": {"quantity": "50g", "emoji": "🍞"},
        "fine salt": {"quantity": "to taste", "emoji": "🧂"},
        "garlic cloves": {"quantity": "1", "emoji": "🧄️"},
        "anchovies": {"quantity": "3 fillets", "emoji": "🐟"},
        "extra virgin olive oil": {"quantity": "30g", "emoji": "🌿"},
        "water": {"quantity": "100g", "emoji": "💧"},
    },

    recipe_steps=[
        {"action": "Prepare cime di rapa(wash and cut)", "time": 3, "temperature": 22},
        {"action": "Fry readcrumbs in half the oil", "time": 3, "temperature": 90},
        {"action": "Boil cime di rapa in water", "time": 5, "temperature": 100},
        {"action": "Sauté crushed garlic clove and anchovies in rest of oil", "time": 2, "temperature": 90},
        {"action": "Boil orecchiette with the cime di rapa", "time": 5, "temperature": 100},
        {"action": "Combine the sauté, breadcrumbs, cime di rapa, salt, olive oil, and orecchiette", "time" : 1},
    ],
    available_ingredients=["orecchiette pasta", "cime di rapa", "breadcrumbs", "garlic cloves", "anchovies", 
                           "extra virgin olive oil", "fine salt", "water"]
)