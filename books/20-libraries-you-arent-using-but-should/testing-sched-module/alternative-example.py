import sched
import time
from datetime import datetime, timedelta

# instancing scheduler class with current time
scheduler = sched.scheduler(timefunc=time.time)

def reschedule():
    # this will create an instance of datetime.now() but with second and microseconds with 0 value
    new_target = datetime.now().replace(second=0, microsecond=0)
    # increments one minute
    new_target += timedelta(minutes=1)

    """
    enterabs - it's used to schedule an event at an absolute time, specified as a timestamp
    timestamp - transform the date into seconds, ex: 
        Before: datetime.datetime(2023, 6, 26, 21, 39, 14, 717985)  
        After: 1687826354.717985
    """
    scheduler.enterabs(new_target.timestamp(), priority=0, action=saytime)

def saytime():
    """
    the flush argument, forces the print to return and display the text immediately without a delay
    this can be used in scenarios where I want to print real-time values
    """
    print(time.ctime(), flush=True)
    reschedule()

reschedule()
try:
    # start of the event loop
    scheduler.run(blocking=True)
# This exception is when we type CTRL+C for example
except KeyboardInterrupt:
    print('Stopped.')