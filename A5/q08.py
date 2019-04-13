# Krystal Wong
# A01089672
# Theoren Leveille
# A01070327
# 12/04/2019

"""
Test 1 - When arguments are two parallel lines:
        line_intersect([[1.0, 2.0],[2.0, 4.0]], [[2.0, 0.0],[3.0, 2.0]]), return None

Test 2 - When arguments are two coincident lines:
        line_intersect([[2.0, 4.0],[4.0, 8.0]], [[2.0, 4.0],[4.0, 8.0]]), return first argument

Test 3 - When arguments are two lines that intersect:
        line_intersect([[0.0, 6.0],[6.0, 0.0]], [[0.0, 0.0],[5.0, 10.0]]), return point of intersection ([2.0, 4.0])

Test 4 - When arguments are two unique points:
        line_intersect([[0.0, 6.0],[0.0, 6.0]], [[2.0, 3.0],[2.0, 3.0]]), return None

Test 5 - When arguments are two coincident points:
        line_intersect([[2.0, 3.0],[2.0, 3.0]], [[2.0, 3.0],[2.0, 3.0]]), return first argument

Test 6 - When arguments are a line and a point that do not intersect:
        line_intersect([[0.0, 0.0],[0.0, 0.0]], [[6.0, 0.0],[0.0, 6.0]]), return None

Test 7 - When arguments are a line and a point that are coincident:
        line_intersect([[0.0, 0.0],[0.0, 0.0]], [[-1.0, -2.0],[2.0, 4.0]]), return first argument
"""

