#from __future__ import print_function, division
#
#import os
#import copy
#
#import scipy.io.wavfile as wav
#
#import numpy as np
#
#def dummyRemover(signal,Bar):
#  
#  # 신호의 길이/(파라메터 1 마디의 수 * 샘플링레이트는 파라메터보다 20배 더 큼)
#  
#  # 더미신호 4마디만큼 잘라냄
#  signal = signal[ int( 1920*4*20 ) : int(1920*(Bar+4)*20) ]
#  
#return signal

import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 64, 4 # mean and standard deviation

buffer = np.zeros((128))
for ss in range(0, 128):
  buffer[ss] = int((1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (ss - mu)**2 / (2 * sigma**2) ))*100)
print(buffer)