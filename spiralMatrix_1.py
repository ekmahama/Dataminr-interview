def spiralOrder(matrix):
    output = []
    left, right = 0, len(matrix[0])-1
    top, bottom = 0, len(matrix)-1

    size = len(matrix)*len(matrix[0])

    while len(output) < size:
        for i in range(left, right+1):
            if len(output) < size:
                output.append(matrix[top][i])
        top += 1
        for i in range(top, bottom+1):
            if len(output) < size:
                output.append(matrix[i][right])
        right -= 1

        for i in range(right, left-1,-1):
            if len(output) < size:
                output.append(matrix[bottom][i])
        bottom -= 1

        for i in range(bottom,top-1,-1):
            if len(output) < size:
                output.append(matrix[i][left])
    return output
