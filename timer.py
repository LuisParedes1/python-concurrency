import threading
import time

def my_function():
    print("Hello World")



handles = [threading.Timer(2.0, my_function),threading.Timer(2.0, my_function),threading.Timer(2.0, my_function)]

for h in handles:
    # cliente.send()
    h.start()

for h in handles:
    h.join()

## Llega el ACK
# 1. Cancelar el timer del segmento
# 2. Eliminar el segmento de la lista de segmentos pendientes
# 3. Actualizar el estado del cliente