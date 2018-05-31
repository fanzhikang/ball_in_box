def funcTarget(state):
    """
    fanzhikang

    the funcTarget is to get the sum of r^2
    
    """
    val=0.0
    for pt in state:
        val+=pt[2]**2
    return val
