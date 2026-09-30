# Pantry Management Module

def manage_pantry(pantry_set):
    """Adds or views ingredients in the kitchen pantry set."""
    print("\nKitchen Pantry Management")
    print("1. View Pantry Stock")
    print("2. Restock Pantry Ingredients")
    choice = input("Choose option (1-2): ").strip()
    
    if choice == '1':
        print("\nCurrent Pantry Stock:", list(pantry_set) if pantry_set else "Pantry is empty.")
    elif choice == '2':
        items_input = input("Enter ingredients separated by commas: ").lower()
        items = [i.strip() for i in items_input.split(',')]
        for item in items:
            pantry_set.add(item)  # Sets automatically eliminate duplicates
        print("Pantry successfully restocked!")
    else:
        print("Invalid choice.")