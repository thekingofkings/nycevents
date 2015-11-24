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
