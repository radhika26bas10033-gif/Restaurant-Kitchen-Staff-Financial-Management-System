# Staff & Payroll Module

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
    
    print(f"\nPayslip Generated for {emp['name']} | Net Pay: Rs{net_salary:.2f} (Logged as expense)")