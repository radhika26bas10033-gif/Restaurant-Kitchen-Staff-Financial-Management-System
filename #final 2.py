#final 2.0
# ==========================================
# FILE 1: Pantry Management Module
# ==========================================

def manage_pantry(pantry_set):
    """Adds or views ingredients in the kitchen pantry set."""
    print("\n--- Kitchen Pantry Management ---")
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


# ==========================================
# FILE 2: Recipe & Shopping List Module
# ==========================================

recipes_db = {
    "burger": {"bun", "patty", "cheese", "lettuce"},
    "pasta": {"pasta", "sauce", "cheese", "garlic"},
    "coffee": {"coffee beans", "milk", "sugar"}
}

def check_cookable_recipes(pantry_set, shopping_list):
    """Uses set subset checks to find cookable recipes; sends missing items to shopping list."""
    print("\n--- Recipe Availability & Smart Shopping ---")
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
        print(f"✅ Success! You have all ingredients to cook {target.capitalize()}.")
    else:
        print(f"⚠️ Missing ingredients for {target.capitalize()}: {list(missing)}")
        for item in missing:
            if item not in shopping_list:
                shopping_list.append(item)
        print("Missing items have been automatically sent to your Shopping List!")


# ==========================================
# FILE 3: Staff & Payroll Module
# ==========================================

def add_employee(employees_db):
    """Adds a staff member profile into the employee dictionary."""
    print("\n--- Add Staff Member ---")
    emp_id = input("Enter Employee ID (e.g., E01): ").strip()
    if emp_id in employees_db:
        print("Error: Employee ID already exists.")
        return
        
    name = input("Enter Full Name: ").strip()
    dept = input("Enter Department (Kitchen/Service): ").strip().lower()
    try:
        base_pay = float(input("Enter Base Salary: "))
    except ValueError:
        print("Error: Invalid salary amount.")
        return
        
    employees_db[emp_id] = {'name': name, 'dept': dept, 'base_pay': base_pay}
    print(f"Success: Staff member {name} added!")

def process_payroll(employees_db, expense_logs):
    """Computes payroll and logs it as an expense."""
    print("\n--- Process Staff Payroll ---")
    emp_id = input("Enter Employee ID: ").strip()
    if emp_id not in employees_db:
        print("Error: Employee ID not found.")
        return
        
    emp = employees_db[emp_id]
    try:
        bonus = float(input("Enter Bonus: "))
        deductions = float(input("Enter Deductions: "))
    except ValueError:
        print("Error: Invalid number entries.")
        return
        
    net_salary = emp['base_pay'] + bonus - deductions
    expense_logs.append({'category': 'payroll', 'amount': net_salary, 'desc': f"Salary for {emp['name']}"})
    
    print(f"\nPayslip Generated for {emp['name']} | Net Pay: ${net_salary:.2f} (Logged as expense)")


# ==========================================
# FILE 4: Budget & Finance Tracking Module
# ==========================================

budget_limit = 5000.0

def view_shopping_list_and_buy(shopping_list, expense_logs):
    """Displays shopping list, calculates estimated costs, and logs expenses."""
    global budget_limit
    print("\n--- Shopping List & Expense Checkout ---")
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
            print(f"⚠️ Warning: This purchase exceeds your total budget limit of ${budget_limit}!")
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
    
    print(f"Total Budget Limit: ${budget_limit:.2f}")
    print(f"Total Spent So Far: ${total_spent:.2f}")
    if total_spent > budget_limit:
        print("❌ Status: Over Budget!")
    else:
        print(f"✅ Status: Within Budget. Remaining: ${remaining:.2f}")
        
    print("\nExpense History:")
    for i, exp in enumerate(expense_logs, start=1):
        print(f"{i}. Category: {exp['category'].capitalize()} | Cost: ${exp['amount']:.2f}")


# ==========================================
# FILE 5: Main Controller Entry Point File
# ==========================================

# In-memory Shared Data Structures
pantry_set = set()
employees_db = {}
shopping_list = []
expense_logs = []

def main():
    while True:
        print("\n=== Restaurant Management & Budget System ===")
        print("1. Manage Pantry Stock")
        print("2. Check Recipe & Generate Shopping List")
        print("3. View Shopping List & Checkout Expenses")
        print("4. Check Budget Status & History")
        print("5. Add Staff Member")
        print("6. Process Staff Payroll")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ").strip()
        
        if choice == '1':
            manage_pantry(pantry_set)
        elif choice == '2':
            check_cookable_recipes(pantry_set, shopping_list)
        elif choice == '3':
            view_shopping_list_and_buy(shopping_list, expense_logs)
        elif choice == '4':
            check_budget_status(expense_logs)
        elif choice == '5':
            add_employee(employees_db)
        elif choice == '6':
            process_payroll(employees_db, expense_logs)
        elif choice == '7':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid selection. Choose between 1 and 7.")

if __name__ == "__main__":
    main()