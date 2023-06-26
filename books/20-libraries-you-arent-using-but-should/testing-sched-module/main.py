import sched
import time

scheduler = sched.scheduler(timefunc=time.time)


def saytime():
    """
    ctime() represents a second formatted date in a local time string
    Ex using .ctime(): Mon Jun 26 20:37:32 2023
    Ex using .time(): 1687822783.908726
    """
    print(time.time())
    # scheduler.enter(10, priority=0, action=saytime())


saytime()
try:
    scheduler.run(blocking=True)
except KeyboardInterrupt:
    print('Stopped.')
