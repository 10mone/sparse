import math
import numpy as np
import matplotlib.pyplot as plt

def draw(x):
    tt = 0
    result_value = []
    true_value = []
    while tt<10.1:
        temp_value = x[0]*(tt**10)+x[1]*(tt**9)+x[2]*(tt**8)+x[3]*(tt**7)+x[4]*(tt**6)+x[5]*(tt**5)+x[6]*(tt**4)+x[7]*(tt**3)+x[8]*(tt**2)+x[9]*tt+x[10]
        result_value.append(temp_value)
        true_value.append(math.sin(tt))
        tt += 0.1
    return result_value, true_value


t = [i for i in range(0,11)]
y = []
true_value = []

for i in t:
    noise = np.random.normal(loc=0, scale=0.2)
    y.append(math.sin(i)+noise)

t = np.array(t)
y = np.array(y)

phi = np.vander(t)
x = np.dot(np.linalg.inv(phi), y.T)

result,true_value = draw(x)

ax = plt.subplot()
plt.plot(result, color='blue')
#plt.plot(y, color='blue', marker='o')
plt.plot(true_value, color='red', linestyle='dashed')
ax.set_xlim(0.0, 100.0)
ax.set_ylim(-2.0, 2.0)
plt.show()
