class CongestionList:
    list = None # should be an ORDERED list of most congested areas from API

    curCongestion = 0 # index of 
    def getNextCongestion():

def getCongestionList(rad, c):
    # return a ORDERED list of congested areas within the given circle using API
    return None

def getRoutes(x):
    # choose x most congested stops from list
    # return the best routes between the stops
    # 0-1, 1-2, ..., n-0
    # should have travel times with congestion and with congestion
    # add 30 seconds to each no congestion travel time to account for stopping for passengers

def reductionAverage(x):
    routes = getRoutes(x)
    sum = 0
    weight = 0
    for s in x:
        sum += routes[s][1]*(1-(routes[s][0])/(routes[s][1]))
        weight += routes[s][1]
    return sum/weight