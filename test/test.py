import unittest

from app.geometry import Point2, Square, SquareFactory, Vector2


class SquareTester(unittest.TestCase):
    
    def test_create_point(self):
        x = 1.0
        y = 3.0

        point = Point2(x, y)
        self.assertEqual(x, point.x)
        self.assertEqual(y, point.y)

    def test_create_vector(self):
        x = -3.0
        y = 1.0

        vector = Vector2(x, y)
        self.assertEqual(x, vector.x)
        self.assertEqual(y, vector.y)

    def test_apply_vector_on_point(self):
        a = Point2(2,-1)
        v = Vector2(-5,3)

        b = v.apply(a)

        self.assertEqual(Point2(-3,2), b)

    def test_find_next_point_by_90_degrees(self):
        b = Point2(2,2)
        v_ab = Vector2(2,2)
        v_bc = Vector2(-1 * v_ab.y, v_ab.x)
        c = v_bc.apply(b)

        self.assertEqual(Point2(0,4), c)

    def test_find_4_points_of_square(self):
        a = Point2(0,0)
        b = Point2(2,2)
        c = Point2(0,4)
        d = Point2(-2,2)

        square = SquareFactory.build(a, b)

        self.assertEqual(c, square.points[2])
        self.assertEqual(d, square.points[3])

    def test_find_multiple_squares(self):
        points = [
            Point2(0,0),
            Point2(2,2),
            Point2(0,4),
            Point2(-2,2),
            Point2(4,0),
            Point2(2,-2)
        ]
        squares = []
        for a in points:
            for b in points:
                if a != b:
                    square = SquareFactory.build(a, b)
                    if square in squares:
                        continue

                    c = square.points[2]
                    d = square.points[3]
                    if c in points and d in points:
                        squares.append(square)

        self.assertEqual(2, len(squares))

    def test_eliminates_duplicate_points(self):
        points = [
            Point2(0,0),
            Point2(2,2),
            Point2(0,4),
            Point2(-2,2),
            Point2(4,0),
            Point2(2,-2),
            Point2(2,2),
            Point2(0,4),
        ]

        distinct_points = set(points)

        self.assertEqual(6, len(distinct_points))
    
    if __name__ == '__main__':
        unittest.main()
