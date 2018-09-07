import math

# The basic implementation of a 2 dimensional point
class Point2(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __hash__(self):
        return hash((self.x, self.y))

    # Override equal
    def __eq__(self, other):
        if isinstance(other, Point2):
            return self.x == other.x and self.y == other.y
        return False

    # Override not equal (!equal)
    def __ne__(self, other):
        return not self.__eq__(other)

    # Override to string
    def __str__(self):
        return '[{0};{1}]'.format(self.x, self.y)

    @staticmethod
    def distance(p1, p2):
        dX = math.pow(p1.x - p2.x, 2)
        dY = math.pow(p1.y - p2.y, 2)
        return math.sqrt(dX + dY)

# The basic implementation of a 2 dimensional point
class Vector2(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Apply this vector to the given point and returns the found point
    def apply(self, point):
        return Point2(point.x + self.x, point.y + self.y)

    @staticmethod
    def rotate_90(vector):
        return Vector2(-1 * vector.y, vector.x)

# The implementation of a segment definied by 2 points
class Segment(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return Point2.distance(self.p1, self.p2)

    def __str__(self):
        return '[{0},{1}]'.format(self.p1, self.p2)

class Square(object):
    def __init__(self):
        self.points = [Point2(0,0), Point2(1,0), Point2(1,1), Point2(0,1)]

    def __eq__(self, other):
        if isinstance(other, Square):
            return  (other.points[0] in self.points and
                    other.points[1] in self.points and
                    other.points[2] in self.points and
                    other.points[3] in self.points)

        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '({0} , {1} , {2} , {3})'.format(self.points[0],self.points[1],self.points[2],self.points[3])

class SquareFactory(object):

    @staticmethod
    def build(a, b):
        s = Square()
        s.points[0] = a
        s.points[1] = b

        v_ab = Vector2(b.x - a.x, b.y - a.y)
        
        v_bc = Vector2.rotate_90(v_ab)
        c = v_bc.apply(b)

        v_cd = Vector2.rotate_90(v_bc)
        d = v_cd.apply(c)

        s.points[2] = c
        s.points[3] = d

        return s

    @staticmethod
    def is_square(square):
        # Must have 4 points
        if len(square.points) != 4:
            return False
        # The reference point
        p1 = square.points[0]
        segments = {}
        # For each other points
        for point in square.points[1:]:
            s = Segment(p1, point)
            l = s.length()  # distance between [p1;point]
            if l in segments.keys():
                segments[l].append(point)
            else:
                segments[l] = [point]

        # The diagonal of the square is the maximum segment
        diag = max(segments.keys())
        # The side of the square is the minimum segment
        side = min(segments.keys())

        # Diagonal must be attached to 1 point only
        # Side must be attached to exactly 2 points
        if len(segments[diag]) != 1 or len(segments[side]) != 2:
            return False

        # Take the diagonal between the adjacent points
        diag2 = Segment(segments[side][0], segments[side][1]).length()
    
        # This second diagonal must be equal to the first
        return diag == diag2

