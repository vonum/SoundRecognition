from preparefortraining import prepare_data
from keras.models import Sequential
from keras.layers.core import Dense,Activation
from keras.optimizers import SGD
import sys
from scipy.io.wavfile import read
import numpy as np
from fft import calculatefft

X, Y = prepare_data(sys.argv[1])

print X.shape

ann = Sequential()

ann.add(Dense(input_dim=50, output_dim=64,init="glorot_uniform"))
ann.add(Activation("sigmoid"))
#ann.add(Dense(input_dim=128, output_dim=128,init="glorot_uniform"))
#ann.add(Activation("sigmoid"))
ann.add(Dense(input_dim=64, output_dim=4,init="glorot_uniform"))
ann.add(Activation("sigmoid"))

# definisanje parametra algoritma za obucavanje
sgd = SGD(lr=0.01, momentum=0.9)
ann.compile(loss='mean_squared_error', optimizer=sgd)

ann.fit(X, Y, nb_epoch=100, batch_size=90, verbose = 0, shuffle=False, show_accuracy = False)


fst, datat = read('test.wav', mmap = False)
testfft = calculatefft(fst, datat)[0]
testfft = testfft / np.amax(testfft) ** 10

freqs = np.array(np.exp(np.linspace(np.log(264), np.log(1056), 50)))
round_freqs = np.round(freqs, 0)

#####
#freq = np.array([399])

amptest = []
amptest.append(testfft[round_freqs.astype(np.int64)])
#amptest.append(testfft[freq])

test = []
test.append(amptest[0])

print amptest

result = ann.predict(np.array(test))
print result



#print amps[0]