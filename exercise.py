import numpy as np
import numpy.fft as nf
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

def freq_pass_filter(filename, filterfreq):
    sample_rate, signals = wav.read(filename)
    signals = signals/(2**15)
    times = np.arange(len(signals))/sample_rate
    
    freqs = nf.fftfreq(signals.size, 1/sample_rate)
    complex_array = nf.fft(signals)
    pows = np.abs(complex_array)
    
    noised_idx = np.where(freqs > 200)[0] 
    ca = complex_array[:]
    ca[noised_idx] = 0 
    filter_pows = np.abs(ca)
    
    filter_sigs = (filter_sigs*(2**15)).astype('i2')
    wav.write('filter.wav',sample_rate,filter_sigs)
signals = signals/(2**15)
    
if __name__ == '__main__':
    filename = '20191223_test_1.wav'
    filterfreq = 5000
    freq_pass_filter(filename, filterfreq)