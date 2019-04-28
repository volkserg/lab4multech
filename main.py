from scipy.io import wavfile
import math

def openwave(filename):
    fs, data = wavfile.read(filename)
    return data

def dft(data):
    res = []
    N = len(data)
    summ = 0
    for k in range(N):
        print(k,N)
        for n in range(N):
            summ+=data[n]*complex(math.cos(2*math.pi*k*n/N), -math.sin(2*math.pi*k*n/N))
        print(summ)
        res.append(summ)
    return res