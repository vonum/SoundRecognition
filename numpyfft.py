import scipy
import scipy.fftpack
import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read

fs, data = read("testinput1.wav", mmap=False)

y = abs(scipy.fft(data))
freqs = scipy.fftpack.fftfreq(len(data), 1.0/44032)


plt.plot( freqs, y)
plt.show()