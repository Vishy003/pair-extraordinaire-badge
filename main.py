import numpy as np

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_fibonacci(n):
    """Generate the first N Fibonacci numbers."""
    fib_series = [0, 1]
    for _ in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

def factorial(n):
    """Calculate factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def matrix_multiplication(A, B):
    """Perform matrix multiplication using NumPy."""
    return np.dot(A, B)

def main():
    print("\n--- Advanced Computational Program ---")
    
    # Prime Number Check
    num = 29
    print(f"Is {num} a prime number? {'Yes' if is_prime(num) else 'No'}")
    
    # Fibonacci Sequence
    n_terms = 10
    print(f"First {n_terms} Fibonacci numbers: {generate_fibonacci(n_terms)}")
    
    # Factorial Calculation
    fact_num = 5
    print(f"Factorial of {fact_num}: {factorial(fact_num)}")
    
    # Matrix Multiplication
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print("\nMatrix A:\n", A)
    print("Matrix B:\n", B)
    print("Matrix Multiplication Result:\n", matrix_multiplication(A, B))

if __name__ == "__main__":
    main()
