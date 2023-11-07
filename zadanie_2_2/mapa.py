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
    
#Używając wybranego gradientu wyświetl wczytany teren
    plt.imshow(lines, cmap='terrain')
    plt.show()
 
   

if __name__ == '__main__':
    main()