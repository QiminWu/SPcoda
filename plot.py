## This is an Script to plot an spectrogram of seismic data
## Using python and Obspy
### Esteban J. Chaves - UC Santa Cruz - 2014


import matplotlib.pyplot as plt
from obspy.core import read
from obspy.imaging.spectrogram import spectrogram
import numpy as np


st = read('indi_saju.bhz.sac') # Reading the waveform in SAC format
print(st)

fig = plt.figure()
ax = fig.add_subplot(111)
spectrogram(st[0].data, st[0].stats.sampling_rate,wlen=5.,axes=ax,log=True)
ax.set_ylim(0.1,3)
ax.set_xlabel('Time [s]')
ax.set_ylabel('Frequency [Hz]')
fig.savefig('SPEC.ps')
#plt.show()


