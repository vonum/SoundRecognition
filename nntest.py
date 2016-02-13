from preparefortraining import prepare_data
from keras.models import Sequential
from keras.layers.core import Dense,Activation
from keras.optimizers import SGD
import sys
from scipy.io.wavfile import read
import numpy as np
from fft import calculatefft
from localmax import localmax
from keras.models import model_from_json

test = np.array([264, 297, 330, 352, 396, 440, 495, 528, 594, 660, 704, 792, 880, 990, 1056])

T = 0.1
test = test * T
test = np.round(test, 0)

freqs = np.array(np.exp(np.linspace(np.log(264), np.log(1056), 15)))
round_freqs = np.round(freqs, 0)

#X, Y = prepare_data()

#print X.shape

ann = model_from_json(open('model/model.json').read())
ann.load_weights('model/weights.h5')

#ann = Sequential()

#ann.add(Dense(input_dim=15, output_dim=64,init="glorot_uniform"))
#ann.add(Activation("sigmoid"))
#ann.add(Dense(input_dim=64, output_dim=64,init="glorot_uniform"))
#ann.add(Activation("sigmoid"))
#ann.add(Dense(input_dim=64, output_dim=4,init="glorot_uniform"))
#ann.add(Activation("sigmoid"))

# definisanje parametra algoritma za obucavanje
#sgd = SGD(lr=0.01, momentum=0.9)
#ann.compile(loss='mean_squared_error', optimizer=sgd)

#ann.fit(X, Y, nb_epoch=3000, batch_size=100, verbose = 0, shuffle=False, show_accuracy = False)

#json_string = ann.to_json()
#open('model/model.json', 'w').write(json_string)
#ann.save_weights('model/weights.h5')

amptest = []

fst, datat = read('test/200test.wav', mmap = False)
datat = datat[0:9600]
testfft = calculatefft(fst, datat)[0]
#testfft = testfft/10000000000

#amptest.append(testfft[test.astype(np.int64)])
amptest.append(localmax(testfft, test.astype(np.int64)))

fst, datat = read('test/330test.wav', mmap = False)
datat = datat[0:9600]
testfft = calculatefft(fst, datat)[0]
#testfft = testfft/10000000000

#amptest.append(testfft[test.astype(np.int64)])
amptest.append(localmax(testfft, test.astype(np.int64)))

fst, datat = read('test/400test.wav', mmap = False)
datat = datat[0:9600]
testfft = calculatefft(fst, datat)[0]
#testfft = testfft/10000000000

#amptest.append(testfft[test.astype(np.int64)])
amptest.append(localmax(testfft, test.astype(np.int64)))

fst, datat = read('test/440test.wav', mmap = False)
datat = datat[0:9600]
testfft = calculatefft(fst, datat)[0]
#testfft = testfft/10000000000

#amptest.append(testfft[test.astype(np.int64)])
amptest.append(localmax(testfft, test.astype(np.int64)))

fst, datat = read('test/500test.wav', mmap = False)
datat = datat[0:9600]
testfft = calculatefft(fst, datat)[0]
#testfft = testfft/10000000000

amptest.append(localmax(testfft, test.astype(np.int64)))

fst, datat = read('test/600test.wav', mmap = False)
datat = datat[0:9600]
testfft = calculatefft(fst, datat)[0]
#testfft = testfft/10000000000

amptest.append(localmax(testfft, test.astype(np.int64)))

fst, datat = read('test/660test.wav', mmap = False)
datat = datat[0:9600]
testfft = calculatefft(fst, datat)[0]
#testfft = testfft/10000000000

amptest.append(localmax(testfft, test.astype(np.int64)))

fst, datat = read('test/700test.wav', mmap = False)
datat = datat[0:9600]
testfft = calculatefft(fst, datat)[0]
#testfft = testfft/10000000000

amptest.append(localmax(testfft, test.astype(np.int64)))

fst, datat = read('test/800test.wav', mmap = False)
datat = datat[0:9600]
testfft = calculatefft(fst, datat)[0]
#testfft = testfft/10000000000

amptest.append(localmax(testfft, test.astype(np.int64)))

fst, datat = read('test/1000test.wav', mmap = False)
datat = datat[0:9600]
testfft = calculatefft(fst, datat)[0]

amptest.append(localmax(testfft, test.astype(np.int64)))

fst, datat = read('test/nosoundtest.wav', mmap = False)
datat = datat[0:9600]
testfft = calculatefft(fst, datat)[0]
#testfft = testfft/10000000000

amptest.append(localmax(testfft, test.astype(np.int64)))

fst, datat = read('test/330-440test.wav', mmap = False)
datat = datat[0:9600]
testfft = calculatefft(fst, datat)[0]
#testfft = testfft/10000000000

amptest.append(localmax(testfft, test.astype(np.int64)))

fst, datat = read('test/440-660test.wav', mmap = False)
datat = datat[0:9600]
testfft = calculatefft(fst, datat)[0]
#testfft = testfft/10000000000

amptest.append(localmax(testfft, test.astype(np.int64)))

fst, datat = read('test/kis.wav', mmap = False)
datat = datat[0:9600]
testfft = calculatefft(fst, datat)[0]
#testfft = testfft/10000000000

amptest.append(localmax(testfft, test.astype(np.int64)))

fst, datat = read('test/git440.wav', mmap = False)
datat = datat[0:9600]
testfft = calculatefft(fst, datat)[0]
#testfft = testfft/10000000000

amptest.append(localmax(testfft, test.astype(np.int64)))

fst, datat = read('test/git660.wav', mmap = False)
datat = datat[0:9600]
testfft = calculatefft(fst, datat)[0]
#testfft = testfft/10000000000

amptest.append(localmax(testfft, test.astype(np.int64)))

#testing = []
#testing.append((amptest[0], amptest[1], amptest[2]))

result = ann.predict(np.array((amptest[0], amptest[1], amptest[2], amptest[3], amptest[4], amptest[5], amptest[6], amptest[7], amptest[8], amptest[9], amptest[10], amptest[11], amptest[12], amptest[13], amptest[14])))
print result



#print amps[0]