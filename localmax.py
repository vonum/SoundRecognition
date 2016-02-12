import numpy as np

def localmax(data, freqs):

	amps = []

	for val in freqs:
		amps.append(np.amax(data[val - 1:val + 1]))

	return np.array(amps)



