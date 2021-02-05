def spiral(R,C, r0,c0):
    output = []
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    dir_ind = 0
    steps = 1
    increment = 1
    output.append([r0,c0])
    total = R*C

    while len(output) < size:
        for _ in range(increment):
            dx, dy = dirs[dir_ind]
            r0,c0 = r0+dx, c0+ dx
            if r0 >=0 and r0 < R and c0 >=0 and c0 < C:
                output.append([r0,c0])

        dir_ind = (dir_ind + 1)%4
        if steps%2==0:
            increment += 1

        steps += 1
    return output

def spiralv2(matrix, i,j):
    results = []
    steps = 1
    increment = 1
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    dir_ind = 0
    results.append(matrix[i][j])
    size = len(matrix)*len(matrix[0])
    sort = True

    while len(results) < size:
        for _ in range(increment):
            dx,dy = dirs[dir_ind]
            i,j = i +dx , j + dy
            if i >=0 and i < len(matrix) and j >=0 and j < len(matrix[0]):
                results.append(matrix[i][j])
            if matrix[i][j] < matrix[i-dx][j-dy]:
                sort = False
            dir_ind = (dir_ind + 1)%4
            if steps%2 == 0:
                increment += 1

            steps += 1
    return sort, results
