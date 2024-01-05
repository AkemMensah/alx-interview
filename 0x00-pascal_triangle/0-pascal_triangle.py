#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    -Returns a list of integers
    -representing the Pascal Triangle of n
    -returns empty list if n <= 0
    """
    if n <= 0:
        return []
    else:
	triangle = [[1]]
	for i in range(1,n):
		triangle.append([1])
		for j in range(1, i):
			triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
		triangle[i].append(i)
	return triangle
