
# DragoonKiller.

import math
import random

###############################################################################

def sim_annealing(
    initState,
    funcTarget,
    funcTransfer,
    funcValidate,
    beginT = 1.0,
    endT = 1e-8,
    stepRate = 0.995 ) :
    """
    DragoonKiller.
    
    One step simulation.
    
    Default parameters are configured just there.
    This is the main simulated annealing function, which searches a *maximum* value for given function.
    Supports only numeric target value for now.
    """
    if not funcValidate(initState) : raise Exception("Simulated annealing: initial state must be valid.")
    
    st = initState
    val = funcTarget(st)
    T = beginT
    
    while T >= endT :
        cnt = 0
        
        nxt = funcTransfer(st, beginT, T, endT)
        while not funcValidate(nxt) :
            nxt = funcTransfer(st, beginT, T, endT)
        
        nxtval = funcTarget(nxt)
        
        if nxtval > val or random.random() < math.exp((nxtval - val) / T) :
            st = nxt
            val = nxtval
        
        T = T * stepRate
    
    return st


###############################################################################


def unit_test() :
    """
    DragoonKiller.
    Use simulated annealing to find the maximun value of F = -sin(x+y)cos(x-y)
      where 0 <= x <= 4, 0 <= y <= 4.
      the answer is (0.75 pi, 0.75 pi), and the value is 1.
    Since this is a randomized algorithm, the unit test may fail in high resolution.
    """
    def target(pt) : return - math.sin(pt[0] + pt[1]) * math.cos(pt[0] - pt[1])
    def validate(pt) : return 0.0 <= pt[0] and pt[0] <= 4.0 and 0.0 <= pt[1] and pt[1] <= 4.0
    def trans(pt, beginT, curT, endT) :
        radius = random.random() * 4.0
        angle = random.random() * math.pi * 2.0
        return (radius * math.cos(angle) + pt[0], radius * math.sin(angle) + pt[1]) 
    
    print("=== unit test : sim_ann : begin ===")
    
    ans = (0.0, 0.0)
    for i in range(10) :
        nxtans = sim_annealing(ans, target, trans, validate)
        if target(nxtans) > target(ans) :
            ans = nxtans
        
    print("ans {}".format(ans))
    print("value {}".format(target(ans)))
    assert math.fabs(ans[0] - 0.75 * math.pi) <= 1e-2
    assert math.fabs(ans[1] - 0.75 * math.pi) <= 1e-2
    assert math.fabs(target(ans) - 1.0) <= 1e-5
    
    print("=== unit test : sim_ann : end ===")

###############################################################################

if __name__ == "__main__" :
    unit_test()
