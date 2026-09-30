# Main Controller Entry Point File
from pantry_module import manage_pantry
from recipe_module import check_cookable_recipes
from staff_module import add_employee, process_payroll
from finance_module import view_shopping_list_and_buy, check_budget_status

# In-memory Shared Data Structures
pantry_set = set()
employees_db = {}
shopping_list = []
expense_logs = []

def main():
    while True:
        print("\nRestaurant Management & Budget System ")
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