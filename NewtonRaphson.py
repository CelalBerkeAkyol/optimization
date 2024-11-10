from sympy import symbols, diff

def newton_raphson(function, x0, max_iter=100, tolerance=1e-6):
    """
    Newton-Raphson Method Implementation
    :param function: Sympy symbolic function (f(x))
    :param x0: Initial guess
    :param max_iter: Maximum number of iterations (default=100)
    :param tolerance: Convergence tolerance (default=1e-6)
    :return: Approximate root or error message
    """
    x = symbols('x')  # Define symbol
    f_prime = diff(function, x)  # Calculate the derivative

    for i in range(max_iter):
        f_x = function.subs(x, x0)  # Evaluate f(x)
        f_prime_x = f_prime.subs(x, x0)  # Evaluate f'(x)

        if f_prime_x == 0:
            return f"Iteration stopped: derivative is zero at x = {x0}"

        # Newton-Raphson formula
        x1 = x0 - f_x / f_prime_x

        # Check convergence
        if abs(x1 - x0) < tolerance:
            return f"Root found: x = {x1}, after {i + 1} iterations"

        x0 = x1  # Update for the next iteration

    return f"Did not converge after {max_iter} iterations"

# Example usage:
x = symbols('x')
f = x**3 - 3*x**2  # Define the function
result = newton_raphson(f, x0=3)  # Call the function with an initial guess
print(result)
