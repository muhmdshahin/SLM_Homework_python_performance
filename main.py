import matplotlib.pyplot as plt
import numpy
import time
from scipy.stats import linregress


def r_squared(n):
    x = numpy.random.normal(loc=0.0, scale=1.0, size=n)
    y = 1 + x + numpy.random.normal(loc=0.0, scale=1.0, size=n)
    res = linregress(x, y)
    return res.rvalue**2


sizes = list(range(10, 200, 10))
reps = 10000

r_squared_q95 = numpy.zeros(len(sizes))
r_squared_q5 = numpy.zeros(len(sizes))
r_squared_mean = numpy.zeros(len(sizes))
start_time = time.time()
for idx, val in enumerate(sizes):
    print(idx, val)
    result = [r_squared(val) for _ in range(reps)]
    r_squared_mean[idx] = numpy.mean(result)
    r_squared_q5[idx] = numpy.quantile(result, 0.05)
    r_squared_q95[idx] = numpy.quantile(result, 0.95)


print("--- %s seconds ---" % (time.time() - start_time))
plt.ylim([min(r_squared_q5), max(r_squared_q95)])
plt.scatter(sizes, r_squared_mean)
plt.plot(sizes, r_squared_q5)
plt.plot(sizes, r_squared_q95)
plt.show()
