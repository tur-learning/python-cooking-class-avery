from pasta_recipe import PastaRecipe

# 🎭 Arrabiata Recipe
arrabiata = PastaRecipe(
    name="Penne Arrabiata",
    ingredients={
        "penne rigate": {"quantity": "1kg", "emoji": "🍝"},
        "crushed red pepper flakes": {"quantity": "1/4 tsp", "emoji": "🥬"},
        "canned whole peeled tomatoes": {"quantity": "28oz", "emoji": "🍅"},
        "fine salt": {"quantity": "to taste", "emoji": "🧂"},
        "garlic cloves": {"quantity": "3", "emoji": "🧄️"},
        "tomato paste": {"quantity": "2tbsp", "emoji": "🥫"},
        "extra virgin olive oil": {"quantity": "3tbsp", "emoji": "🫒"},
        "chopped basil leaves": {"quantity": "6", "emoji": "🌿"},
        "freshly grated parmesan cheese": {"quantity": "1/2 cup", "emoji": "🧀"},
        "fresh chopped parsley": {"quantity": "1/3 cup", "emoji": "☘️"},
    }, )
    recipe_steps=[
        {"action": "Cook pasta in a large pot of boiling water, according to package instructions, until tender", "time": 5, "temperature": 100},
        {"action": "Meanwhile, heat olive oil in a large skillet over medium heat. Add garlic and crushed red pepper; cook, stirring. ", "time": .5, "temperature": 50},
        {"action": "Add tomatoes, crushing them roughly with the back of a wooden spoon, and tomato paste", "time": 3, "temperature": 50},
        {"action": "Bring to a simmer over low heat and cook for 5-10 minutes. Remove from heat and add fresh chopped basil", "time": 10, "temperature": 50},
        {"action": "When pasta is cooked, drain the water and add it to the sauce. Toss well. Taste and add more red pepper flakes or salt and pepper, if needed.", "time": 5, "temperature": 50},
        {"action": "Serve immediately topped with a generous portion of grated pecorino or parmesan cheese and fresh chopped parsley.", "time" : 1},
    ],
    available_ingredients=["penne rigate", "crushed red pepper flakes", "canned whole peeled tomatoes", "garlic cloves", "fine salt", 
                           "extra virgin olive oil", "tomato paste", "chopped basil leaves", "freshly grated parmesan cheese", "fresh chopped parsley"]