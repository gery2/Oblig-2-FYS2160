#3.5
import numpy as np
import matplotlib.pyplot as plt

N = 100

T = [0.8, 0.9, 0.95, 1.0]

ρ = np.linspace(0, 2, N)

P0 = np.zeros(N)
P1 = np.zeros(N)
P2 = np.zeros(N)
P3 = np.zeros(N)

for i in range(N):
    P0[i] = 8*ρ[i]*T[0]/(3 - ρ[i]) - 3*ρ[i]**2
    P1[i] = 8*ρ[i]*T[1]/(3 - ρ[i]) - 3*ρ[i]**2
    P2[i] = 8*ρ[i]*T[2]/(3 - ρ[i]) - 3*ρ[i]**2
    P3[i] = 8*ρ[i]*T[3]/(3 - ρ[i]) - 3*ρ[i]**2

plt.title('Pressure P as function of ρ for ρ in the range from 0 to 2')
plt.plot(ρ, P0, label = 'T = 0.8')
plt.plot(ρ, P1, label = 'T = 0.9')
plt.plot(ρ, P2, label = 'T = 0.95')
plt.plot(ρ, P3, label = 'T = 1.0')
plt.xlabel('Density ρ')
plt.ylabel('Pressure P')
plt.legend()
plt.show()
