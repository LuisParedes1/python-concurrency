# https://realpython.com/intro-to-python-threading/

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
    logging.info("Main    : before creating thread")

    # Creo el thread
    x = threading.Thread(target=thread_function, args=(1,),  daemon=True)

    logging.info("Main    : before running thread")

    # Comineza el thread
    x.start()

    logging.info("Main    : wait for the thread to finish")

    # Espero por el thread
    x.join()

    logging.info("Main    : all done")
