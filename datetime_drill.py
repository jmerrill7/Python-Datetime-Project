######Python 2.7
######
######Author: James Merrill
######
######Project: The company you work for just opened two new branches. One is in New York City,
######the other in London. They need a very simple program to find out if the branches are open or
######closed based on the current time of the Headquarters here in Portland. The hours of both
######branches are 9:00AM - 9:00PM in their own time zone. What is asked of you:
######Create code that will use the current time of the Portland HQ to find out the time in the NYC &
######London branches, then compare that time with the branches hours to see if they are open or
######closed.Print out if each of the two branches are open or closed.
 

import datetime
import time
import pytz

dt_portland = (datetime.datetime.now())
dt_newyork = (datetime.datetime.now(tz = pytz.timezone('US/Eastern')))
dt_london = (datetime.datetime.now(tz = pytz.timezone('Europe/London')))

def get_portland_status():
    portland_time = datetime.datetime.now().time()
    start = datetime.time(9)
    end = datetime.time(21)
    if start <= portland_time <= end:
        print ("Portland's timestamp: {},\n Portland's office is open!\n".format(dt_portland))
    else:
        print ("Portland's timestamp: {},\n Portland's office is closed.\n".format(dt_portland))

def get_newyork_status():
    from datetime import date, datetime, time, timedelta
    newyork_time = datetime.now() + timedelta(hours=3)
    start = newyork_time.replace(hour=9)
    end = start +timedelta(hours=12)
    if start <= newyork_time <= end:
        print ("New York City's timestamp: {},\n New York's office is open!\n".format(dt_newyork))
    else:
        print ("New York City's timestamp: {},\n New York's office is closed.\n".format(dt_newyork))

def get_london_status():
    from datetime import date, datetime, time, timedelta
    london_time = datetime.now() + timedelta(hours=8)
    start = london_time.replace(hour=9)
    end = start +timedelta(hours=12)
    if start <= london_time <= end:
        print ("London's timestamp: {},\n London's office is open!\n".format(dt_london))
    else:
        print ("London's timestamp: {},\n London's office is closed.\n".format(dt_london))

get_portland_status()
get_newyork_status()
get_london_status()
