def calculate_discount(price, discount_percent):
  """
  Calculates the final price after applying a discount.

  Args:
    price: The original price of the item.
    discount_percent: The discount percentage (e.g., 20 for 20%).

  Returns:
    The final price after the discount, or the original price if the discount is less than 20%.
  """
  # Check if the discount percentage is at least 20%
  if discount_percent >= 20:
    # Calculate the discount amount
    discount_amount = (discount_percent / 100) * price
    # Calculate the final price after applying the discount
    final_price = price - discount_amount
    # Return the final price
    return final_price
  else:
    # If the discount is less than 20%, return the original price
    return price


if __name__ == "__main__":
  # The code within this block only runs when the script is executed directly
  try:
    # Get the original price from the user and convert it to a float
    original_price = float(input("Enter the original price of the item: "))
    # Get the discount percentage from the user and convert it to a float
    discount_percentage = float(input("Enter the discount percentage: "))

    # Check if the entered values are valid (non-negative)
    if original_price < 0 or discount_percentage < 0:
      # Raise a ValueError if the input is invalid
      raise ValueError("Price and discount percentage must be non-negative.")

    # Calculate the final price using the calculate_discount function
    final_price = calculate_discount(original_price, discount_percentage)

    # Check if a discount was applied (discount_percentage >= 20)
    if discount_percentage >= 20:
      # Print the final price after the discount, formatted to two decimal places
      print(f"The final price after the discount is: ${final_price:.2f}")
    else:
      # Print that no discount was applied and show the original price
      print(f"No discount applied. The original price is: ${final_price:.2f}")

  # Handle ValueError exceptions (invalid input)
  except ValueError as e:
    # Print an error message indicating invalid input
    print(f"Invalid input: {e}")
    # Provide instructions to the user on how to correct the input
    print("Please enter valid numerical values for price and discount percentage.")
  # Handle any other unexpected exceptions
  except Exception as e:
    # Print a generic error message for unexpected errors
    print(f"An unexpected error occurred: {e}")
