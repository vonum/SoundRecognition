import scipy
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np
import sys
from utils import calculatefft

fs, data = read(sys.argv[1], mmap=False)

amp, frq = calculatefft(fs, data)

plt.xlabel('frequency')
plt.ylabel('amplitude')
plt.plot(frq, amp)
plt.show()

freqs = np.array(np.exp(np.linspace(np.log(264), np.log(1056), 15)))
round_freqs = np.round(freqs, 0)
amps = amp[round_freqs.astype(np.int64)]

test = np.array([264, 297, 330, 352, 396, 440, 495, 528, 594, 660, 704, 792, 880, 990, 1056])

#T = n/float(fs)

#frq = k/T
T = len(data)/float(fs)
k = test * T

print k
print np.amax(amp)
print np.where(amp == np.amax(amp))

#print round_freqs.astype(np.int64)

#plt.plot(amps)
#plt.show()