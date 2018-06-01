import math
import random
from validate import validate
from funcTarget import funcTarget
from funcTransfer import funcTransfer
from sim_ann import sim_annealing

__all__ = ['ball_in_box']

def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]):
    """
    m is the number circles.
    n is the list of coordinates of tiny blocks.
    
    This returns a list of tuple, composed of x,y of the circle and r of the circle.
    """

    # The following is an example implementation.
    circles = []
    for index in range(m):
        circles.append((0,0,0))
    circles = sim_annealing(circles, funcTarget, funcTransfer, lambda x : validate(x, blockers))
    print(circles)
    return circles
if __name__ == '__main__':
    ball_in_box()
