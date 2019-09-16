import matplotlib.pyplot as plt;
import numpy as np;
import scipy.optimize as opt;
from scipy.optimize import curve_fit;

data = np.loadtxt("M-L-z014.txt")

data=np.transpose(data)
print(np.shape(data))
data.sort(axis=1)
#plt.loglog(data[0],data[1],'.')
# plt.loglog(data[0],data[1])
# plt.show()

# This is the function we are trying to fit to the data.
def funcL(M, alpha, beta, landa, delta, epsilon, zeta, nu ):
     return (alpha*M**5.5 + beta*M**11.0)/(landa + M**3.0 + delta*M**5.0 + epsilon*M**7.0 + zeta*M**8.0 +nu*M**9.5)

Mdata = data[0]
Ldata = data[1]
plt.plot(Mdata, Ldata, ".", label="Data");
# plt.show()
optimizedParameters,pcov = curve_fit(funcL, Mdata, Ldata,maxfev=100000);
print(optimizedParameters);
plt.plot(Mdata, funcL(Mdata, *optimizedParameters), label="fit");
plt.xlabel('M(M_s)')
plt.ylabel('L(L_s)')
plt.savefig('M_L-z0.02.png')
plt.legend();
plt.show();

exit()
