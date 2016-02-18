from scipy.io.wavfile import read
import numpy as np
from utils import calculatefft
from utils import localmax
from utils import adaptivelocalmax

def prepare_data():

	freqs = np.array([264, 297, 330, 352, 396, 440, 495, 528, 594, 660, 704, 792, 880, 990, 1056]) 	#odredjivanje potrebnih frekvencija
	#freqs = np.array(np.exp(np.linspace(np.log(264), np.log(1056), 15)))						

	chunk = 9600  #96000/10 (sample rate je 96000, uzimam deseti deo sekunde)

	T = 0.1 			#samples/fs 9600/96000

	freqs = freqs * T

	round_freqs = np.round(freqs, 0).astype(np.int64)															

	#data = np.array(data)
	#high = np.amax(data)
	#data = data/high
																				#seckanje zvuka od n s, na n zvukova od 1s

	print round_freqs

	timedata = [] 	#sample-ovi, svaki red je 9600 samplova
	#prvi ton
	#fs, data = read(filename, mmap=False)
	fs, data = read('training/training440.wav')

	for i in range(0, 3000):
		timedata.append(data[i*chunk:i*chunk+chunk])

	#drugi ton
	fs, data = read('training/training660.wav')

	for i in range(0, 3000):
		timedata.append(data[i*chunk:i*chunk+chunk])

	fs, data = read('training/training330.wav')

	for i in range(0, 3000):
		timedata.append(data[i*chunk:i*chunk+chunk])

	fs, data = read('training/training990.wav')

	for i in range(0, 3000):
		timedata.append(data[i*chunk:i*chunk+chunk])	

	timedata = np.array(timedata)

	fftdata = []

	for row in timedata:																		#za svaki zvuk se racuna fft
		fftdata.append(calculatefft(fs, row)[0])

	#fftdata = np.array(fftdata)
	#fftdata = fftdata/10000000000

	amps = []	

	for row in fftdata:																			#uzimanje odgovarajucih amplituda za frekvencije
		#amps.append(row[round_freqs])
		amps.append(localmax(row, round_freqs))

	y = []
	for i in range(0, 3000):
		y.append([1, 0, 0, 0])

	for i in range(0, 3000):
		y.append([0, 1, 0, 0])

	for i in range(0, 3000):
		y.append([0, 0, 1, 0])

	for i in range(0, 3000):
		y.append([0, 0, 0, 1])

	x = np.array(amps)
	y = np.array(y)

	return x, y

def prepare_harder():

	freqs = np.array(np.exp(np.linspace(np.log(264), np.log(2000), 150)))
	round_freqs = np.round(freqs, 0)

	T = 0.1 #n/fs = 9600/96000
	chunk = 9600

	round_freqs = round_freqs * T #indeski frekvencija

	timedata = [] 	#sample-ovi, svaki red je 9600 samplova

	#prvi ton
	fs, data = read('training/trainingG4.wav')

	for i in range(0, 3000):
		timedata.append(data[i*chunk:i*chunk+chunk])

	#drugi ton
	fs, data = read('training/trainingF5.wav')

	for i in range(0, 3000):
		timedata.append(data[i*chunk:i*chunk+chunk])

	fs, data = read('training/trainingD6.wav')

	for i in range(0, 3000):
		timedata.append(data[i*chunk:i*chunk+chunk])

	fs, data = read('training/trainingA6.wav')

	for i in range(0, 3000):
		timedata.append(data[i*chunk:i*chunk+chunk])	

	timedata = np.array(timedata)

	fftdata = []

	for row in timedata:																		#za svaki zvuk se racuna fft
		fftdata.append(calculatefft(fs, row)[0])

	amps = []	

	for row in fftdata:																			#uzimanje odgovarajucih amplituda za frekvencije
		#amps.append(row[round_freqs])
		amps.append(adaptivelocalmax(row, round_freqs))

	y = []
	for i in range(0, 3000):
		y.append([1, 0, 0, 0])

	for i in range(0, 3000):
		y.append([0, 1, 0, 0])

	for i in range(0, 3000):
		y.append([0, 0, 1, 0])

	for i in range(0, 3000):
		y.append([0, 0, 0, 1])

	x = np.array(amps)
	y = np.array(y)

	return x, y