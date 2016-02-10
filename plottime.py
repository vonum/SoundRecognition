import scipy
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import numpy as np
import sys


fs, data = read(sys.argv[1], mmap=False)

#x = np.arange(len(data))

end = 1.0 - (96000.0 - len(data))/96000.0

x = np.linspace(0.0, end, len(data))

plt.xlabel('time')
plt.ylabel('amplitude')
plt.plot(x, data)
plt.show()