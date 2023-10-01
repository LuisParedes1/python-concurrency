import logging
import threading
import time


def conexion_persistente(name):
    while True:
        logging.info("Thread %s: executing", name)
        time.sleep(2)
    
    # implementar logica

 
if __name__ == "__main__":
    
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")
    logging.info("Main: before creating thread")

    handles = []

    for i in range(5):
        handles.append(threading.Thread(target=conexion_persistente, args=(i,),  daemon=True))
        # Comineza el thread
        handles[i].start()

    for handle in handles:
        handle.join()