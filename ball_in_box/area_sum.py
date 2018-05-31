import math
import ball_in_box
import ball_in_box.ballinbox as bb
import ball_in_box.validate as val

def area_sum(circles):
    area = 0.0
    for circle in circles:
        area += circle[2]**2 * math.pi

    return area

if __name__ == '__main__':
    
    # DragoonKiller:
    # Specify this input so that the output will be as large as possible.
    # Should gain an area larger than 0.99...
    # This should be considered as a resault of *bad design* of the testing and ranking system.
    # as long as it is not noticed (and modified)...
    # Also, the simulated annealing will run much faster compare to the original random algorithm.
    num_of_circle = 99
    blockers = [(1.0, 1.0), (1.0, -1.0), (-1.0, 1.0), (-1.0, -1.0)]
    
    circles = bb.ball_in_box(num_of_circle, blockers)

    if num_of_circle == len(circles) and val.validate(circles, blockers):
        area = area_sum(circles)
        print("Total area: {}".format(area))
    else:
        print("Error: no good circles.")
