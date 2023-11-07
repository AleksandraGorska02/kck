import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    filename = 'zadanie_2_2/big.dem'
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [line.split() for line in lines]
        lines = [[float(value) for value in line] for line in lines]
    
    dane=lines[0]

   
    lines = lines[1:]
    lines = np.array(lines)
    print(lines[0][1])
    #coppy lines
    lines2=lines.copy()
    #increase values by 10% if value is greather than the previous one
    for i in range(0,len(lines)):
        for j in range(1,len(lines[i])):
            if lines2[i][j]>lines2[i][j-1]:
                lines[i][j]=lines[i][j]*1.1
            else:
                lines[i][j]=lines[i][j]*0.9


    #decrease values by 10% if value is smaller than the previous one
    print(lines[0][1])
    #uzywajac wybranego gradientu wyswietl podany teren
     #Dodaj więc cieniowanie, tak aby nadać rysunkowi głębi. Zacznij od najprostszej metody: pojaśniaj lub pociemniaj piksel w zależności od tego, czy jego lewy sąsiad jest wyżej czy niżej na mapie
    plt.imshow(lines, cmap='terrain')
    plt.colorbar()
    plt.show()



   

if __name__ == '__main__':
    main()