import scipy
import matplotlib.pyplot as plt
import numpy as np
import os

from numpy import *
import math
from ipywidgets import *
import matplotlib.pyplot as plt
import pandas as pd

def hps(signal,fs):
   
    signal1 = signal[0:fs]
    #fft na signal1
    for i in range(0,fs):
        signal1[i] = fft.fft(signal1[i])
    #fft na signal2
    plt.plot(signal1)
    plt.show()
    

   

    return signal
  






if __name__ == '__main__':
 
    files_path = os.listdir('./zadanie_3_2/train/')
    print(files_path)
    for file in files_path:
       
        fs, signal = scipy.io.wavfile.read("./zadanie_3_2/train/"+file, mmap=False)
        #correct answer
        correrct_answer = file.split('_')[1][0]
        hpss = hps(signal,fs)
        if hpss == correrct_answer:
            print('Correct')
            print(hpss)
        else:
            print('Incorrect')
            print(hpss)

        
 


