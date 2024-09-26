def add(a, b):
    """Function to add two numbers."""
    return a + b

def multiply(a, b):
    """Function to multiply two numbers."""
    return a * b


if __name__ == "__main__":
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        

        sum_result = add(num1, num2)
        product_result = multiply(num1, num2)

        
        print(f"The sum of {num1} and {num2} is: {sum_result}")
        print(f"The product of {num1} and {num2} is: {product_result}")

    except ValueError:
        print("Please enter valid numbers.")
