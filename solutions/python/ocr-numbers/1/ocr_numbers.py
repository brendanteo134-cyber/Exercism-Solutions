def convert(input_grid):
    nrows, ncols = len(input_grid), len(input_grid[0])

    if len(input_grid) == 0 or len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if not(all([len(col) >= 3 and len(col) % 3 == 0 for col in input_grid])):
        raise ValueError("Number of input columns is not a multiple of three")

    digits = {
        " _ | ||_|   " : '0', "     |  |   " : '1', " _  _||_    " : '2',
        " _  _| _|   " : '3', "   |_|  |   " : '4', " _ |_  _|   " : '5',
        " _ |_ |_|   " : '6', " _   |  |   " : '7', " _ |_||_|   " : '8',
        " _ |_| _|   " : '9'
        }
    result = [''] * (nrows // 4)
    
    for nrow_start in range(0, nrows, 4):
        for col_slice in range(0, ncols, 3):
            ocr_conv = ''
            for to_be_added in range(4):
                ocr_conv += input_grid[nrow_start + to_be_added][col_slice:col_slice+3]
    
            result[nrow_start // 4] += digits.get(ocr_conv, '?')
    return ','.join(result)