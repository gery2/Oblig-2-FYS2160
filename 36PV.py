#3.6
import numpy as np
import matplotlib.pyplot as plt

N = 100

T = [77, 100, 110, 115, 120, 125] # K
V = np.linspace(0.4, 6, N)

Tc = 126 # K
Vc = 0.089 # l/mol
Pc = 33.6 # atm

P0_hat = np.zeros(N)
P1_hat = np.zeros(N)
P2_hat = np.zeros(N)
P3_hat = np.zeros(N)
P4_hat = np.zeros(N)
P5_hat = np.zeros(N)

T_hat = [x / Tc for x in T]
V_hat = [x / Vc for x in V]

for i in range(N):
    P0_hat[i] = 8*T_hat[0]/(3*V_hat[i] - 1) - 3/(V_hat[i]**2)
    P1_hat[i] = 8*T_hat[1]/(3*V_hat[i] - 1) - 3/(V_hat[i]**2)
    P2_hat[i] = 8*T_hat[2]/(3*V_hat[i] - 1) - 3/(V_hat[i]**2)
    P3_hat[i] = 8*T_hat[3]/(3*V_hat[i] - 1) - 3/(V_hat[i]**2)
    P4_hat[i] = 8*T_hat[4]/(3*V_hat[i] - 1) - 3/(V_hat[i]**2)
    P5_hat[i] = 8*T_hat[5]/(3*V_hat[i] - 1) - 3/(V_hat[i]**2)

plt.title('The PV isotherms of a nitrogen gas')
plt.plot(V_hat, P0_hat, label = 'T/Tc = %g' % T_hat[0])
plt.plot(V_hat, P1_hat, label = 'T/Tc = %g' % T_hat[1])
plt.plot(V_hat, P2_hat, label = 'T/Tc = %g' % T_hat[2])
plt.plot(V_hat, P3_hat, label = 'T/Tc = %g' % T_hat[3])
plt.plot(V_hat, P4_hat, label = 'T/Tc = %g' % T_hat[4])
plt.plot(V_hat, P5_hat, label = 'T/Tc = %g' % T_hat[5])
plt.xlabel('Volume V/Vc')
plt.ylabel('Pressure P/Pc')
plt.legend()
plt.show()
