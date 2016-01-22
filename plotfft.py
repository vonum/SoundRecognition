import scipy
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import arange
import numpy as np
import sys

fs, data = read(sys.argv[1], mmap=False)

n = len(data)
k = arange(n)
T = n/float(fs)

frq = k/T

frq = frq[range(n/2)]

amp = fft(data)
amp = amp[range(n/2)]

plt.xlabel('frequency')
plt.ylabel('amplitude')
plt.plot(frq, amp)
plt.show()