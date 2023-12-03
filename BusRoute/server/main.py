def getCongestionList(rad, c):
    # return a ORDERED list of congested areas within the given circle using API
    return None

def getRoutes(x, t):
    # choose x most congested stops from list at given time t
    # return the best routes between the stops
    # 0-1, 1-2, ..., n-0
    # should have travel times with congestion and with congestion
    # add 30 seconds to each no congestion travel time to account for stopping for passengers
    return None

def reductionAverage(x, t):
    routes = getRoutes(x, t)
    sum = 0
    weight = 0
    for s in x:
        sum += routes[s][1]*(1-(routes[s][0])/(routes[s][1]))
        weight += routes[s][1]
    return sum/weight

# Returns the best number of stops to reduce congestion (percentage) for the given time
def bestReductionForTime(t):
    maxReduction = 0
    bestAmount = 2
    for i in range(2, 30): # fix the range, make it the cap on the # of stops
        cur = reductionAverage(i, t)
        if cur > max: 
            maxReduction = cur
            bestAmount = i
    return [bestAmount, maxReduction]

# Returns the optimal sequence of bus routes
def bestRoutes():
    bestReduction = 0
    bestStops = 2
    bestTime = 0
    for i in range(5): # fix the range, make it the intervals of time
        cur = bestReductionForTime(i)
        if cur[1] > bestReduction:
            bestReduction = cur[1]
            bestStops = cur[0]
            bestTime = i
    return getRoutes(bestStops, bestTime)