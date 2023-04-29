#note: n_values are supposed to be inputed by user; this is the demonstration of different n_values contributing to relative frequency

import random
import matplotlib.pyplot as plt

n_values = [9, 95, 990, 9989, 99995, 5000000]

for n in n_values:
    zbir8 = 0
    zbir9 = 0

    for i in range(0, n): 
        kockica1 = random.randint(1,6)
        kockica2 = random.randint(1,6)
        kockica3 = random.randint(1,6)
        a = [kockica1, kockica2, kockica3]
        zbir_brojeva = sum(a)
        if zbir_brojeva == 8:
            zbir8 += 1
        elif zbir_brojeva == 9:
            zbir9 += 1
        
    relativna_frekvencija8 = zbir8 / n
    relativna_frekvencija9 = zbir9 / n
    
    print("Zbir brojeva je jednak 8:", zbir8, "puta. \nZbir brojeva je jednak 9:", zbir9, "puta. \n")
    print("Relativna frekvecnija zbira 8 je:", relativna_frekvencija8, "\nRelativna frekvencija zbira 9 je:", relativna_frekvencija9)
    
    plt.figure()
    plt.bar(["Zbir 8", "Zbir 9"], [relativna_frekvencija8, relativna_frekvencija9], color=['#FFDD33', '#FF5733'])
    plt.title(f"n = {n}")
    plt.ylabel("Relativna frekvencija")
    plt.show()


