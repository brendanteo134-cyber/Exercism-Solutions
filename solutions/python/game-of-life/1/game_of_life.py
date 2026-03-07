def tick(matrix):
    if len(matrix) == 0:
        return []
    row_num = len(matrix)
    row_length = len(matrix[0])
    result = []
    for row_index in range(row_num):
        new_row = []
        result.append(new_row)
        for index in range(row_length):
            anc = count(matrix, row_num, row_length, row_index, index)
            alive = matrix[row_index][index]
            new_row.append(
                alive and (anc == 2 or anc == 3)
                or not alive and anc == 3
            )
    return result
def count(matrix, row_num, row_length, row_index, index):
    neighbors = [
        (index, row_index + 1), 
        (index + 1, row_index + 1), 
        (index + 1, row_index), 
        (index + 1, row_index - 1),
        (index, row_index - 1), 
        (index - 1, row_index - 1), 
        (index - 1, row_index), 
        (index - 1, row_index + 1) 
    ]
    return len([n
        for n in neighbors
        if (
            0 <= n[0] < row_length 
            and 0 <= n[1] < row_num
            and matrix[n[1]][n[0]]
        )
    ])