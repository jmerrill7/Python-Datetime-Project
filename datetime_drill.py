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
    newyork_time = datetime.now() - timedelta(hours=3)
    start = datetime.combine(date.today(), time(9)) - timedelta(hours=3)
    end = datetime.combine(date.today(), time(21)) - timedelta(hours=3)
    if start <= newyork_time <= end:
        print ("New York City's timestamp: {},\n New York's office is open!\n".format(dt_newyork))
    else:
        print ("New York City's timestamp: {},\n New York's office is closed.\n".format(dt_newyork))

def get_london_status():
    from datetime import date, datetime, time, timedelta
    london_time = datetime.now() + timedelta(hours=8)
    start = datetime.combine(date.today(), time(9)) - timedelta(hours=8)
    end = datetime.combine(date.today(), time(21)) - timedelta(hours=8)
    if start <= london_time <= end:
        print ("London's timestamp: {},\n London's office is open!\n".format(dt_london))
    else:
        print ("London's timestamp: {},\n London's office is closed.\n".format(dt_london))

get_portland_status()
get_newyork_status()
get_london_status()

