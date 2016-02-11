from scipy.io.wavfile import read
import numpy as np
from fft import calculatefft

test = np.array([264, 297, 330, 352, 396, 440, 495, 528, 594, 660, 704, 792, 880, 990, 1056])

fs, data = read('training440.wav')

print np.amax(data)

data = calculatefft(fs, data)[0]

scale = np.amax(data)

fst, datat = read('test.wav')
datat = calculatefft(fst, datat)[0]

print data[test]/scale
print datat[test]/scale