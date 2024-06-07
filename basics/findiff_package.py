# Define the inner and outer functions
def g(x):
    return np.sin(x)

def f(u):
    return np.exp(u)

# Composite function
def composite_func(x):
    return f(g(x))

# Compute the derivative using the chain rule at a point, say x=1
x_val = 1.0
dx = 1e-6
d_dx = FinDiff(0, dx, 1)

# Compute derivatives of inner and outer functions
inner_derivative = d_dx(g)(x_val)
outer_derivative = d_dx(f)(g(x_val))
chain_derivative = outer_derivative * inner_derivative

print("Composite Function: f(g(x)) = exp(sin(x))")
print(f"Chain Rule Derivative at x = {x_val}: dy/dx =", chain_derivative)


# Define the function
def f(x):
    return np.sin(x)

# Compute the first, second, and third derivatives at a point, say x=1
x_val = 1.0
dx = 1e-6
d_dx = FinDiff(0, dx, 1)
d2_dx2 = FinDiff(0, dx, 2)
d3_dx3 = FinDiff(0, dx, 3)

f_prime = d_dx(f)(x_val)
f_double_prime = d2_dx2(f)(x_val)
f_triple_prime = d3_dx3(f)(x_val)

print("Function: f(x) = sin(x)")
print(f"First Derivative at x = {x_val}: f'(x) =", f_prime)
print(f"Second Derivative at x = {x_val}: f''(x) =", f_double_prime)
print(f"Third Derivative at x = {x_val}: f(triple dash)(x) = ", f_triple_prime)