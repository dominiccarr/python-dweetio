# Queue code https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch12s03.html
import dweepy
import random
import time

from Queue import Queue
from threading import Thread

# A thread that produces data
def listener(publisher_thread):
    for dweet in dweepy.listen_for_dweets_from('rand'):
        my_dweet = dweet
        print "request coming in from Android %s" % my_dweet
        content = my_dweet["content"]
        should_publish = content["publish"]
        if should_publish == "true":
            publisher_thread.start();
        else:
            print "was false"
            

def publisher():
    while True:
        print "publishing data"
        result = dweepy.dweet_for('testpublisher', {'some_key': 'some_value'})
        print result
        time.sleep(5)

# Create the shared queue and launch both threads
q = Queue()
publisher_thread = Thread(target=publisher)
listener_thread = Thread(target=listener, args=(publisher_thread,))
listener_thread.start()
