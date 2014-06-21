from threading import Thread

class RaceThread(Thread):
    sharedVariable = 0
    
    def __init__(self, increment):
        self.increment = increment
        super(RaceThread, self).__init__()
    
    def run(self):
        for i in range(0, 100):
            RaceThread.sharedVariable += self.increment
            
            if (RaceThread.sharedVariable > 10):
                RaceThread.sharedVariable = 0
                
            print RaceThread.sharedVariable
            
t1 = RaceThread(1)
t2 = RaceThread(2)
t3 = RaceThread(3)

t1.start()
t2.start()
t3.start()