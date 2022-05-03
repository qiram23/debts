import numpy as np
import matplotlib.pyplot as plt

with open("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]

data_array = np.loadtxt("data.txt", dtype=int)
volt_data = data_array / 2**8 * 3.3

aaa = data_array * tmp[1]
x = [i*tmp[0] for i in range(len(data_array))]
total_time = tmp[0]*len(data_array)

fig, ax=plt.subplots(figsize=(16,10),dpi=200)
ax.set_title('Процесс заряда и разряда конденсатора в RC-цепочке', fontsize = 10)
ax.set_xlabel('Время, с')
ax.set_ylabel('Напряжение, В')
ax.plot(x, volt_data, label = 'V(t)', marker = 'o', markersize=2, markerfacecolor = 'darkgreen', linewidth = 1, color = 'green')
plt.legend()
maxq = np.argmax(volt_data)

ax.text(8, 2.2, 'Время заряда = {:.2f} с'.format(x[maxq]), fontsize = 7.5)
ax.text(8, 1.2, 'Время заряда = {:.2f} с'.format(total_time - x[maxq]), fontsize = 7.5)
plt.xlim(0, 12.5)
plt.ylim(0,3.5)
ax.minorticks_on()
ax.grid(which='major', linewidth = 1)
ax.grid(which = 'minor', linestyle = ':', linewidth = 0.5)
plt.show()
fig.savefig('мой график.svg')