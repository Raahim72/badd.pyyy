def is_natural_number(num):
    
    if isinstance(num, int) and num > 0:
        return True
    return False


user_input = input("Enter a number: ")

try:
    number = int(user_input) 
    if is_natural_number(number):
        print(f"{number} is a natural number.")
    else:
        print(f"{number} is not a natural number.")
except ValueError:
    print("Please enter a valid integer.")
