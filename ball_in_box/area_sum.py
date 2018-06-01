import math
import time
import ball_in_box
import ball_in_box.ballinbox as bb
import ball_in_box.validate as val

# DragoonKiller
# According to the test_docker_image.sh,
# this file will be replaced by another file when testing.

def area_sum(circles):
    area = 0.0
    for circle in circles:
        area += circle[2]**2 * math.pi

    return area

if __name__ == '__main__':
    
    rec = time.clock()
    
    num_of_circle = 5
    blockers = [(0.8, 0.8), (0.8, -0.8), (-0.8, 0.8), (-0.8, -0.8)]
    
    circles = bb.ball_in_box(num_of_circle, blockers)

    if num_of_circle == len(circles) and val.validate(circles, blockers):
        area = area_sum(circles)
        print("Total area: {}".format(area))
    else:
        print("Error: no good circles.")
    
    print("time usage: {}s".format(time.clock() - rec))
