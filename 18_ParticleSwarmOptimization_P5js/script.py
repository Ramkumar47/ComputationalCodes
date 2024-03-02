import numpy as np
import matplotlib.pyplot as plt


def f_obj(x,y):
    return 100*np.sqrt(np.abs(y-0.01*x**2))+0.01*np.abs(x+10)


X,Y = np.meshgrid(np.linspace(-15,-5,101),np.linspace(-4,6,101))

f_val = f_obj(X,Y)



plt.figure(frameon = False)
plt.contourf(X,Y,f_val,100,cmap="jet")
plt.axis("image")
plt.colorbar()
plt.savefig("output.jpg", dpi =150)
plt.show()
