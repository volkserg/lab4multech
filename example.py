from main import *


data = openwave('4.wav')
L = data[:, 0]
R = data[:, 1]

dat = [1, 2, 5, 7]

d = DFT(dat)
print(d)

und = invertDFT(d)
print(und)

print(windowDFT([1, 2, 5, 7]))