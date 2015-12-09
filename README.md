# nycevents
Crawl NYC event from web archieve


## Event sources
There is an event archive here:
http://www1.nyc.gov/events/events-filter.html#page-1

This page provides an API supporting query events by date.

The base API url:

`http://www1.nyc.gov/calendar/api/json/search.htm`

Parameters:

`startDate, endDate, sort, pageNumber`

Examples:

`http://www1.nyc.gov/calendar/api/json/search.htm?startDate=01/01/2014%2012:00%20AM&endDate=12/31/2014%2011:59%20PM&sort=DATE&pageNumber=1`


### codec problem

The API will returns a JSON object, which is coded in 'cp1252'. The encoding if unknown from the API. However, the stackoverflow provides the following insight

`If the encoding of a file is said to be *latin1* or unknown, or there is no mention of such a concept, then surely the encoding is *cp1252*. Unless, of course, the file is ancient, in which case the encoding is *cp850* or *cp437*. Further more, the files may result from concatenating many others, in which case the encoding may well be a fubarred mixture.`

