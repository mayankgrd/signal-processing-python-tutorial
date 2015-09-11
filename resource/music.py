from numpy import sin, linspace, pi 

import numpy as np 
from scipy.io.wavfile import write
from pylab import plot,show,axis


def soundsc(sound, rate=44100, filename='sound.wav'):
	baseAmpl = 10000.0; 
	data = (baseAmpl*sound).astype(np.int16)
	write(filename, rate, data)





# A tone, 2 seconds, 44100 samples per second

# specify sampling rate of sound card 
rate =44100 

# what frequency of sound you want to generate 
freq = 440 

# Define the time axis 
t = np.linspace(0,4,4*rate) 

# Generate the sound (Replace this with your function), the amplitude should be between +/- 1

sound = np.sin(2*np.pi*freq*t)


# Generate wave file, rate defaults to 44100  
soundsc(sound, rate)



# just some random plots 

plot(t,sound)
axis([0,0.05,np.min(sound),np.max(sound)])
show() 