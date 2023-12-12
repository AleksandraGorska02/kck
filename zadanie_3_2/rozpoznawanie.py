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




def hps(signal, fs):
    """Estimate the pitch using the Harmonic Product Spectrum (HPS).
    """
    # Compute the short-time Fourier transform of the signal


    hamming_window = np.hamming(len(signal))
    signal = signal * hamming_window
    spectrum = np.fft.rfft(signal)
    spectrum = np.abs(spectrum)
    hps = spectrum.copy()
    for harmonic in range(2, 6): #wywalenie wszystkicg równych 0
        decimated_spectrum = spectrum[::harmonic]
        hps[:len(decimated_spectrum)] *= decimated_spectrum
    # Find the peak in the HPS



    estimated_pitch_index = np.argmax(hps)

    # Convert the index to frequency in Hertz

    estimated_pitch = fs * estimated_pitch_index / len(signal)

    return estimated_pitch
        
if __name__ == '__main__':
    wyn=0
    files_path = os.listdir('./zadanie_3_2/train/')
    for file in files_path:
       
        fs, signal = scipy.io.wavfile.read("./zadanie_3_2/train/"+file, mmap=False)
        if len(signal.shape) > 1:
            signal = signal[:, 0]

        #correct answer
        correrct_answer = file.split('_')[1][0]
      
       
        result ="K" if hps(signal, fs) > 160 else "M"
        if result == correrct_answer:
            wyn+=1
        else:
            print("FAŁsz")
     


       
        print("result: ", result, "correct answer: ", correrct_answer, "file: ", file, "hps: ", hps(signal, fs))
        
    print(wyn / len(files_path))

        
 


