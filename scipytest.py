import scipy
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import numpy as np

fs, data = read("testinput1.wav", mmap=False)

#print fs, data[0:10]

x = np.linspace(0.0, 1.0, 44032)

print len(x)
print len(data)

freqdata = fft(data)

#print freqdata[0:50]

freqplot = freqdata[0:len(freqdata)]

plt.plot(np.arange(44032), abs(freqdata))
plt.show()