def power_series_exp(x, terms):
    result = sum((x ** n) / (1 if n == 0 else n * factorial(n)) for n in range(terms))
    return result

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

if __name__ == "__main__":
    x = float(input("Enter the value of x: "))
    terms = int(input("Enter the number of terms: "))
    print(f"e^{x} ≈ {power_series_exp(x, terms)}")
