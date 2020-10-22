

# basic inversion gibbs sampler 
# 'warm-up' 

import numpy as np

from matplotlib import pyplot as plt

# gibbs sampling - inversion method

# use bivariate distribution
# iterate through conditional distributions ( in this case, only 2 conditionals)
# we start with this case and will work our way up to a 'network' of distribution

# let f(x,y) = (1/28)*(2x + 3y + 2)


# some arbitrary starting value for our paramters
x = np.full((2000,1),-5.0)
y = np.full((2000,1),-5.0)


for i in range(2,2000):
# sample from x | y

    u=np.random.rand()

    x[i]=np.sqrt(u*(6*y[i-1]+8)+(1.5*y[i-1]+1)*(1.5*y[i-1]+1)) - (1.5*y[i-1]+1)
    #print(x[i])
    u=np.random.rand()
    y[i]=np.sqrt((2*u*(4*x[i]+10))/3 + ((2*x[i]+2)/3)*((2*x[i]+2)/3)) - ((2*x[i]+2)/3)


plt.plot(x,y)
plt.show()
