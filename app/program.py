import math
from geometry import *

# read the file to get the points
def get_points(file):
    points = []

    with open(file, 'r') as f:
        lines = f.readlines()
        for l in lines:
            coordonates = l.split(' ')
            if len(coordonates) != 2:
                raise Exception('The file contains a line that cannot be red as a point.')

            point = Point2(coordonates[0], coordonates[1])
            points.append(point)

    return points

def compute(points):
    squares = []
    used_points = []
    count = 0
    # For all points
    for a in points:
        count += 1
        print(count)

        # Compute to other points only if the point
        # is not part of a detected square
        if not a in used_points:
            for b in points[count:]:
                if a != b:
                    # build the potential square
                    square = SquareFactory.build(a, b)

                    c = square.points[2]
                    d = square.points[3]

                    # we are sure that 'a' and 'b' are in our list of point
                    # then we must check if 'c' and 'd' are in too
                    if c in points and d in points :
                        print('SQUARE')
                        squares.append(square)

                        # update used points
                        used_points.append(a)
                        if not b in used_points:
                            used_points.append(b)
                        if not c in used_points:
                            used_points.append(c)
                        if not d in used_points:
                            used_points.append(d)

    return squares

if __name__ == '__main__':
    f = open("data/out.txt", "w")
    # get points
    points = get_points('data/points.txt')
    #points = [Point2(-5,3), Point2(-3,7), Point2(-2,4), Point2(-6,6)]
    # Remove duplicate points
    points = list(set(points))
    print('{0} points to compute'.format(len(points)))
    # find squares
    squares = compute(points)

    square_count = len(squares)
    if square_count > 0:
        f.write('{0} square(s) found\n'.format(square_count))
        for square in squares:
            f.write('#1 : {0}\n'.format(square))
    else:
        f.write('No square found ! :(')

    f.close()