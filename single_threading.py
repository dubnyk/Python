import time
from time import sleep

def job(job_num):
    print('Starting job %d now' % job_num)
    sleep(3)
    print('Job %d done' % job_num)

time_start = int(time.time())

job(1)
job(2)

time_end = int(time.time())

print("Running jobs took %d secs" % (time_end - time_start))
