def rectangles(strings):
    HEIGHT = len(strings)
    if HEIGHT == 0:
        return 0
    WIDTH = len(strings[0])
    count = 0
    for top_left_row in range(HEIGHT):
        for top_left_col in range(WIDTH):
            if strings[top_left_row][top_left_col] != '+':
                continue
            for top_right_col in range(top_left_col + 1, WIDTH):
                top_right = strings[top_left_row][top_right_col]
                if top_right == '-':
                    continue
                elif top_right == ' ':
                    break
                else:
                    for bottom_row in range(top_left_row + 1, HEIGHT):
                        bottom_left = strings[bottom_row][top_left_col]
                        bottom_right = strings[bottom_row][top_right_col]
                        if bottom_left not in '+|' or bottom_right not in '+|':
                            break
                        if bottom_left == bottom_right == '+':
                            if all(ch in '-+' for ch in strings[bottom_row][top_left_col + 1 : top_right_col]):
                                count += 1
    return count