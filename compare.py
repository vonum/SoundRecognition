from scipy.io.wavfile import read
import numpy as np
from fft import calculatefft
from localmax import localmax

test = np.array([264, 297, 330, 352, 396, 440, 495, 528, 594, 660, 704, 792, 880, 990, 1056])


print "TEST"
print "-----------------"
fs, data = read('test/330test.wav')
data  = data[0:9600]

T = len(data)/float(fs)
k = test * T
chunk = 9600

amp, freq = calculatefft(fs, data)

print T
print len(data)
print fs
print k
print np.amax(amp)
print np.where(amp == np.amax(amp))
print freq[np.where(amp == np.amax(amp))]
print localmax(amp, k)

fs, data = read('training330.wav')
for i in range(0, 3):
	print "SAMPLES"
	print"----------"
	tmpdata = data[i*chunk:i*chunk+chunk]
	amp, freq = calculatefft(fs, tmpdata)
	print k
	print np.amax(amp)
	print np.where(amp == np.amax(amp))
	print freq[np.where(amp == np.amax(amp))]
	print localmax(amp, k)


#data = data[0:9600]
#amp, freq = calculatefft(fs, data)
#print np.amax(amp)
#print np.where(amp == np.amax(amp))
#print amp[33], amp[32], amp[34]

