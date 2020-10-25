# rejection sampling example

import numpy as np

from matplotlib import pyplot as plt


# f(x) = (1/40)*(2x+3)

# support is [0,5]

# we will sample a z~U(0,5)
# then, we get g(z), which, in our case, is uniform 0.2
# however, this will not envelope our f(x), and so we choose m = 2, so it envelopes f(x)

# for each iteration, sample a z~U(0,5);
# then, sample a u~U(0,1);
# if  g(z) = (0.2*2*u) < f(z), then keep z; otherwise, don't keep("reject") z

x = np.empty(1001, dtype=object)


count = 0;

k=0;



while (k<1001):

    z = np.random.rand()*5
    f_z = (1/40)*(2*z + 3)
    u = np.random.rand()

    if (0.4*u < f_z):
        x[k] = z
        k+=1
    count+=1



plt.hist(x, normed=True,facecolor='green', alpha=0.75)


plt.plot(x,(1/40)*(2*x +3))

plt.show()
print(count)

# rejection sampling with marginals

# rejection sampling example #2

# f(x) = (2x+3y+2)

# support is [[0,2],[0,2]]

# we will sample a z~U(0,2)
# then, we get g(z), which, in our case, is uniform 0.5
# however, this will not envelope our f(x) (peak of 12), and so we choose m = 25, so it envelopes f(x)

# for each iteration, sample a z~U(0,2);
# then, sample a u~U(0,1);
# if  g(z) = (0.5*25*u) < f(z), then keep z; otherwise, don't keep("reject") z

x = np.ones(2000, dtype=object)*-1
y = np.ones(2000, dtype=object)*-1

print(x)
for i in range(1,2000):
         #sample from x | y, using rejection sampling
    z = 0
    while (z==0):
        u = np.random.rand()*2
        if (((2*u)+3*y[i-1] + 2) > (25*np.random.rand()*.5)):
            x[i]=u
            z=1
            
 
       # sample from y | x, using rejection sampling
    z = 0
    while (z==0):
        u = np.random.rand()*2
        if (((2*x[i])+3*u + 2) > (25*np.random.rand()*.5)):
    
            y[i]=u
            z=1
    
 

print(np.ones_like(x),len(x))

plt.hist(x, normed=True,facecolor='green', alpha=0.75)

plt.plot(x, (1/28)*(4.0*x+10.0))

plt.show()

plt.hist(y, normed=True,facecolor='yellow', alpha=0.75)

plt.plot(y,  (1/28)*(6*y+8))



plt.show()



