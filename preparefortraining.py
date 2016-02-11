from scipy.io.wavfile import read
import numpy as np
from fft import calculatefft

def prepare_data(filename):

	test = np.array([264, 297, 330, 352, 396, 440, 495, 528, 594, 660, 704, 792, 880, 990, 1056])
	freqs = np.array(np.exp(np.linspace(np.log(264), np.log(1056), 15)))						#odredjivanje potrebnih frekvencija
	round_freqs = np.round(freqs, 0)

	fs, data = read(filename, mmap=False)

	data = np.array(data)
	high = np.amax(data)
	data = data/high

	chunk = fs/10

	timedata = []																				#seckanje zvuka od n s, na n zvukova od 1s

	for i in range(0, 1200):
		timedata.append(data[i*chunk:i*chunk+chunk])

	timedata = np.array(timedata)

	fftdata = []

	for row in timedata:																		#za svaki zvuk se racuna fft
		fftdata.append(calculatefft(fs, row)[0])

	amps = []	

	for row in fftdata:																			#uzimanje odgovarajucih amplituda za frekvencije
		amps.append(row[test])

	x = np.array(amps)
	y = []
	for i in range(0, 1200):
		y.append([1, 0, 0, 0])

	y = np.array(y)

	return x, y
