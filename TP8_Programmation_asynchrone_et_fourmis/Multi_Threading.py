import os
import time
import threading

def calcul_long():
    print("pid:" + str(os.getpid()))
    n = 1E7
    while n > 0:
        n -= 1


def multiThreading():

    class myThread (threading.Thread):
        def __init__(self, threadID, name):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name

        def run(self):
            print("Démarrer: " + self.name)
            calcul_long()
            print("Fin: " + self.name)

    # Créer nouveaux threads
    thread1 = myThread(1, "Thread-1")
    thread2 = myThread(2, "Thread-2")
    thread3 = myThread(3, "Thread-3")

    # Lancer threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Attend que les threads se terminent
    thread1.join()
    thread2.join()
    thread3.join()
    print("Sortir")


if __name__ == "__main__":
    start = time.time()
    multiThreading()
    end = time.time()
    print("Temps d'exécution du processeur <coeur de CPU>:", end - start)