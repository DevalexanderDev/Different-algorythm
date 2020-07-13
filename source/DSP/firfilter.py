import math
import matplotlib.pyplot as plt
import numpy as np

def firfilter(b,x):
	N = len(x)
	L = len(b)

	y = [0 for i in range(N)]
	r = [0 for i in range(L)]

	for n in range(N):
		for k in reversed(range(1,L)):
			r[k] = r[k-1]
			y[n] = y[n] + r[k] * b[k]
		r[0] = x[n]
		y[n] = y[n] + r[0] * b[0]

	return y

k = [
	-0.0015122859296948122,
	-0.008673685955236262,
	-0.0066718510881530685,
	-0.009828857589841512,
	-0.011962821884640507,
	-0.01404382747618891,
	-0.015613026216626299,
	-0.016503754577730415,
	-0.016528215651673114,
	-0.01556687620775217,
	-0.013586730843546432,
	-0.010646242803231006,
	-0.006899394829000263,
	-0.0026031366165265033,
	0.0018946468270584359,
	0.006202014809063863,
	0.009905875457182729,
	0.012601336433342367,
	0.013957379671344486,
	0.013745830410612881,
	0.01186553566998625,
	0.008392869122116505,
	0.0035754189463261367,
	-0.0021836122086230374,
	-0.008320288850026053,
	-0.014188786504108413,
	-0.019077473388968185,
	-0.02229043119703793,
	-0.023217579274260734,
	-0.021368623557291033,
	-0.01647295413479255,
	-0.008468593693775183,
	0.002433813886379394,
	0.015789620403025693,
	0.030910931693122676,
	0.04694092669271672,
	0.0628945820944888,
	0.07774596130295504,
	0.09051066448819982,
	0.10031764887117778,
	0.10649011783401166,
	0.10859762489358087,
	0.10649011783401166,
	0.10031764887117778,
	0.09051066448819982,
	0.07774596130295504,
	0.0628945820944888,
	0.04694092669271672,
	0.030910931693122676,
	0.015789620403025693,
	0.002433813886379394,
	-0.008468593693775183,
	-0.01647295413479255,
	-0.021368623557291033,
	-0.023217579274260734,
	-0.02229043119703793,
	-0.019077473388968185,
	-0.014188786504108413,
	-0.008320288850026053,
	-0.0021836122086230374,
	0.0035754189463261367,
	0.008392869122116505,
	0.01186553566998625,
	0.013745830410612881,
	0.013957379671344486,
	0.012601336433342367,
	0.009905875457182729,
	0.006202014809063863,
	0.0018946468270584359,
	-0.0026031366165265033,
	-0.006899394829000263,
	-0.010646242803231006,
	-0.013586730843546432,
	-0.01556687620775217,
	-0.016528215651673114,
	-0.016503754577730415,
	-0.015613026216626299,
	-0.01404382747618891,
	-0.011962821884640507,
	-0.009828857589841512,
	-0.0066718510881530685,
	-0.008673685955236262,
	-0.0015122859296948122
]

num_period = 20
sample_rate = 8000
freq = 450

x = [math.sin(2*math.pi*freq*i/sample_rate) for i in range(int(num_period*sample_rate/freq))]

y = firfilter(k, x)

plt.figure(figsize=(9,9))
plt.subplot(5,1,1)
plt.plot(range(len(x)), x)
plt.title('Изначальный сигнал')
plt.ylabel("Амплитуда")
plt.xlabel("Время")
plt.grid(True)

plt.subplot(5,1,2)
plt.plot(range(len(y)), y)
plt.title('Изначальный сигнал пропущенный через фильтр')
plt.ylabel("Амплитуда")
plt.xlabel("Время")
plt.grid(True)

x = [0 for i in range(len(k) + 3)]
x[0] = 1
y = firfilter(k, x)

plt.subplot(5,1,3)
plt.plot(range(len(y)), y)
plt.title('Импульсная характеристика фильтра')
plt.ylabel("Амплитуда")
plt.xlabel("Время")
plt.grid(True)

plt.show()