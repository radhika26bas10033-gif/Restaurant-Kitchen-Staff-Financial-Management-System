# Budget & Finance Tracking Module

budget_limit = 5000.0

def view_shopping_list_and_buy(shopping_list, expense_logs):
    """Displays shopping list, calculates estimated costs, and logs expenses."""
    global budget_limit
    print("\n-- Shopping List & Expense Checkout --")
    if not shopping_list:
        print("Shopping list is empty. No items to buy.")
        return
        
    print("Current Shopping List Items:", shopping_list)
    confirm = input("Do you want to purchase these items and log expenses? (y/n): ").strip().lower()
    
    if confirm == 'y':
        try:
            cost = float(input("Enter total purchase cost for these items: "))
        except ValueError:
            print("Error: Invalid cost entered.")
            return
            
        total_spent = sum(e['amount'] for e in expense_logs)
        if (total_spent + cost) > budget_limit:
            print(f"Warning: This purchase exceeds your total budget limit of Rs{budget_limit}!")
            proceed = input("Proceed anyway? (y/n): ").strip().lower()
            if proceed != 'y':
                return
                
        expense_logs.append({'category': 'procurement', 'amount': cost, 'desc': list(shopping_list)})
        shopping_list.clear()
        print(f"Success! Expense of ${cost:.2f} logged and shopping list cleared.")

def check_budget_status(expense_logs):
    """Tracks spending against the total budget limit using dictionaries and lists."""
    print("\n--- Budget Status Report ---")
    total_spent = sum(e['amount'] for e in expense_logs)
    remaining = budget_limit - total_spent
    
    print(f"Total Budget Limit: Rs{budget_limit:.2f}")
    print(f"Total Spent So Far: Rs{total_spent:.2f}")
    if total_spent > budget_limit:
        print(" Status: Over Budget!")
    else:
        print(f"Status: Within Budget. Remaining: Rs{remaining:.2f}")
        
    print("\nExpense History:")
    for i, exp in enumerate(expense_logs, start=1):
        print(f"{i}. Category: {exp['category'].capitalize()} | Cost: Rs    {exp['amount']:.2f}")