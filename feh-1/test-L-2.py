import matplotlib.pyplot as plt;
import numpy as np;
import scipy.optimize as opt;
#from scipy.optimize import curve_fit;

data = np.loadtxt("M-L-z14log.txt")

data=np.transpose(data)
# print(np.shape(data))
data.sort(axis=1)
#plt.loglog(data[0],data[1],'.')
# plt.loglog(data[0],data[1])
# plt.show()

# This is the function we are trying to fit to the data.
def funcL(M, alpha, beta, landa, delta, epsilon):
     return (alpha*M**4 + beta*M**3+landa* M**2.0 + delta*M+ epsilon )

def exp10(M):
     return 10**M

Mdata = data[0]

Ldata = data[1]
fig = plt.figure()
fig.set_size_inches(8,7)
# fig.set_label_position('Y','right')
# plt.plot(Mdata, Ldata, ".", label="Data");
# plt.show()
optimizedParameters,pcov = opt.curve_fit(funcL, Mdata, Ldata,maxfev=100000);
print(optimizedParameters);
# print(funcL(Mdata, *optimizedParameters));
# plt.plot(Mdata, funcL(Mdata, *optimizedParameters), label="fit");
Mdataexp = []
for i in range(len(Mdata)):
     Mdataexp.append(2**Mdata[i])
Ldataexp = []
for i in range(len(Ldata)):
     Ldataexp.append(2**Ldata[i])
funcLexp = []
for i in range(len(Mdata)):
     funcLexp.append(2**funcL(Mdata[i],*optimizedParameters))
# Mdataexp = exp10(Mdata)
# funcLexp = exp10(funcL(Mdata,*optimizedParameters))
# Ldataexp = exp10(Ldata)
plt.plot(Mdataexp, Ldataexp, ".", label="Data")
plt.plot(Mdataexp, funcLexp, label="fit")
# plt.loglog(Mdata, funcL(Mdata, *optimizedParameters),".", label="fit");
print([Mdataexp[i] for i in range(len(Mdataexp)) if Mdataexp[i] > 300])
plt.xlabel('M(M_s)')
plt.ylabel('L(L_s)')
plt.savefig('2M_L-z0.02.png')
# plt.set_size_inches
# plt.axis.set_label_position('right')
# plt.axis()
plt.legend();
plt.show();

exit()

