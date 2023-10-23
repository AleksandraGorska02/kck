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
    
    
    plt.figure(figsize=(10, 6))
    plt.subplot(1, 2, 1)

    # Pierwszy wykres
    plt.plot(dane3["effort"], dane3["avg"], color='blue', label='1-Evol-RS',marker='o', markevery=25,markeredgecolor='black')
    plt.plot(dane2["effort"], dane2["avg"], color='green', label='1-Coev-RS',marker='^', markevery=25,markeredgecolor='black')
    plt.plot(dane5["effort"], dane5["avg"], color='red', label='2-Coev-RS', marker='D', markevery=25,markeredgecolor='black')
    plt.plot(dane1["effort"], dane1["avg"], color='black', label='1-Coev',marker='s', markevery=25,markeredgecolor='black')
    plt.plot(dane4["effort"], dane4["avg"], color='deeppink', label='2-Coev',marker='d', markevery=25,markeredgecolor='black')

    plt.margins(x=0, y=0)
    plt.xlim(0, 500000)
    plt.xticks(range(0, 500001, 100000),["0", "100", "200", "300", "400", "500"])
    plt.yticks([0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1],["60", "65", "70", "75", "80", "85", "90", "95", "100"])
    plt.xlabel("Rozegranych gier (" + r"$\times$" + "1000)")
    plt.ylabel("Odsetek wygranych gier [%]")
    legend = plt.legend(frameon=True, loc='lower right')
    frame = legend.get_frame()
    frame.set_edgecolor('black')
    plt.grid(True, linestyle='--', alpha=0.7)
    ax2 = plt.twiny()
    ax2.set_xlim(0, 500000)
    ax2.set_xticks(range(0, 500001, 100000))
    ax2.set_xticklabels(["0", "40", "80", "120", "160", "200"])
    ax2.set_xlabel("Pokolenie")
   #dodanie markerów do wykresu dla danych
    


    # Drugi wykres
    plt.subplot(1, 2, 2)

    plt.plot(dane3["effort"], dane3["avg"], color='blue', label='1-Evol-RS')
    plt.plot(dane2["effort"], dane2["avg"], color='green', label='1-Coev-RS')
    plt.plot(dane5["effort"], dane5["avg"], color='red', label='2-Coev-RS')
    plt.plot(dane1["effort"], dane1["avg"], color='black', label='1-Coev')
    plt.plot(dane4["effort"], dane4["avg"], color='deeppink', label='2-Coev')

    plt.margins(x=0, y=0)
    plt.xlim(0, 500000)
    plt.ylim(0.6, 1)
    plt.xlabel("Rozegranych gier")
    plt.ylabel("Odsetek wygranych gier [%]")
    legend = plt.legend(frameon=True, loc='lower right')
    frame = legend.get_frame()
    frame.set_edgecolor('black')

    plt.tight_layout()
    plt.show()

   

if __name__ == '__main__':
    main()
