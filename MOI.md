``` python
from scipy.integrate import dblquad
import numpy as np

def integrand_Iz(R, beta):
    return R**4 * np.cos(beta)**3

def integrand_M(R, beta):
    return R**2 * np.cos(beta)

num = dblquad(integrand_Iz, -np.pi/2, np.pi/2, lambda x:0, lambda x: 1)[0]
dem = dblquad(integrand_M, -np.pi/2, np.pi/2, lambda x:0, lambda x: 1)[0]
Iz_MR2 = num/dem
print(Iz_MR2)

num = dblquad(integrand_Iz, np.pi/4, np.pi/2, lambda x:0, lambda x: f(x))[0]
dem = dblquad(integrand_M, np.pi/4, np.pi/2, lambda x:0, lambda x: f(x))[0]
Iz_MR2 = num/dem
print(Iz_MR2)
```


