from scipy.fftpack import fft
from scipy import arange
import numpy as np

def calculatefft(fs, data):
	n = len(data)
	k = arange(n)
	T = n/float(fs)

	frq = k/T

	frq = frq[range(n/2)]

	amp = fft(data)
	amp = np.array(amp[range(n/2)])

	return (abs(amp), frq)

