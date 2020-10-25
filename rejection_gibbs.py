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
