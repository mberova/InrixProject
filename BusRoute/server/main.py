RAD = 5 # radius given by client
C = [10,50] # lat/long given by client

def getCongestionList(t):
    # return a ORDERED list of congested areas within the given circle using API, at time t
    return None

## TODO: Write a quicker way to instantly get the most congested area?

# Returns the optimal sequence of stops (optimal in the sense that people will prefer to take the bus) for a given number of stops & given time interval t between stops
def getRoutes(x, t):
    res = [getCongestionList(0)[0]]
    for i in range(x-1):
        nextList = getCongestionList(t*i)
        cur = nextList[0]
        if (res[0] = cur): # check if the next most congested area is the same as the current one, in which case we want to the the second most congested area (so that the bus actually moves)
            cur = nextList[1]
        if addStop(cur, res): # if adding the stop is beneficial, we add it
            res.append(cur)
    return res

# Returns the difference in time between getting to a stop directly and taking the bus there
def addStop(s, stops):
    # Calculate time it takes to get to stop by bus (no traffic)
    busTime = 0
    for i in range(len(stops)-1):
        busTime += expectedTime(stops[i], stops[i+1])[0]
    busTime += expectedTime(stops[len(stops)-1], s)[0]

    return expectedTime(stops[0], s)[1] - busTime

# Returns the expected times (not congested and congested) to travel from s1 to s2
def expectedTime(s1, s2):
    return None
    # expectedTime[0] : not congested, expectedTime[1] : congested

# Returns the expected reduction in congestion for an optimal route given a number of stops and time interval t
def reductionAverage(x, t):
    routes = getRoutes(x, t)
    sum = 0
    weight = 0
    for s in x:
        sum += routes[s][1]*(1-(routes[s][0])/(routes[s][1]))
        weight += routes[s][1]
    return sum/weight

# Returns the cap on stops (where adding stops starts to make the route worse)
def getStopCap(x, t):

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