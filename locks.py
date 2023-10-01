import logging
import time
import threading
import concurrent.futures

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock() # This ._lock is initialized in the unlocked state.

    def locked_update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock", name)
        
        # Lock is locked and released by the with statement.
        with self._lock:
            logging.debug("Thread %s has lock", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.3)
            self.value = local_copy
            logging.debug("Thread %s about to release lock", name)
        
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    
    logging.getLogger().setLevel(logging.DEBUG)


    database = FakeDatabase()

    # logging.info("Testing update. Starting value is %d.", database.value)
    # with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    #     for index in range(2):
    #         executor.submit(database.locked_update, index)
    # logging.info("Testing update. Ending value is %d.", database.value)

    threads = list()
    for index in range(3):
        #logging.info("Main: create and start thread %d.", index)
        x = threading.Thread(target=database.locked_update, args=(index,))
        threads.append(x)
        x.start()
    

    for index, thread in enumerate(threads):
        #logging.info("Main    : before joining thread %d.", index)
        thread.join()
        #logging.info("Main    : thread %d done", index)
