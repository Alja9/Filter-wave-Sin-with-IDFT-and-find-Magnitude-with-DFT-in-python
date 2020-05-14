import matplotlib.pyplot as plt
import numpy as np
import cmath as cmh

#Fungsi DFT
def DFT (x,N):
       i = len(x)

       j = cmh.sqrt(-1)
       X = []

       #w = np.linspace (0, 2*np.pi, N)
       for k in range(N):
              sum = 0
              for n in range(i):
                     sum = sum + (x[n]*(cmh.exp(((-j)*2*cmh.pi*n*k)/N)))
              X.append(sum)
       return(X)

#Fungsi Invers DFT
def IDFT(X):
	N=len(X) # 128
	j=cmh.sqrt(-1)
	x=[]
	i=3
	for n in range(N):
		sum=0
		for k in range(N):
			sum=sum+(X[k]*(cmh.exp((j*2*cmh.pi*n*k)/N)))
		x.append(sum/N)
	return(x)

#NAMA : ALDI JAYADI
#NIM  : 185150301111014
F = 4 
Fs = 128
N = Fs

t = np.arange(0,1,0.0078125)
#Stepnya berdasarkan max time / jumlah n jadi 1/128 = 0.0078125
print("t")
print(*t, sep = "\n")
print('----\n')

n = np.arange(0,128)
x = np.sin(2*np.pi*(F/Fs)*n)

#Clean x
plt.subplot(3,2,1)
plt.ylabel("x[n]")
plt.xlabel("t")
plt.xlim(0,1)
pertama, = plt.plot(t,x,color='b', label="Clean")
plt.legend(handles=[pertama], loc='upper right')
print("n[x]")
print(*x, sep = "\n")
print('----\n')

#Magnitude Clean x dengan DFT
plt.subplot(3,2,2)
plt.ylabel("MgX[w]")
plt.xlabel("t")
plt.xlim(0,1)
kedua, = plt.plot(t,np.abs(DFT(x,N)),color='b',label="Magnitude Clean")
plt.legend(handles=[kedua], loc='upper right')
print("Mg_n[x]")
print(*np.abs(DFT(x,N)), sep = "\n")
print('----\n')

xNoise = x + 0.5 *np.random.randn(len(x))
#Noise
plt.subplot(3,2,3)
plt.ylabel("x[n]")
plt.xlabel("t")
ketiga, = plt.plot(t,xNoise,color='g',label="Noise")
plt.legend(handles=[ketiga], loc='upper right')
print("Noise")
print(*xNoise, sep = "\n")
print('----\n')

#Magnitude Noise dengan DFT
plt.subplot(3,2,4)
plt.ylabel("MgNoise_X[w]")
plt.xlabel("t")
keempat, = plt.plot(t,np.abs(DFT(xNoise,N)),color='g',label="Magnitude Noise")
plt.legend(handles=[keempat], loc='upper right')
print("MgNoise")
print(*np.abs(DFT(xNoise,N)), sep = "\n")
print('----\n')

#x_Clean and Noise
plt.subplot(3,2,5)
plt.ylabel("x[n]")
plt.xlabel("t")
kelima, = plt.plot(t,x,color='b',label="Clean")
keenam, = plt.plot(t,xNoise,color='g',label="Noise")
plt.legend(handles=[kelima,keenam], loc='upper right')

#Filter menggunakan cara yang di contohkan di video :)
#Dan menggunakan metode Invers DFT untuk Clean Noise
dftKU = DFT(xNoise+x,N)
print("xNoise+x")
print(*dftKU, sep = "\n")
print('----\n')
PSD = dftKU * np.conj(dftKU)/len(n)
SinglSided = np.arange(1,np.floor(len(n)/2),dtype='int')
idc = PSD > 5 #Sebab Nilai NOISEnya memiliki perhitungan F/Fs yang membuat nilainya harus dikecilkan
PSDclean = PSD * idc
dftKU = idc * dftKU
dftFLT = IDFT(dftKU)

plt.subplot(3,2,6)
ketujuh, = plt.plot(t,dftFLT,color='r',label="Filter")
plt.legend(handles=[ketujuh], loc='upper right')

plt.show()
