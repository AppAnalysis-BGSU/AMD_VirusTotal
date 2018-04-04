import numpy as np
import matplotlib.pyplot as plt

group = ("time<20 seconds") 

time=[1,2,5,10,100,100,100,100,200,300,1]

for i  in range(1,100):
	time.append(i)

for j in range(1,10):
	time.append(50)
 
# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, axisbg="1.0")
 
for x in time:
	ax.scatter(x, 0, alpha=0.4, c="red", edgecolors='none', s=5)
 
plt.title('Execution time of LockScreen Plugin')
plt.legend(loc=2)
plt.show()