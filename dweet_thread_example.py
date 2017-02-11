# Queue code https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch12s03.html
import dweepy
import random

from Queue import Queue
from threading import Thread

# A thread that produces data
def producer(out_q):
    for dweet in dweepy.listen_for_dweets_from('rand'):
        print dweet
        out_q.put(dweet)

# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        data = in_q.get()
        # Process the data
        print data

# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()