"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""


def rotateClokwise(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j or i < j:
                continue
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def rotateAntiClockwise(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j or i < j:
                continue
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    matrix.reverse()
