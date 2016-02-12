from preparefortraining import prepare_data
from keras.models import Sequential
from keras.layers.core import Dense,Activation
from keras.optimizers import SGD
import sys
from scipy.io.wavfile import read
import numpy as np
from fft import calculatefft
from localmax import localmax

test = np.array([264, 297, 330, 352, 396, 440, 495, 528, 594, 660, 704, 792, 880, 990, 1056])

T = 0.1
test = test * T
test = np.round(test, 0)

freqs = np.array(np.exp(np.linspace(np.log(264), np.log(1056), 15)))
round_freqs = np.round(freqs, 0)

X, Y = prepare_data(sys.argv[1])

print X.shape

ann = Sequential()

ann.add(Dense(input_dim=15, output_dim=64,init="glorot_uniform"))
ann.add(Activation("sigmoid"))
#ann.add(Dense(input_dim=128, output_dim=128,init="glorot_uniform"))
#ann.add(Activation("sigmoid"))
ann.add(Dense(input_dim=64, output_dim=4,init="glorot_uniform"))
ann.add(Activation("sigmoid"))

# definisanje parametra algoritma za obucavanje
sgd = SGD(lr=0.01, momentum=0.9)
ann.compile(loss='mean_squared_error', optimizer=sgd)

ann.fit(X, Y, nb_epoch=5000, batch_size=90, verbose = 0, shuffle=False, show_accuracy = False)


amptest = []

fst, datat = read('440test.wav', mmap = False)
datat = datat[0:9600]
testfft = calculatefft(fst, datat)[0]
testfft = testfft/10000000000

#amptest.append(testfft[test.astype(np.int64)])
amptest.append(localmax(testfft, test.astype(np.int64)))

fst, datat = read('330test.wav', mmap = False)
datat = datat[0:9600]
testfft = calculatefft(fst, datat)[0]
testfft = testfft/10000000000

amptest.append(localmax(testfft, test.astype(np.int64)))

fst, datat = read('660test.wav', mmap = False)
datat = datat[0:9600]
testfft = calculatefft(fst, datat)[0]
#testfft = testfft/10000000000

amptest.append(localmax(testfft, test.astype(np.int64)))


#testing = []
#testing.append((amptest[0], amptest[1], amptest[2]))

print amptest

result = ann.predict(np.array((amptest[0], amptest[1], amptest[2])))
print result



#print amps[0]