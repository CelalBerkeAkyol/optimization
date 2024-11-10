import sympy as sp

def gradient_descent(function, x0, learning_rate=0.1, max_iter=1000, tolerance=1e-6):
    """
    Gradient Descent Implementation
    :param function: Sympy symbolic function (f(x))
    :param x0: Initial guess
    :param learning_rate: Step size (default=0.1)
    :param max_iter: Maximum number of iterations (default=100)
    :param tolerance: Convergence tolerance (default=1e-6)
    :return: Approximate minimum point or error message
    """
    x = sp.symbols('x')  # Define symbol
    f_prime = sp.diff(function, x)  # Compute derivative of the function

    steps = []  # To store each step

    for i in range(max_iter):
        f_prime_x = f_prime.subs(x, x0)  # Evaluate derivative at current x0
        
        # Update step: Gradient Descent formula
        x1 = x0 - learning_rate * f_prime_x
        
        steps.append((x0, f_prime_x, x1))  # Save current step
        
        # Check convergence
        if abs(x1 - x0) < tolerance:
            return x1, steps
        
        x0 = x1  # Update x0 for next iteration

    return f"Did not converge after {max_iter} iterations", steps

# Example usage:
x = sp.symbols('x')
f = (x+5)**2  # Define a simple convex function
minimum, steps = gradient_descent(f, x0=-5, learning_rate=0.1)

print("Minimum point:", minimum)
