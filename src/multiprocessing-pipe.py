from multiprocessing import Process, Pipe

def pipe_example(pipe):
    # Can be any object, so long as it can be pickled
    pipe.send("This can be anything")

parent_conn, child_conn = Pipe()

p1 = Process(target=pipe_example, args=(child_conn,))
p1.start()
# This call blocks
print parent_conn.recv()
p1.join()
