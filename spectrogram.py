#!/usr/bin/env python3

import argparse
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
import soundfile as sf


parser = argparse.ArgumentParser(description="spectrogram")
parser.add_argument("--show", help="shows plot", action="store_true")
parser.add_argument("-y", "--ylim", help="limit freq on y axis", type=int)
parser.add_argument("realtimePlaybackFile", help="realtimePlayback wav file")
arguments = parser.parse_args()

def plot(realtimePlaybackFile):
    plt.figure(figsize=(16,9))
    plt.pcolormesh(realtimePlaybackFile[1]
    , realtimePlaybackFile[0]
    , np.log(realtimePlaybackFile[2]))
    if arguments.ylim:
        plt.ylim((0, int(arguments.ylim)))
    plt.title('Spectrogram')
    plt.ylabel('frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.savefig('spectrogram_'
    +arguments.realtimePlaybackFile+'.png', orientation='landscape', dpi = 300)
    if arguments.show:
        plt.show()

def toArray(filename):
    return  sf.read(filename)

def spectrogram(data):
    return signal.spectrogram(data[0], fs=data[1], nperseg=1024)

realtimePlaybackFile = spectrogram(toArray(arguments.realtimePlaybackFile))
plot(realtimePlaybackFile)
