import os 
import time

os.system("cls")

#De 1 até 10

for i in range(1, 11, 1):
    print(i)
    # Espera um segundos
    time.sleep(1)

#De 10 até 1
for i in range(10, 0, -1):
    print(i)
    # Espera um segundos
    time.sleep(1)

#De 5 até 0
for i in range(5, -1, -1):
    print(i)
    # Espera um segundos
    time.sleep(1)
