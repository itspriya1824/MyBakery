orders = []
customers = set()
cake_sizes = ("0.5 kg", "1 kg", "2 kg")

def greet_customer():
    print("\nWelcome to My Bakery! ")

def add_order():
    try:
        customer = input("Enter customer name: ").strip()
        if not customer:
            print("Customer name cannot be empty!")
            return
        
        cake = input("Enter cake name: ").strip()
        if not cake:
            print("Cake name cannot be empty!")
            return
        
        print("Available cake sizes:", cake_sizes)

        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per cake: "))
        if quantity <= 0 or price < 0:
            print("Quantity must be positive and price cannot be negative!")
            return
        bill = quantity * price
        order = {
            "customer": customer,
            "cake": cake,
            "quantity": quantity,
            "price": price,
            "bill": bill}
        orders.append(order)
        customers.add(customer)
        print("Order added successfully!")
        print("Total bill:", bill)
    except ValueError:
            print("lnvalid input! Enter a whole number for quantity and a number for price.")   

def view_orders():
    if not orders:
        print("No orders available.")
        return
    for order in orders:
        print("\n-- Order Details --")
        print("Customer:", order["customer"])
        print("Cake:", order["cake"])
        print("quantity:",order["quantity"])
        print("Price per cake:" ,order["price"])
        print("bil:",order["bill"] )        

def search_customer():
    if not orders:
        print("No orders available.")
        return
    search_name = input("Enter customer name to search: ").strip()
    found = False
    for order in orders:
        if search_name.lower() == order["customer"].lower():
            print("\n order found!")
            print("Customer:", order["customer"])
            print("Cake:", order["cake"])
            print("Quantity:", order["quantity"])
            print("Bill:",order["bill"])
            found = True
    if not found:
        print("Customer not found!")

def calculate_sales():
    total_sales = 0
    for order in orders:
        total_sales += order["bill"] 
    print("Total sales:",total_sales) 

def show_customers():
    if not customers:
        print("No customers yet.")
    else:
        print("Unique customers:", customers)

greet_customer()

while True:
    print("\n==== My Bakery ====")        
    print("1. Add Order")
    print("2. View All Orders")
    print("3. Search Customer")
    print("4. Calculate Total Sales")
    print("5. Show Unique Customers")
    print("6. Exit")

    try:
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_order()

        elif choice =="2":
            view_orders()

        elif choice == "3":
           search_customer()

        elif choice == "4":
           calculate_sales()

        elif choice == "5":
            show_customers()

        elif choice == "6":
            print("Thank you for visiting My Bakery!")
            break

        else:
            print("lnvalid choice! Please select 1 to 6")

    except Exception as error:
        print("An unexpected error occurred:", error )       




