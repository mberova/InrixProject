from scipy.optimize import minimize_scalar
from main import reductionAverage
from main import getRoutes
import math

t0 = 0 # should be user input
# The function to minimize (negative of what we want to maximize)
def f(x):
    return -reductionAverage(x, t0)

# Returns the best route as a sequence of stops
def opt():
    print("in opt")
    init = [2, 1440]
    res = minimize_scalar(f)
    print(res.x, res.fun)
    return getRoutes(math.floor(res.x), t0)

opt()