import numpy as np
import matplotlib.pyplot as plt
from random import random
from random import seed
from random import randint
seed(1)
# зададим начальные условия
N = 1000     # начальная численность популяции
r = 0.35      # коэффициент рождаемости
d = 0.25      # коэффициент смертности
K = 11000     # предельная численность популяции

# задаем шаг по времени и количество шагов
dt = 0.1     # шаг по времени
num_steps = 10000   # количество шагов

# создаем массивы для хранения времени и численности популяции
time = np.arange(num_steps)*dt

# вычисляем численность популяции на каждом шаге для каждого начального значения
for i in range(10):
    
    N = randint(1000, 10000)
    # Только для вывода в легенде ниже
    N0=N
    population = np.zeros(num_steps)
    population[0] = N
    # Рандомим начальные коэффициенты
    r = random()
    d = random()
    for j in range(1, num_steps):
        rN = r*N
        dN = d*N
        dNdt = rN*(1 - N/K) - dN
        N += dNdt*dt
        if N < 0:
            N = 0
        population[j] = N

    # выводим график численности популяции по времени
    plt.plot(time, population, label='N0 = {:.0f}, R={:.2f}, D={:.2f}'.format( N0, r,d))

# задаем параметры графика
plt.xlim([0, num_steps*dt + 100])
plt.ylim([0, K+1000])
plt.xlabel('Время')
plt.ylabel('Численность популяции')
plt.legend()
plt.show()