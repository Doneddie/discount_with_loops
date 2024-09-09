

def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    Parameters:
    - price (float): The original price of the item.
    - discount_percent (float): The discount percentage to apply.

    Returns:
    - float: The final price after applying the discount, or the original price if discount is below 20%.
    """
    # Check if the discount is 20% or more
    if discount_percent >= 20:
        # Calculate the discounted price
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return the original price if discount is less than 20%
        return price

# Prompt user for input
try:
    # Get the original price from the user
    original_price = float(input("Enter the original price of the item: "))
    
    # Get the discount percentage from the user
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate the final price using the calculate_discount function
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Print the final price or the original price
    if discount_percentage >= 20:
        print(f"Discount applied. The final price is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
        
except ValueError:
    print("Please enter valid numerical values for price and discount percentage.")
