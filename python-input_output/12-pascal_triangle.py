#!/usr/bin/python3
"""
This module defines 1 method:
    - 'pascal_triangle(n):
"""


def pascal_triangle(n):
    """
    This method calculates Pascal's Triangle
    to the n'th layer
    """

    if n <= 0:
        return []

    pascals_triangle = []
    for layer_num in range(0, n):
        layer = []
        for layer_len in range(0, layer_num + 1):
            if pascals_triangle == []:
                layer.append(1)
            elif layer_len == 0 or layer_len == layer_num:
                layer.append(1)
            else:
                layer.append(
                        pascals_triangle[layer_num - 1][layer_len - 1]
                        + pascals_triangle[layer_num - 1][layer_len])

        pascals_triangle.append(layer.copy())

    return pascals_triangle
