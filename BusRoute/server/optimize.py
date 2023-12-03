from scipy.optimize import minimize
from main import reductionAverage

# The function to minimize (negative of what we want to maximize)
def f(x,y):
    return -reductionAverage(x,y)

init = [2, 1440]

res = minimize(f, init, method='L-BFGS-B')

print("Optimized Parameters:", result.x) 
print("Maximized Value:", -result.fun)  # Negate the result.fun for maximization