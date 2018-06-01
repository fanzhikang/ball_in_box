import matplotlib.pyplot as plt
import numpy as np
def drawCircle(pts):
    for p in pts:
        theta = np.arange(0,2*np.pi,0.01)
        x = p[0]+ p[2]*np.cos(theta)
        y = p[0] + p[2]*np.sin(theta)
        plt.plot(x,y)