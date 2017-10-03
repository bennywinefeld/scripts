import threading
import time

exitFlag = 0
globalCount = 0

class myThread (threading.Thread):
  def __init__(self, threadID, name, delay):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.name = name
    self.delay = delay

  def run(self):
    print ("Starting " + self.name)
    threadLock.acquire()
    print_time(self.name, self.delay, 5)
    threadLock.release()
    print ("Exiting " + self.name)

def print_time(threadName, delay, counter):
  global globalCount
  while counter:
    time.sleep(delay)
    print ("%s: local=%s, global=%s, %s" % (threadName, counter, globalCount, time.ctime(time.time())))
    globalCount += 1
    counter -= 1

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("Exiting Main Thread")