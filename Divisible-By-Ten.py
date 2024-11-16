def divisible_by_ten(num):
    """
    Determines whether a number is divisible by 10.

    Parameters:
        num (int): The number to check.

    Returns:
        bool: True if num is divisible by 10, False otherwise.
    """
    if num % 10 == 0:  # Check if the remainder of num divided by 10 is 0
        return True
    else:
        return False

# Example usage:
number = int(input("Enter a number: "))
result = divisible_by_ten(number)

if result:
    print(f"{number} is divisible by 10.")
else:
    print(f"{number} is not divisible by 10.")
