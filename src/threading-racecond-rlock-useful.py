from threading import Thread, RLock

class RaceThread(Thread):
    sharedVariable = 0
    
    def __init__(self, increment, lock):
        self.increment = increment
        self.lock = lock
        super(RaceThread, self).__init__()
    
    def run(self):
        for i in range(0, 100):
            with self.lock:
                self.othermethod()
                RaceThread.sharedVariable += self.increment
            
                if (RaceThread.sharedVariable > 10):
                    RaceThread.sharedVariable = 0
                    
                print RaceThread.sharedVariable

    def othermethod(self):
        with self.lock:
            print "Hi there"
# This is useful in case you need to have 2 methods acquire the lock
lock = RLock()
            
t1 = RaceThread(1, lock)
t2 = RaceThread(2, lock)
t3 = RaceThread(3, lock)

t1.start()
t2.start()
t3.start()
