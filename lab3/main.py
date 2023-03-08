import numpy as np
import matplotlib.pyplot as plt
import random
   
'''
Метод усечения (truncation method) - это один из способов генерации случайных чисел в заданном диапазоне, который основывается на усечении дробной части случайного вещественного числа. Этот метод генерирует равномерно распределенные случайные числа в интервале [a, b], где a и b - концы интервала.
Для генерации случайных чисел методом усечения можно использовать функцию random() модуля random библиотеки Python. Эта функция возвращает случайное вещественное число в интервале [0.0, 1.0).

Для получения случайного целого числа в интервале [a, b] с помощью метода усечения нужно выполнить следующие шаги:

1.Сгенерировать случайное вещественное число x в интервале [a, b+1).
2.Получить целое число y из x, отбросив дробную часть и вычтя a: y = int(x) - a.
3.Если y <= (b - a), то y является искомым случайным числом. Иначе повторить шаги 1-3.

Вот пример реализации этого метода на Python:

Здесь функция truncation_random(a, b) принимает на вход два параметра: концы интервала [a, b].
Внутри функции выполняется бесконечный цикл, пока не будет сгенерировано искомое случайное число.
В этом цикле сначала генерируется случайное вещественное число x в интервале [a, b+1), 
затем отбрасывается дробная часть и вычитается a, чтобы получить целое число y.
Если y находится в интервале [0, b-a], то оно является искомым случайным числом, и функция его возвращает с помощью оператора return.
Если y находится вне этого интервала, то цикл продолжается и генерируется новое случайное число.
'''

def truncation_random(a, b):
    while True:
        x = random.uniform(a, b+1)
        y = int(x) - a
        if y <= (b - a):
            return y


random_numbers_trunc = [truncation_random(0, 10) for _ in range(1000)]

plt.hist(sorted(random_numbers_trunc), bins=21, range=[-0.5, 10.5])
plt.xlabel('Random number')
plt.ylabel('Count')
plt.title('Truncation method')
plt.show()

# генерация случайного числа в интервале [a, b]
def random_sampling(a, b):
    return random.choice(range(a, b+1))

# пример генерации 10 случайных чисел в интервале [1, 100]
random_numbers_sampling = [random_sampling(0, 10) for _ in range(100000)]
print(random_numbers_sampling)
plt.hist(sorted(random_numbers_sampling), bins=21, range=[-0.5, 10.5])
plt.xlabel('Random number')
plt.ylabel('Count')
plt.title('Random sampling')
plt.show()

# Пример 1: Метод обратной функции

# Метод обратной функции - это метод генерации случайной величины с 
# использованием обратной функции распределения. Данный метод основан на том факте, 
# что если X - случайная величина с функцией распределения F(x), то Y = F^(-1)(U), где U - равномерно распределенная 
# на [0,1] случайная величина, будет иметь функцию распределения F(x).

# Для демонстрации данного метода сгенерируем случайную величину с экспоненциальным распределением.



# Функция обратной функции распределения экспоненциального распределения
def inv_exp_cdf(u, lambda_=1):
    return -np.log(1-u)/lambda_

# Генерация случайной величины с помощью метода обратной функции
n = 100000
U = np.random.uniform(size=n)
X = inv_exp_cdf(U)

# Построение гистограммы сравнения с теоретической плотностью распределения
x = np.linspace(0, 5, 10000)
y = lambda x: np.exp(-x)
plt.hist(X, density=True, bins=20)
plt.plot(x, y(x), 'r--', linewidth=2)
plt.show()



'''

Inverse transform sampling (ITS) is a method of generating random numbers from a given probability distribution. The method is based on the observation that if a random variable X has a cumulative distribution function (CDF) F(x), then the random variable Y=F(X) has a uniform distribution on the interval [0,1].

The method of ITS involves the following steps:

Compute the inverse of the CDF, F^-1(y), where y is a random number generated from a uniform distribution on the interval [0,1].
Generate a random number y from a uniform distribution on the interval [0,1].
Compute x=F^-1(y), which is a random number from the distribution with CDF F(x).
This method works for any distribution, as long as the CDF is invertible.
 The advantage of ITS is that it can be used to generate random numbers from any distribution, even if the probability density function is not easy to work with.

One limitation of ITS is that it can be computationally expensive to compute the inverse CDF for some distributions. 
In such cases, alternative methods like rejection sampling or Markov chain Monte Carlo methods may be more appropriate. 
Additionally, ITS may not be the best choice for generating a large number of random numbers, as it can be slow and may require a large number of evaluations of the inverse CDF.

Overall, ITS is a powerful method for generating random numbers from arbitrary distributions, and is widely used in various fields such as statistics, physics, and finance.'''




# define the exponential distribution
def exponential(x, beta):
    return 1/beta * np.exp(-x/beta)

# define the inverse CDF of the exponential distribution
def inverse_cdf(y, beta):
    return -beta * np.log(1-y)

# generate random numbers from the exponential distribution using ITS
def generate_exponential(N, beta):
    # generate random numbers from a uniform distribution
    y = np.random.rand(N)
    # apply the inverse CDF to transform the uniform numbers into exponential numbers
    x = inverse_cdf(y, beta)
    return x

# set the parameters of the distribution and generate random numbers
beta = 1.0
N = 1000
samples = generate_exponential(N, beta)

# plot the histogram of the generated samples
plt.hist(samples, bins=30, density=True, alpha=0.7, label='Samples')

# plot the theoretical distribution for comparison
x = np.linspace(0, 10, 100)
y = exponential(x, beta)
plt.plot(x, y, 'r-', label='Exponential PDF')
plt.legend()

plt.show()