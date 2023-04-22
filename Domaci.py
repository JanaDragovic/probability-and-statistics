import random
from math import *
n = int(input("Unesite broj koliko puta zelite da se izvrsi data simulacija: "))

zbir8 = 0
zbir9 = 0

for i in range(0, n): 
    kockica1 = random.randint(1,6)
    kockica2 = random.randint(1,6)
    kockica3= random.randint(1,6)
    a=[kockica1, kockica2, kockica3]
    zbir_brojeva = sum(a)
    if zbir_brojeva == 8:
        zbir8+=1
    elif zbir_brojeva == 9:
        zbir9+=1
        
relativna_frekvencija8 = zbir8/n
relativna_frekvencija9 = zbir9/n
    
print("Zbir brojeva je jednak 8: ",zbir8, " puta. \nZbir brojeva je jednak 9: ", zbir9, " puta. \n")
print("Relativna frekvecnija zbira 8 je: ", relativna_frekvencija8, "\nRelativna frekvencija zbira 9 je: " ,relativna_frekvencija9)
