def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

print("=== Discount Calculator ===")
try:
    # Get user input
    original_price = float(input("Enter the original price of the item: $"))
    discount_percent = float(input("Enter the discount percentage (0-100): "))
    
    # Validate inputs
    if original_price < 0:
        print("Error: Price cannot be negative!")
    elif discount_percent < 0 or discount_percent > 100:
        print("Error: Discount must be between 0-100%!")
    else:
        # Calculate final price
        final_price = calculate_discount(original_price, discount_percent)
        
        # Display results
        print("\n" + "="*30)
        print(f"Original Price: ${original_price:.2f}")
        print(f"Discount Percentage: {discount_percent}%")
        
        if discount_percent >= 20:
            discount_amount = original_price * (discount_percent / 100)
except ValueError:
    print("Error: Please enter a valid number for price and discount percentage.")

    
    