#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd

def main():
    dane1 = pd.read_csv("zadanie_1/1c.csv")
    dane2 = pd.read_csv("zadanie_1/1crs.csv")
    dane3 = pd.read_csv("zadanie_1/1ers.csv")
    dane4 = pd.read_csv("zadanie_1/2c.csv")
    dane5 = pd.read_csv("zadanie_1/2crs.csv")
    dane1["avg"] = dane1[dane1.columns.difference(["effort", "generation"])].mean(axis=1)
    dane2["avg"] = dane2[dane2.columns.difference(["effort", "generation"])].mean(axis=1)
    dane3["avg"] = dane3[dane3.columns.difference(["effort", "generation"])].mean(axis=1)
    dane4["avg"] = dane4[dane4.columns.difference(["effort", "generation"])].mean(axis=1)
    dane5["avg"] = dane5[dane5.columns.difference(["effort", "generation"])].mean(axis=1)
    
    
    plt.plot(dane3["effort"],dane3["avg"],color='blue' ,label='1-Evol-RS')
    plt.plot(dane2["effort"],dane2["avg"],color='green',label='1-Coev-RS')
    plt.plot(dane5["effort"],dane5["avg"],color='red' ,label='2-Coev-RS')
    plt.plot(dane1["effort"],dane1["avg"],color='black',label='1-Coev')
    plt.plot(dane4["effort"],dane4["avg"],color='deeppink' ,label='2-Coev')

    plt.margins(x=0,y=0)
    plt.xlim(0, 500000)
    plt.ylim(0.6, 1)
    plt.xlabel("Rozegranych gier")
    plt.ylabel("Odsetek wygranych gier")
    legend = plt.legend(frameon=True, loc='lower right')
    frame = legend.get_frame()
    frame.set_edgecolor('black')
    plt.show()

   

if __name__ == '__main__':
    main()

