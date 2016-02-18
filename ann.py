from keras.models import Sequential
from keras.layers.core import Dense,Activation
from keras.optimizers import SGD
from keras.models import model_from_json
import numpy as np
from preparefortraining import prepare_data
from preparefortraining import prepare_harder
from localmax import adaptivelocalmax
from scipy.io.wavfile import read
from fft import calculatefft


def get_ann():
	ann = model_from_json(open('model/modelfinal.json').read())
	ann.load_weights('model/weightsfinal.h5')

	return ann

def create_and_train():

	#test = np.array([264, 297, 330, 352, 396, 440, 495, 528, 594, 660, 704, 792, 880, 990, 1056])

	#T = 0.1
	#test = test * T
	#test = np.round(test, 0)

	X, Y = prepare_data()
	print X.shape

	ann = Sequential()

	ann.add(Dense(input_dim=15, output_dim=64,init="glorot_uniform"))
	ann.add(Activation("sigmoid"))
	ann.add(Dense(input_dim=64, output_dim=64,init="glorot_uniform"))
	ann.add(Activation("sigmoid"))
	ann.add(Dense(input_dim=64, output_dim=4,init="glorot_uniform"))
	ann.add(Activation("sigmoid"))

	# definisanje parametra algoritma za obucavanje
	sgd = SGD(lr=0.01, momentum=0.9)
	ann.compile(loss='mean_squared_error', optimizer=sgd)

	ann.fit(X, Y, nb_epoch=3000, batch_size=100, verbose = 0, shuffle=False, show_accuracy = False)

	json_string = ann.to_json()
	open('model/model2.json', 'w').write(json_string)
	ann.save_weights('model/weights2.h5')

	return ann

def train_harder():

	X, Y = prepare_harder()

	ann = Sequential()

	ann.add(Dense(input_dim=150, output_dim=64,init="glorot_uniform"))
	ann.add(Activation("sigmoid"))
	ann.add(Dense(input_dim=64, output_dim=64,init="glorot_uniform"))
	ann.add(Activation("sigmoid"))
	ann.add(Dense(input_dim=64, output_dim=4,init="glorot_uniform"))
	ann.add(Activation("sigmoid"))

	# definisanje parametra algoritma za obucavanje
	sgd = SGD(lr=0.01, momentum=0.9)
	ann.compile(loss='mean_squared_error', optimizer=sgd)

	ann.fit(X, Y, nb_epoch=2000, batch_size=500, verbose = 0, shuffle=False, show_accuracy = False)

	json_string = ann.to_json()
	open('model/modelfinal.json', 'w').write(json_string)
	ann.save_weights('model/weightsfinal.h5')

	return ann

def test_harder():

	freqs = np.array(np.exp(np.linspace(np.log(264), np.log(2000), 150)))
	round_freqs = np.round(freqs, 0)

	T = 0.1 #n/fs = 9600/96000
	chunk = 9600

	round_freqs = round_freqs * T #indeski frekvencija


	ann = model_from_json(open('model/modelfinal.json').read())
	ann.load_weights('model/weightsfinal.h5')

	amptest = []

	fst, datat = read('testA6.wav', mmap = False)
	datat = datat[0:9600]
	testfft = calculatefft(fst, datat)[0]

	#amptest.append(testfft[test.astype(np.int64)])
	amptest.append(adaptivelocalmax(testfft, round_freqs))

	fst, datat = read('testG4.wav', mmap = False)
	datat = datat[0:9600]
	testfft = calculatefft(fst, datat)[0]

	#amptest.append(testfft[test.astype(np.int64)])
	amptest.append(adaptivelocalmax(testfft, round_freqs))

	fst, datat = read('testF5.wav', mmap = False)
	datat = datat[0:9600]
	testfft = calculatefft(fst, datat)[0]

	#amptest.append(testfft[test.astype(np.int64)])
	amptest.append(adaptivelocalmax(testfft, round_freqs))

	fst, datat = read('testD6.wav', mmap = False)
	datat = datat[0:9600]
	testfft = calculatefft(fst, datat)[0]

	#amptest.append(testfft[test.astype(np.int64)])
	amptest.append(adaptivelocalmax(testfft, round_freqs))

	fst, datat = read('testB4.wav', mmap = False)
	datat = datat[0:9600]
	testfft = calculatefft(fst, datat)[0]

	#amptest.append(testfft[test.astype(np.int64)])
	amptest.append(adaptivelocalmax(testfft, round_freqs))

	result = ann.predict(np.array((amptest[0], amptest[1], amptest[2], amptest[3], amptest[4])))
	print result