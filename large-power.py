def test_power(base, exponent):
    """
    Test whether the result of base raised to the power of exponent is greater than 5000.

    Parameters:
        base (float): The base number.
        exponent (float): The exponent to which the base will be raised.

    Returns:
        bool: True if the result is greater than 5000, False otherwise.
    """
    result = base ** exponent  # Calculate the result of base raised to the power of exponent
    if result > 5000:
        return True
    else:
        return False

# Example usage:
base = float(input("Enter the base number: "))
exponent = float(input("Enter the exponent: "))

# Check if the result is greater than 5000
is_greater_than_5000 = test_power(base, exponent)

# Print the result
if is_greater_than_5000:
    print("The result is greater than 5000.")
else:
    print("The result is not greater than 5000.")
