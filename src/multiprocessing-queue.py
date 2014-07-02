from multiprocessing import Process, Queue


def queue_example(queue):
    print "Thread 1"
    print queue.get()
    queue.put({"llama":"fork"})

def queue_example_two(queue):
    print "Thread 2"
    print queue.get()

q = Queue()

q.put(["item1"])

p1 = Process(target=queue_example, args=(q,))
p2 = Process(target=queue_example_two, args=(q,))
p1.start()
p1.join()

p2.start()
p2.join()
