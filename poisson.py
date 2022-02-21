#!/usr/bin/env python3
from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy
def factorial(n):
	fact = 1
	for item in range(1,n + 1):
		fact = fact * item
	return fact
def poisson_distribution(k, lambd, percent = False):
	a = (lambd ** k * numpy.exp(- lambd))
	b = factorial(k)
	if percent is False:
		return  a / b
	else:
		return a / b * 100

answer = poisson_distribution(5, lambd = 2)
answerper = poisson_distribution(5, lambd = 2, percent = True)

#print(round(answer, 4))
#print(round(answerper, 2), '%')
## test with https://hadrienj.github.io/posts/Essential-Math-poisson_distribution/
#print(answer == 0.03608940886309672)

# Let’s plot the distribution for various values of k:

lambd = 2

k_axis = numpy.arange(0, 25)
# >> [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24]

distribution = numpy.zeros(k_axis.shape[0])
# >> [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

for i in range(k_axis.shape[0]):
	distribution[i] = poisson.pmf(i, lambd)

# >> [1.35335283e-01 2.70670566e-01 2.70670566e-01 1.80447044e-01
# 9.02235222e-02 3.60894089e-02 1.20298030e-02 3.43708656e-03
# 8.59271640e-04 1.90949253e-04 3.81898506e-05 6.94360921e-06
# 1.15726820e-06 1.78041262e-07 2.54344660e-08 3.39126213e-09
# 4.23907766e-10 4.98715019e-11 5.54127799e-12 5.83292420e-13
# 5.83292420e-14 5.55516590e-15 5.05015082e-16 4.39143550e-17
# 3.65952958e-18]
	
plt.bar(k_axis, distribution)

f, axes = plt.subplots(6, figsize=(6, 8), sharex=True)

for lambd in range(1, 7):
	
	k_axis = numpy.arange(0, 20)
	distribution = numpy.zeros(k_axis.shape[0])
	for i in range(k_axis.shape[0]):
		distribution[i] = poisson.pmf(i, lambd)
		
	axes[lambd-1].bar(k_axis, distribution)
	axes[lambd-1].set_xticks(numpy.arange(0, 20, 2))
	axes[lambd-1].set_title(f"$\lambda$: {lambd}")


plt.show()
# [...] Add axes, labels...
