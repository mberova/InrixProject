RAD = 5 # radius given by client
C = [10,50] # lat/long given by client

def getCongestionList(t):
    # return a ORDERED list of congested areas within the given circle using API, at time t
    return None

## TODO: Write a quicker way to instantly get the most congested area?

# Returns the optimal sequence of stops (optimal in the sense that people will prefer to take the bus) for a given number of stops & given time interval t between stops
def getRoutes(x, t0):
    res = [getCongestionList(0)[0]]
    t = 0
    for i in range(x-1):
        nextList = getCongestionList(t0 + t)
        cur = nextList[0]
        if (res[0] = cur): # check if the next most congested area is the same as the current one, in which case we want to the the second most congested area (so that the bus actually moves)
            cur = nextList[1]
        # insert the stop at the optimal spot
        addResults = addStop(cur, res)
        res.insert(cur, addStop[0])
        t += addResults[1]
    return res

# Adds the desired stop into the list of spot at the optimal time
def addStop(s, stops):
    # Set the inserting index + detour time to the front of list position
    index = 0
    dTime = expectedTime(s, stops[0])[0]

    # Check all the indices between two existing stops
    for i in range(1,len(stops)-1):
        curDTime = expectedTime(stops[i-1], s)[0] + expectedTime(s, stops[i])[0]
        if curDTime < dTime:
            dTime = curDTime
            index = i
    
    # Check the back of list position
    lastDTime = expectedTime(stops[len(stops)-1], s)[0]
    if lastDTime < dTime: 
        dTime = lastDTime
        index = len(stops)

    return [index, dTime]

# Returns the expected times (not congested and congested) to travel from s1 to s2
def expectedTime(s1, s2):
    return None
    # expectedTime[0] : not congested, expectedTime[1] : congested

# Returns the expected reduction in congestion for an optimal route given a number of stops and time interval t
# TODO: Fix this
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