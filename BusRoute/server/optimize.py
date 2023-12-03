from scipy.optimize import minimize
from main import reductionAverage
from main import getRoutes

# The function to minimize (negative of what we want to maximize)
def f(x,y):
    return -reductionAverage(x,y)

# Returns the best route as a sequence of stops
def opt():
    init = [2, 1440]
    res = minimize(f, init, method='L-BFGS-B')
    return getRoutes(result.x[0], result.x[1])