from scipy.io.wavfile import read
import numpy as np
from fft import calculatefft

def prepare_data(filename):
	fs, data = read(filename, mmap=False)

	data = np.array(data)
	high = np.amax(data)
	data = data/high

	chunk = fs/10

	timedata = []																				#seckanje zvuka od n s, na n zvukova od 1s

	for i in range(0, 9000):
		timedata.append(data[i*chunk:i*chunk+chunk])

	timedata = np.array(timedata)

	fftdata = []

	for row in timedata:																		#za svaki zvuk se racuna fft
		fftdata.append(calculatefft(fs, row)[0])

	amps = []

	freqs = np.array(np.exp(np.linspace(np.log(264), np.log(1056), 50)))						#odredjivanje potrebnih frekvencija
	round_freqs = np.round(freqs, 0)
	####
	#freq = np.array([399])		

	for row in fftdata:																			#uzimanje odgovarajucih amplituda za frekvencije
		amps.append(row[round_freqs.astype(np.int64)])
		#amps.append(row[freq])

	x = np.array(amps)
	y = []
	for i in range(0, 9000):
		y.append([1, 0, 0, 0])

	y = np.array(y)

	return x, y
