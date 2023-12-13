import scipy
import matplotlib.pyplot as plt
import numpy as np
import os
from pydub import AudioSegment
from numpy import *
import math
from ipywidgets import *
import matplotlib.pyplot as plt
import pandas as pd

from scipy.signal import find_peaks



def hps(signal, fs):
    hamming_window = np.kaiser(len(signal),beta=30)
    signal=signal.astype(float)
    signal *= hamming_window
    spectrum = np.fft.rfft(signal)
    spectrum = np.abs(spectrum)
    for i in range(1, len(spectrum)):
        spectrum[i] = spectrum[i] / i
    spectrum = spectrum / np.max(spectrum)
    hps = np.copy(spectrum)
    for harmonic in range(2, 7): 
        decimated = scipy.signal.decimate(spectrum, harmonic)
        hps[:len(decimated)] += decimated
    for harmonic in range(2, 7): 
        hps*=np.roll(spectrum, harmonic)
    peaks,_=find_peaks(hps, height=0)
    freqs = fs*peaks/len(signal)
    male = (85, 180)
    fmale = (160, 255)
    male2 = np.interp(np.arange(male[0], male[1] + 1), freqs, hps[peaks])
    fmale2 = np.interp(np.arange(fmale[0], fmale[1] + 1), freqs, hps[peaks])
    male_sum = np.sum(male2)
    female_sum = np.sum(fmale2)
    if male_sum > female_sum:
        return 'M'
    else:
        return 'K'

        
if __name__ == '__main__':
    wyn=0
    files_path = os.listdir('./zadanie_3_2/train/')
    for file in files_path:
       
        fs, signal = scipy.io.wavfile.read("./zadanie_3_2/train/"+file, mmap=False)
        if len(signal.shape) > 1:
            signal = signal[:, 0]

        #correct answer
        correrct_answer = file.split('_')[1][0]
      
       
        result = hps(signal, fs)
        if result == correrct_answer:
            wyn+=1
        else:
            print("FAŁsz")
     


       
        print("result: ", result, "correct answer: ", correrct_answer, "file: ", file, "hps: ", hps(signal, fs))
        
    print(wyn / len(files_path))

        
 


