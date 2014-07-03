from multiprocessing import Process, Value, Array

def state_example(v, a):
    # This isn't atomic! Use a lock
    v.value += 1
    for i in range(5):
        a[i] = 0

val = Value('I', 1)
arr = Array('i', range(10))

p1 = Process(target=state_example, args=(val,arr,))
p1.start()
p1.join()

print val.value
print arr[:]
