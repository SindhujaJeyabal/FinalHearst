import urllib
import urllib2
import json

class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)

def GetSubTribes():        
    url = "https://apis.berkeley.edu/hearst_museum/select"
    values = {'q' : 'objculturetree_ss:California tribes',
                'rows' : '44800',
                'wt' : 'json',
                'indent': 'on',
                'fl' : 'objassoccult_txt'}

    headers = { 'app_id' : '8dc4e11c',
                'app_key': '4aa1d8d78752ef675e607187c4663b17',
                'User-Agent': 'Mozilla 5.10',
                'Accept-Charset':'utf-8'}
    data = urllib.urlencode(values)
    url = url + '?' + data
    req = urllib2.Request(url, None, headers)

    result = urllib2.urlopen(req).read()
    r = Payload(result)
    tlist = [tribe.values()[0] for tribe in r.response['docs'] if (len(tribe.values())!=0)]
    t2 = [item for sublist in tlist for item in sublist]
    t3 = list(set(t2))
    t4 = [item.encode('utf8',"replace") for item in t3]
    t5 = [item for item in t4 if (('@' not in  item) and ('DO NOT USE' not in item) and ('c3' not in item) and ('?' not in item) )]
    return t5
