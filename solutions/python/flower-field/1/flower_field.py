def annotate(garden):
    if not garden:
        return []
  
    row_length = len(garden[0])
    for row in garden:
        if len(row) != row_length:
            raise ValueError("The board is invalid with current input.")
   
    for row in garden:
        for ch in row:
            if ch not in (' ', '*'):
                raise ValueError("The board is invalid with current input.")
                

    neighbor_offsets = [
        (-1, -1), (-1, 0), (-1, +1),
        ( 0, -1),          ( 0, +1),
        (+1, -1), (+1, 0), (+1, +1)
    ]
    num_rows = len(garden)
    num_cols = len(garden[0]) if num_rows > 0 else 0
    annotated_garden = []
    for current_row in range(num_rows):
        new_row_string = ""
        for current_col in range(num_cols):
            if garden[current_row][current_col] == '*':
              
                new_row_string += '*'
            else:
                flower_count = 0
        
                for row_offset, col_offset in neighbor_offsets:
                    neighbor_row = current_row + row_offset
                    neighbor_col = current_col + col_offset
                  
                    if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                        if garden[neighbor_row][neighbor_col] == '*':
                            flower_count += 1
              
                new_row_string += str(flower_count) if flower_count > 0 else ' '
        annotated_garden.append(new_row_string)
    return annotated_garden
