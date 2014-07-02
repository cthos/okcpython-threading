from multiprocessing import Process

integer = 0

def simple_example(thread_id):
    global integer
    integer += 1
    
    print "Thread {0} says integer is {1}".format(thread_id, integer)

p1 = Process(target=simple_example, args=(1,))
p2 = Process(target=simple_example, args=(2,))
p1.start()
p2.start()

p1.join()
p2.join()
