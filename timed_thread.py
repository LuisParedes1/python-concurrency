import threading
import time
from enum import Enum
import random

Estados = Enum('Estado', ['Enviado', 'NoEnviado', 'ACK'])
RWND = 2

class timed_Thead:
    def __init__(self):
        self._lock = threading.Lock()
        self.elementos = []
        self.base = 0


    def receive_function(self):
        
        while self.base < len(self.elementos):

            # Simula el num random que llega
            ack_rec = random.randrange(self.base, self.base+RWND, 1)

            with self._lock:
                print("ACK")

                # ack_rec simula el seq_num recibido
                if (ack_rec) < len(self.elementos):
                    self.elementos[ack_rec][1] = Estados.ACK

                    if ack_rec == self.base:
                        print("Llegue aca, la base es:", self.base)
                        
                        while self.base < len(self.elementos):
                            if self.elementos[self.base][1] == Estados.ACK:
                                self.base += 1
                            else:
                                break

                        print("Ahora la base es es:", self.base)
                        print(self.elementos)                
            
            time.sleep(5)
            
    
    def enviar_thread(self):
        while self.base < len(self.elementos):

            with self._lock:
                print("Enviado")
                
                if self.elementos[self.base][1] == Estados.NoEnviado:
                    # Creo el thread para reenviar despues de 15 segundos
                    threading.Timer(15.0, self.reenviar_thread).start()

                for indice in range(self.base, RWND):
                    if self.elementos[indice][1] == Estados.NoEnviado:
                        self.elementos[indice][1] = Estados.Enviado
                    
                    if (indice + 1) == len(self.elementos):
                        break
            
            #print(self.elementos)
            time.sleep(5)

    def reenviar_thread(self):

        with self._lock:
            print("Reenviado")

            for indice in range(self.base, self.base+RWND):
                if self.elementos[indice][1] == Estados.Enviado:
                    self.elementos[indice][1] = Estados.NoEnviado
                
                if (indice + 1) == len(self.elementos):
                    break

        #print(self.elementos)
        time.sleep(15)


        # while True:
        #     with self._lock:
        #         print("Reenviado")
        #         if self.elementos[0][1] != Estados.ACK:
        #             self.elementos[0][1] = Estados.NoEnviado
        #         print(self.elementos)
            
        #     time.sleep(15)

    def addElements(self):
        self.elementos = [[x, Estados.NoEnviado] for x in range(10)]


# read-modify-write section of your code.
# #elementos = [[x, Estado.NoEnviado] for x in range(10)]

send = timed_Thead()
send.addElements()

handles = [
    threading.Thread(target=send.receive_function, daemon=True),
    threading.Thread(target=send.enviar_thread, daemon=True),
    #threading.Thread(target=send.reenviar_thread)
]

for handle in handles:
    handle.start()

for handle in handles:
    handle.join()


#threading.Timer(2.0, my_function, args=(elementos)).start()
