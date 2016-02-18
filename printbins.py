from scipy.io.wavfile import read
import numpy as np
from fft import calculatefft
from localmax import adaptivelocalmax
from localmax import localmax


freqs = np.array(np.exp(np.linspace(np.log(264), np.log(2000), 150)))
round_freqs = np.round(freqs, 0)

#9600/96000
T = 0.1

print 'Prave Frekvencije'
print round_freqs

round_freqs = round_freqs * T

print 'Indeksi'
print round_freqs

print '---------------------------------------0:20'
for i in range(0, 20):
	print (round_freqs[i] - 0.5) / T, (round_freqs[i] + 0.5) / T
print '---------------------------------------20:40'
for i in range(20, 40):
	print (round_freqs[i] - 0.5) / T, (round_freqs[i] + 0.5) / T
print '---------------------------------------40:60'
for i in range(40, 60):
	print (round_freqs[i] - 0.5) / T, (round_freqs[i] + 0.5) / T
print '---------------------------------------60:80'
for i in range(60, 80):
	print (round_freqs[i] - 0.5) / T, (round_freqs[i] + 0.5) / T
print '---------------------------------------80:100'
for i in range(80, 100):
	print (round_freqs[i] - 0.6) / T, (round_freqs[i] + 0.7) / T
print '---------------------------------------100:120'
for i in range(100, 120):
	print (round_freqs[i] - 0.9) / T, (round_freqs[i] + 0.9) / T
print '---------------------------------------120:150'
for i in range(120, 150):
	print (round_freqs[i] - 1.3) / T, (round_freqs[i] + 1.3) / T


