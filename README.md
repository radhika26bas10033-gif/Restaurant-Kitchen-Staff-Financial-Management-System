# Restaurant-Kitchen-Staff-Financial-Management-System
Key Features
Kitchen Pantry Management (set): Track current raw ingredient inventory. Uses Python sets to automatically enforce uniqueness and prevent duplicate entries.

Smart Recipe Matcher (set & list): Check recipe feasibility using set subset operations. If any ingredients are missing, they are automatically queued into an organized shopping list.

Budget & Expense Tracking (list & dict): Checkout shopping lists, log procurement costs, and continuously monitor expenses against a global budget ceiling with built-in over-budget warnings.

Staff & Payroll Management (dict): Register staff profiles with unique identification keys, compute net monthly salaries (factoring in bonuses and deductions), and seamlessly sync payouts into the financial expense ledger.


Project Structure
The project is combined into a single, easy-to-run script or can be separated into functional modules:

manage_pantry() - Handles inventory updates.

check_cookable_recipes() - Performs set-based recipe matching and shopping list generation.

view_shopping_list_and_buy() - Manages procurement checkout and budget limits.

process_payroll() - Computes staff compensation and logs financial outflows.

main() - Provides the interactive control dashboard loop.




 Academic Context
Developed as part of a foundational programming project focusing on practical algorithmic logic and data structure implementation.
