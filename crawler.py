from pymongo import MongoClient
import urllib
import urllib2
import json
import sys
from bs4 import BeautifulSoup


"""
Crawl events from
http://www1.nyc.gov
"""


def retrieve_online_event( page = 1 ):
    url = 'http://www1.nyc.gov/calendar/api/json/search.htm'
    values = {  'startDate': '01/01/2014 12:00 AM',
                'endDate': '12/31/2014 11:59 PM',
                'sort': 'DATE',
                'pageNumber': page
             }
             
    data = urllib.urlencode(values)
    
    
    the_page = urllib.urlopen('{0}?{1}'.format(url, data))
    
    html = the_page.read()
    r = json.loads(html.decode('cp1252').encode('utf_8'))
    
    return r['items'], r['pagination']


    
    
def crawl_events_into_Mongo():
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
    
    
    
    
def test_crawling(p):
    # test with page = 88, where the encoding error happened
    return retrieve_online_event( page = p )
    
    

    
    
"""
Crawl events from 
http://www.nyc.com/events/
"""


def crawl_nyc_events( page = 1 ):
    url = 'http://www.nyc.com/events/'
    values = {  'int4': 1,
                'from': '1/1/2015',
                'to':   '12/31/2015',
                'p': page }
    
    data = urllib.urlencode(values)
    the_page = urllib.urlopen('{0}?{1}'.format(url, data))
    
    html = the_page.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find('ul', class_='eventrecords')


if __name__ == '__main__':
    
    
    # r = test_crawling(88)
    # crawl_events_into_Mongo()
    s = crawl_nyc_events(2)
    with open('test2.html', 'w') as fout:
        fout.write(str(s))
        
        
    
    