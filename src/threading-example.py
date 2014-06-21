from threading import Thread

class MyThread(Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        
        self.name = name
        
    def run(self):
        print "Hello there thread {0}.".format(self.name)
        

t1 = MyThread("one")
t2 = MyThread("two")

t1.start()
t2.start()