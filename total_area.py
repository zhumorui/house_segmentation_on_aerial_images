import numpy as np
import matplotlib.pyplot as plt

txtfiles = [["2010_v1.txt","2014_v1.txt","2017_v1.txt","2021_v1.txt"],["2010_v2.txt","2014_v2.txt","2017_v2.txt","2021_v2.txt"]]

data = []

for version in txtfiles:
    year_data = np.array([])
    for txtfile in version:
        with open(txtfile, 'r') as f:
            lines = f.readlines()
            areas = 0
            for line in lines:
                second_row = line.split(',')[0]
                areas += int(second_row)
                x = (areas * 0.51 * 0.51)/1000000
        year_data = np.append(year_data, x)
    data.append(year_data)

x = np.array([2010, 2014, 2017, 2021])

fig, ax = plt.subplots()
ax.plot(x, data[0])
plt.show()
