import time
from time import sleep
from threading import Thread

def job(job_num):
    print('Starting job %d now' % job_num)
    sleep(3)
    print('Job %d done' % job_num)

time_start = int(time.time())

thread1 = Thread(target=job, args=(1,))
thread2 = Thread(target=job, args=(2,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

time_end = int(time.time())

print("Running jobs took %d secs" % (time_end - time_start))
