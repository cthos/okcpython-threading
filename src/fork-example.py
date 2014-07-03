import os, time, sys

newpid = os.fork()

if newpid == 0:
    # This is the child process.
    for i in range(5):
        print "This is child loop {0}".format(i)
        time.sleep(1)
    # Make sure you die.
    sys.exit()
else:
    # This is the parent, and pid is the child process id
    # Wait until the child finishes otherwise you get zombies
    os.waitpid(newpid, 0)
    print "All done."
