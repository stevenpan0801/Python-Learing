def eval_quadratic(a,b,c,x):
    """
    a, b, c: numerical values for the coefficients of a quadratic equation.
    x: numerical value at which to evaluate the quadratic.
    Returns the value of the quadratic a*x**2 + b*x + c.
    """
    return a*x**2 + b*x + c

print(eval_quadratic(1, 1, 1, 1))