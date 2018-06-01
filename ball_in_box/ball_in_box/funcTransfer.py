import math
import random
from .validate import validate

mxst = 0.0

# DragoonKiller:
# take the blocks to generate valid transfers,
# so that the sim-ann will not be blocked.
def funcTransfer(state, beginT, T, endT, blocks):
    global mxst
    """
    change the state randomly
    """
    
    def repeat(a, b, t) :
        if a < b : return repeat(b - a, b, t)
        elif a > t : return repeat(a - t, b, t)
        else : return a
        
    def dist(a, b) :
        ax, ay = a
        bx, by = b
        return math.sqrt((ax-bx)**2 + (ay-by)**2)
    
    eps = 1e-12
    
    # move all circles randomly.
    rate = math.pow((T - endT) / (beginT - endT), 0.25)
    
    # choose a dependence (contact) sequence.
    if random.random() < rate :
        for i in range(1, len(state)) :
            a = random.randint(0, i)
            state[a], state[i] = state[i], state[a]
    
    state[0] = (
        repeat(state[0][0] + rate * (2.0 * random.random() - 1.0), -1, 1),
        repeat(state[0][1] + rate * (2.0 * random.random() - 1.0), -1, 1),
        min(1.0, state[0][2] + rate) )
    
    # generate radius for each circle.
    for i in range(len(state)) :
        x, y, r = state[i]
        
        # check boundary.
        r = min(r, x - (-1))
        r = min(r, 1 - x)
        r = min(r, y - (-1))
        r = min(r, 1 - y)
        
        # check blocks.
        for blc in blocks :
            r = min(r, dist((x,y), blc))
        
        # check circle centers.
        for j in range(len(state)) :
            if i != j :
                r = min(r, dist((x, y), (state[j][0], state[j][1])))
        
        # check circles.
        for j in range(i) :
            cx, cy, cr = state[j]
            r = min(r, max(0.0, dist((x, y), (cx, cy)) - cr))
        
        state[i] = (x, y, max(0.0, r - eps))
    
    sz = 0.0
    for x,y,r in state:
        sz += r**2
    mxst = max(sz, mxst)
    # print(mxst)
    
    return state
