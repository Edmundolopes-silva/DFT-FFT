import numpy as np
import matplotlib.pyplot as plt

fs = 8000  #taxa de amostragem
ts=1/fs;   #tempo de amostragem 
f1=1000;   #frequência de 1000HZ
f2=2000;   #frequência de 2000HZ
N=16;      #número de amostras
#m=0:16;    %índice da componente de saída da DFT

t = np.linspace(0,(N-1)*ts,N)
fstep = (fs/N)
f = np.linspace(0,(N-1)*fstep,N)

y = (1 * np.sin(2*np.pi*f1*t) + 0.5 * np.sin(2*np.pi*f2*t + (3*np.pi/4))) # Signal

X = np.fft.fft(y);
X_mag = np.abs(X) / N

fig1, ax1 = plt.subplots(nrows=1,ncols=1)
ax1.stem(t,y)
plt.show()
#plt.savefig('ts.png')  #save

fig1, ax2 = plt.subplots(nrows=1,ncols=1)
ax2.stem(f,X_mag)
plt.show()
#plt.savefig('fft.png')  #save
