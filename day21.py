def calculate_factorial(n):
    # Base case: 0! or 1! is always 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: n * (n - 1)!
    return n * calculate_factorial(n - 1)

# Testing the recursion puzzle
number = 5
factorial_result = calculate_factorial(number)
print("--- Puzzle 1: Recursion ---")
print(f"The factorial of {number} is: {factorial_result}")
