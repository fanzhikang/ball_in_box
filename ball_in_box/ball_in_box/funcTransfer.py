import math
import random

def funcTransfer(state, beginT, T, endT):
    
    """
    change the state randomly
    """
    nxts = []
    for pt in state:
        radius = random.random() * 1.0
        angle = random.random() * math.pi * 2.0
        nxts.append( (pt[0] + radius*math.cos(pt[0] + angle),
            pt[1] + radius*math.sin(pt[1] + angle),
            max(0, pt[2] + radius*2 - 1)) )
    
    return nxts
    
