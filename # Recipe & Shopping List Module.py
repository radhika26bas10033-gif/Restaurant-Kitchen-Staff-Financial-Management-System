# Recipe & Shopping List Module

recipes_db = {
    "burger": {"bun", "patty", "cheese", "lettuce"},
    "pasta": {"pasta", "sauce", "cheese", "garlic"},
    "coffee": {"coffee beans", "milk", "sugar"}
}

def check_cookable_recipes(pantry_set, shopping_list):
    """Uses set subset checks to find cookable recipes; sends missing items to shopping list."""
    print("\n-- Recipe Availability & Smart Shopping --")
    if not pantry_set:
        print("Pantry is empty! Restock items first.")
        return
    
    print("Available Recipes:", list(recipes_db.keys()))
    target = input("Enter the recipe you want to check/cook: ").lower().strip()
    
    if target not in recipes_db:
        print("Recipe not found.")
        return
        
    required = recipes_db[target]
    missing = required - pantry_set  # Set difference to find missing ingredients
    
    if not missing:
        print(f"Success! You have all ingredients to cook {target.capitalize()}.")
    else:
        print(f"Missing ingredients for {target.capitalize()}: {list(missing)}")
        for item in missing:
            if item not in shopping_list:
                shopping_list.append(item)
        print("Missing items have been automatically sent to your Shopping List!")