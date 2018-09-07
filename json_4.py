import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab


 # x=[1,4,6,3]
# y=[5,9,11,2]

# x=[21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,48,50,100]

# to hold value bars for data
# num_bins=5

#  n,bins,patches=plt.hist(x,num_bins,facecolor='blue',edgecolor='black', linewidth=1.2,alpha=0.4)


  # plt.plot(x,y)

# plt.show()

# -------------------------------------------------------------
# create a pie chat now
labels = 'Python', 'C++', 'Ruby', 'Java'
# labels = 'chocolate','tea','coffee','milk'
sizes = [215,300,550,100]

colors=['gold','lightcoral','yellowgreen','lightskyblue']
explode=(0.1,0,0,0)

plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)

plt.axis('equal')
plt.show();
