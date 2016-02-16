from preparefortraining import prepare_data
from keras.models import Sequential
from keras.layers.core import Dense,Activation
from keras.optimizers import SGD
import sys
from scipy.io.wavfile import read
import numpy as np
from fft import calculatefft
from localmax import localmax
from ann import get_ann
from ann import create_and_train

test = np.array([264, 297, 330, 352, 396, 440, 495, 528, 594, 660, 704, 792, 880, 990, 1056])

T = 0.1
test = test * T
test = np.round(test, 0)

#freqs = np.array(np.exp(np.linspace(np.log(264), np.log(1056), 15)))
#round_freqs = np.round(freqs, 0)

ann = create_and_train()

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

