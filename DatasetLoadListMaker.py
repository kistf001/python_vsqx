import numpy as np

FinishedPosition = np.array([0])

ad = np.random.randint( 0,150000*15 , 150000*15*2)

hap = np.hstack([FinishedPosition,ad])

np.save("Array", hap)

print(hap.shape)