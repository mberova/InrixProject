from congestion import get_map as getMap 
from congestion import minutes as minutes
from congestion import remove_duplicates as removePresent
import numpy as np
import math

PARAMS = [37.699033, -122.491619, 37.858031, -122.390381, 10, 10]

def getCongestionList(t):
    print("in getCongestionList")
    return getMap(PARAMS[0], PARAMS[1], PARAMS[2], PARAMS[3], PARAMS[4], PARAMS[5], t) # TODO: Let the user input these

## TODO: Write a quicker way to instantly get the most congested area?

def getMaxCongestion(l):
    return np.max(l)

def get2MaxCongestion(l):
    maxIndex = np.argmax(l)
    arr = np.delete(l, maxIndex)
    return np.max(arr)

def congToTuple(c):
    print(c)
    return (c.latitude, c.longitude)

# Returns the optimal sequence of stops (optimal in the sense that people will prefer to take the bus) for a given number of stops & given time interval t between stops
def getRoutes(x, t0):
    # first = getCongestionList(t0)
    # if (x == len(first)): 
    #     return first
    res = [congToTuple(getMaxCongestion(getCongestionList(t0)))]
    t = 0
    x = math.floor(x)
    for i in range(x-1):
        nextList = removePresent(getCongestionList(t0 + t), res, PARAMS[0], PARAMS[1], PARAMS[2], PARAMS[3], PARAMS[4], PARAMS[5])
        cur = congToTuple(getMaxCongestion(nextList))
        if (res[0][0] == cur[0] and res[0][1] == cur[1]): # check if the next most congested area is the same as the current one, in which case we want to the the second most congested area (so that the bus actually moves)
            cur = congToTuple(get2MaxCongestion(nextList))
        # insert the stop at the optimal spot
        addResults = addStop(cur, res)
        res.insert(addResults[0], cur)
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
    print("in expectedtime")
    return [minutes([s1, s2], False), minutes([s1, s2], True)]

# Returns the expected reduction in congestion for an optimal route given a number of stops
def reductionAverage(x, t0):
    print("in reductionaverage")
    routes = getRoutes(x, t0)
    sum = 0
    weight = 0
    x = math.floor(x)
    for i in range(x-1):
        print ("in loop")
        curTime = expectedTime(routes[i], routes[i+1])
        sum += curTime[1]*(1-(curTime[0]/curTime[1]))
        weight += curTime[1]
    if (weight == 0): weight = 1
    return sum/weight