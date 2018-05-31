import math
import random

def funcTransfer(state, beginT, T, endT):
    
    """
    change the state randomly
    """
    for pt in state:
        radius = random.random() * 1.0
        angle = random.random() * math.pi * 2.0
        pt[0]+=radius*math.cos(angle)
        pt[1]+=radius*math.sin(angle)
        pt[2]+=radius*2-1
    return state
    
