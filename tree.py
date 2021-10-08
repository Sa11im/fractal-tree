import simple_draw as sd
import random

def draw_branches(point, angle, length, width=1):
    if length < random.randint(1, 5):
        return
    delta = random.randint(18, 42)
    v1 = sd.get_vector(start_point=point, angle=(angle-delta), length=length)
    v1.draw(width=width)
    v2 = sd.get_vector(start_point=point, angle=(angle+delta), length=length)
    v2.draw(width=width)

    next_points = [v1.end_point, v2.end_point]
    next_angles = [angle - delta, angle + delta]
    next_length = length * random.uniform(.6, .8)
    for i in range(2):
        draw_branches(point=next_points[i], angle=next_angles[i], length=next_length)


sd.resolution = (1200, 800)
point_0 = sd.get_point(sd.resolution[0] // 2, 0)
angle_0 = 90
length_0 = 100
width_0 = 4
trunk = sd.get_vector(point_0, angle_0, length_0)
trunk.draw(width=width_0)

point_1 = trunk.end_point
angle_1 = 90
length_1 = 150
width_1 = 2
draw_branches(point=point_1, angle=angle_1, length=length_1, width=width_1)
sd.take_snapshot('tree.jpg')
sd.pause()


