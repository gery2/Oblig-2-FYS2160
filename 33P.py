#3.3
import numpy as np
import matplotlib.pyplot as plt

N = 100

T = [1, 0.95, 0.9, 0.8]

V = np.linspace(0.4, 6, N)

P0 = np.zeros(N)
P1 = np.zeros(N)
P2 = np.zeros(N)
P3 = np.zeros(N)

for i in range(N):
    P0[i] = 8*T[0]/(3*V[i] - 1) - 3/(V[i]**2)
    P1[i] = 8*T[1]/(3*V[i] - 1) - 3/(V[i]**2)
    P2[i] = 8*T[2]/(3*V[i] - 1) - 3/(V[i]**2)
    P3[i] = 8*T[3]/(3*V[i] - 1) - 3/(V[i]**2)

plt.title('Pressure P as function of V for V in the range from 0.4 to 6')
plt.plot(V, P0, label = 'T = 1.0')
plt.plot(V, P1, label = 'T = 0.95')
plt.plot(V, P2, label = 'T = 0.9')
plt.plot(V, P3, label = 'T = 0.8')
plt.xlabel('Volume V')
plt.ylabel('Pressure P')
plt.legend()
plt.show()
