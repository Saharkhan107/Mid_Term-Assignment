# customer_order_management.py
# Author: [Sahar Iqbal]
# Date: [10/19/2024]
# This program manages customer orders for a small business, allowing for customer information 
# management, product ordering, discounts, tax calculations, and order storage.

import re

def validate_phone(phone):
    """Validates the phone number format."""
    pattern = re.compile(r'^\(\d{3}\) \d{3}-\d{4}$|^\d{3}-\d{3}-\d{4}$')
    return bool(pattern.match(phone))

def validate_email(email):
    """Validates the email address format."""
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(pattern.match(email))

def input_customer_info():
    """Prompts the user for customer information and validates the input."""
    name = input("Enter the customer's name: ")
    
    # Validate phone number
    while True:
        phone = input("Enter the customer's phone number (format: (123) 456-7890 or 123-456-7890): ")
        if validate_phone(phone):
            break
        print("Invalid phone number format. Please try again.")

    # Validate email address
    while True:
        email = input("Enter the customer's email address: ")
        if validate_email(email):
            break
        print("Invalid email format. Please try again.")
    
    return {"name": name, "phone": phone, "email": email}

def display_product_list(products):
    """Displays the list of available products."""
    print("\nAvailable Products:")
    for product in products:
        print(f"ID: {product['id']}, Name: {product['name']}, Price: ${product['price']:.2f}")

def calculate_total_cost(orders, products, delivery):
    """Calculates the total cost of the order, applying discounts and tax."""
    total_cost = sum(products[int(pid) - 1]['price'] * qty for pid, qty in orders.items())
    
    # Apply discount if applicable
    if total_cost > 100:
        total_cost *= 0.9  # 10% discount

    # Add tax
    total_cost *= 1.0825  # 8.25% tax
    
    # Add delivery fee if applicable
    if delivery:
        total_cost += 10  # Flat delivery fee

    return total_cost

def save_order_to_file(customer_info, orders, final_amount):
    """Saves the order details to a text file."""
    with open("customer_orders.txt", "a") as file:
        file.write(f"Customer: {customer_info['name']}, Phone: {customer_info['phone']}, Email: {customer_info['email']}\n")
        file.write("Orders:\n")
        for product_id, quantity in orders.items():
            file.write(f"Product ID: {product_id}, Quantity: {quantity}\n")
        file.write(f"Final Amount: ${final_amount:.2f}\n\n")

def main():
    """Main function to control the program flow."""
    products = [
        {"id": "1", "name": "Car floor Mats", "price": 25.00},
        {"id": "2", "name": "Gadget", "price": 15.00},
        {"id": "3", "name": "Headphone", "price": 50.00},
        {"id": "4", "name": "Pillow", "price": 30.00},
        {"id": "5", "name": "Mobile Cover", "price": 10.00},
    ]
    
    customer_info = input_customer_info()
    
    display_product_list(products)
    
    orders = {}
    while True:
        product_id = input("Enter the product ID to order (or 'done' to finish): ")
        if product_id.lower() == 'done':
            break
        quantity = input(f"Enter the quantity for product ID {product_id}: ")
        
        if quantity.isdigit() and int(quantity) > 0:
            orders[product_id] = int(quantity)
        else:
            print("Invalid quantity. Please enter a positive integer.")

    delivery_choice = input("Would you like delivery (y/n)? ").lower() == 'y'
    
    final_amount = calculate_total_cost(orders, products, delivery_choice)
    
    print(f"\nCustomer: {customer_info['name']}")
    print(f"Final amount (including tax and delivery if applicable): ${final_amount:.2f}")
    
    # Save the order to a file
    save_order_to_file(customer_info, orders, final_amount)
    print("Order has been saved.")

if __name__ == "__main__":
    main()

