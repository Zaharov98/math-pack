
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate

x = np.arange(0, 0.8, 0.1)
y = np.array([0.078, 0.2, 0.67, 0.334, 0.24, 0.15, 0.1, 0.08, ])

s = scipy.interpolate.InterpolatedUnivariateSpline(x, y)

xnew = np.arange(0, 0.8, 0.05)
ynew = s(xnew)

plt.plot(xnew, ynew)
plt.show()

