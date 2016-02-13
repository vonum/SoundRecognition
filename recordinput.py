"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""

import pyaudio
import wave
import sys
import numpy as np

def recordandsave(filename):

	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 1
	RATE = 96000
	RECORD_SECONDS = 1
	WAVE_OUTPUT_FILENAME = filename

	p = pyaudio.PyAudio()

	stream = p.open(format=FORMAT,
					channels=CHANNELS,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK)

	print("* recording")

	frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		print len(data)
		frames.append(data)

	print("* done recording")

	print len(frames)

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)

	wf.setnframes(RATE*RECORD_SECONDS)

	wf.writeframes(b''.join(frames))
	wf.close()

def record(p, stream):

	CHUNK = 9600
	FORMAT = pyaudio.paInt16
	CHANNELS = 1
	RATE = 96000
	RECORD_SECONDS = 0.1

	frames = [] # A python-list of chunks(numpy.ndarray)
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	    data = stream.read(CHUNK)
	    frames.append(np.fromstring(data, dtype=np.int16))

	#Convert the list of numpy-arrays into a 1D array (column-wise)
	return np.hstack(frames)


if __name__ == '__main__':
	recordandsave(sys.argv[1])