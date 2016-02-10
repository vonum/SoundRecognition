# keras
from keras.models import Sequential
from keras.layers.core import Dense,Activation
from keras.optimizers import SGD
import numpy as np

ann = Sequential()

ann.add(Dense(input_dim=5, output_dim=64,init="glorot_uniform"))
ann.add(Activation("sigmoid"))
ann.add(Dense(input_dim=64, output_dim=1,init="glorot_uniform"))
ann.add(Activation("sigmoid"))

# definisanje parametra algoritma za obucavanje
sgd = SGD(lr=0.01, momentum=0.9)
ann.compile(loss='mean_squared_error', optimizer=sgd)

# obucavanje neuronske mreze
x = []
x.append([1, 2, 3, 4, 5])
x.append([1, 2, 3, 3, 5])
x.append([2, 2, 3, 4, 5])
X = np.array(x)
y = []
y.append([1])
y.append([1])
y.append([1])
Y = np.array(y)
print X, Y
ann.fit(X, Y, nb_epoch=500, batch_size=1, verbose = 0, shuffle=False, show_accuracy = False)

t = []
t.append([25115, -15225, 13, 25155, -241])
test = np.array(t)

res = ann.predict(test)
print res