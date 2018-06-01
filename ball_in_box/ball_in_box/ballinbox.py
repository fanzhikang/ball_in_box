import math
import random
from .validate import validate
from .funcTarget import funcTarget
from .funcTransfer import funcTransfer
from .sim_ann import sim_annealing

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
            circles.append((2 * random.random() - 1, 2 * random.random() - 1, 0))
    ans = circles.copy()
    # set up repeating limits to prevent TLE.
    # Python runs too slow !!!
    for i in range(1, max(2, 8000 // (m * max(1, len(blockers))))) :
        circles = sim_annealing(
            ans.copy(),
            lambda x : funcTarget(x) * i,
            lambda x, b, c, e : funcTransfer(x, b, c, e, blockers),
            lambda x : validate(x, blockers),
            1.0 / (i ** 3),
            1e-8,
            0.995)
        if funcTarget(circles) > funcTarget(ans) :
            ans = circles.copy()
    
    return ans

if __name__ == '__main__':
    ball_in_box()
