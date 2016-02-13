from keras.models import Sequential
from keras.layers.core import Dense,Activation
from keras.optimizers import SGD
from keras.models import model_from_json


def get_ann():
	ann = model_from_json(open('model/model.json').read())
	ann.load_weights('model/weights.h5')

	return ann

def create_and_train():

	test = np.array([264, 297, 330, 352, 396, 440, 495, 528, 594, 660, 704, 792, 880, 990, 1056])

	T = 0.1
	test = test * T
	test = np.round(test, 0)

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