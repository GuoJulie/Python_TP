import timeit
from multiprocessing import Process
import os

def calcul_long(self):
    print("pid:" + str(os.getpid()))
    n = 1E7
    while n > 0:
        n -= 1

if __name__ == '__main__':
    start = timeit.default_timer()
    processes = [Process(target=calcul_long, args=('process'+str(i),)) for i in range(3)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    end = timeit.default_timer()
    print("Temps d'exécution du processeur <coeur de CPU>:", end - start)

