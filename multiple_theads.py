import logging
import threading
import time


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

 
if __name__ == "__main__":
    
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")
    logging.info("Main: before creating thread")

    handles = []

    for i in range(5):
        x = threading.Thread(target=thread_function, args=(i,),  daemon=True)
        handles.append(x)
        logging.info("Main: before running thread")
        # Comineza el thread
        x.start()

    for handle in handles:
        handle.join()