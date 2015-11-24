from pymongo import MongoClient
import urllib
import urllib2
import json
import sys


def retrieve_online_event( page = 1 ):
    url = 'http://www1.nyc.gov/calendar/api/json/search.htm'
    values = {  'startDate': '01/01/2014 12:00 AM',
                'endDate': '12/31/2014 11:59 PM',
                'sort': 'DATE',
                'pageNumber': page
             }
             
    data = urllib.urlencode(values)
    
    the_page = urllib.urlopen('{0}?{1}'.format(url, data))
    r = json.loads(the_page.read())
    return r['items'], r['pagination']



if __name__ == '__main__':
    
    client = MongoClient('localhost', 27017)
    
    db = client.nyc_events
    docs = db.events
    
    
    p = 0
    total = sys.maxint
    cnt = 0
    while p != total:
        items, pagination = retrieve_online_event(p+1)
        cnt += len(items)
        total = pagination['numPages']
        p = pagination['currentPage']
        docs.insert_many( items )
        if p % 50 == 0:
            print 'On page {0}'.format(p)
        
    print cnt
        
    
    