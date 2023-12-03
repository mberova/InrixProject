from core import *

def minutes(waypoints, useTraffic):
    url = f"https://api.iq.inrix.com/findRoute?useTraffic=true"
    text = 'uncongestedTravelTimeMinutes="'
    if useTraffic:
        text = 'travelTimeMinutes="'
    wp = []
    for i,(lat,long) in enumerate(waypoints):
        if i <= 10:
            url+=f'&wp_{i}={lat},{long}'
        else:
            wp.append((lat,long))
            
    headers = {
      'Authorization': f'Bearer {get_token()[0]}'
    }
    response = requests.request("GET", url, headers=headers, data={})
    
    m = None
    
    try:
        m = int(response.text.split(text)[1][:2])
    except:
        m = 1
    if len(wp) == 0:
        return m
    return m + minutes(wp)

class Cong:
    def __init__(self, lat, long, cong):
        self.latitude = lat
        self.longitude = long
        self.congestion = cong
    
    def __str__(self):
        return f'latitude: {self.latitude}\nlongitude: {self.longitude}\ncongestion: {self.congestion}'
    
    def __lt__(self, other):
        return self.congestion < other.congestion
    
    def __gt__(self, other):
        return self.congestion > other.congestion
    
    def __ge__(self, other):
        return self.congestion >= other.congestion

def congestion(startTime, box):
    url = f"https://api.iq.inrix.com/v1/segments/speed?SpeedOutputFields=SpeedBucket&box={box}&StartTime={start}"
    headers = {
      'Authorization': f'Bearer {get_token()[0]}'
    }

    response = requests.request("GET", url, headers=headers, data={})
    text = response.text
    #print(text, box)
    segments = json.loads(text)['result']['segmentspeeds'][0]['segments']
    s = 0
    c = 0
    for segment in segments:
        if 'speedBucket' in segment:
            s += segment['speedBucket']
            c += 1
    return s/c

def remove_duplicates(congs, to_remove, la1, lo1, la2, lo2, ladiv, lodiv):
    lainc = (la2-la1)/ladiv
    loinc = (lo2-lo1)/lodiv
    for lat,long in to_remove:
        col = (lat-la1)/lainc
        row = (long-lo1)/loinc
        numpy.delete(congs, row*lodiv+col)
    

def get_map(la1, lo1, la2, lo2, ladiv, lodiv, start):
    box = f'{la1}%7C{lo1},{la2}%7C{lo2}'
        
    a1 = min(la1,la2)
    a2 = max(la1,la2)
    o1 = min(lo1,lo2)
    o2 = max(lo1,lo2)
    la1, la2, lo1, lo2 = a1, a2, o1, o2
    
    res = []
    
    dt = datetime.datetime.now()
    y = dt.year
    m = dt.month
    d = dt.day+1
    if m < 10:
        m = f'0{m}'
    if d < 10:
        d = f'0{d}'
    
    start_time = f'{y}-{m}-{d}T{start//60}:{start%60}:00Z'
    
    lainc = (la2-la1)/ladiv
    loinc = (lo2-lo1)/lodiv
    
    curr_lo1 = lo1
    curr_lo2 = lo1+loinc  
    while(curr_lo2 <= lo2):
        curr_la1 = la1
        curr_la2 = la1+lainc      
        while(curr_la2 <= la2):
            box = f'{curr_la1}%7C{curr_lo1},{curr_la2}%7C{curr_lo2}'
            score = None
            try:
                score = congestion(start_time, box)
            except:
                score = 0
            res.append(Cong(curr_la1, curr_lo1, score))
            curr_la2 += lainc
            curr_la1 += lainc
            #print(curr_la1, curr_la2, curr_lo1, curr_lo2)
        curr_lo1 += loinc
        curr_lo2 += loinc
        
    return numpy.array(res)