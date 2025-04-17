import numpy as np
import matplotlib.pyplot as plt

# Define the function (example: f(x) = x^3 - x - 2)
def f(x):
    return x**3 - x - 2

# Random probe to find initial interval where f(a)*f(b) < 0
a, b = np.random.uniform(-10, 10, 2)
while f(a) * f(b) > 0:
    a, b = np.random.uniform(-10, 10, 2)

# Bisection method
tolerance = 1e-6
iterations = []
while abs(b - a) > tolerance:
    c = (a + b) / 2
    iterations.append([a, b, c, f(c)])
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

results = np.array(iterations)

# Plotting
x_vals = np.linspace(results[0,0], results[0,1], 400)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='black', linewidth=0.5)

for i, row in enumerate(results):
    plt.plot(row[2], f(row[2]), 'ro')
    plt.text(row[2], f(row[2]), f'{i}', fontsize=8)

plt.title('Bisection Method Root Finding')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
