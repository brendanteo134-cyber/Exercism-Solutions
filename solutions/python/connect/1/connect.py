import sys
class ConnectGame:
    def __init__(self, board_string):
        rows = list(board_rows(board_string))
        positions = list(enumerate_board(rows))
        self.width = len(rows[0])
        self.height = len(rows)
        self.x_positions = create_player_positions(positions, 'X')
        self.o_positions = create_player_positions(positions, 'O')
    def get_winner(self):
        if self.width == 1:
            if self.x_positions:
                return 'X'
            elif self.o_positions:
                return 'O'
            else:
                return ""
        elif wins_west_to_east(self.x_positions, self.width):
            return 'X'
        elif wins_north_to_south(self.o_positions, self.height):
            return 'O'
        else:
            return ""
def create_player_positions(positions, player_char):
    return set(
        (x, y) for x, y, c in positions if c == player_char
    )
def enumerate_board(rows):
    for y, row in enumerate(rows):
        for x, c in enumerate(row):
            yield (x, y, c)
def board_rows(board_string):
    yield from (row.replace(" ", "") for row in board_string.split("\n"))
def wins_west_to_east(positions, width):
    west_positions = [(x, y) for x, y in positions if x == 0]
    east_positions = [(x, y) for x, y in positions if x == width - 1]
    return path_exists_between_position_lists(positions, west_positions, east_positions)
def wins_north_to_south(positions, height):
    north_positions = [(x, y) for x, y in positions if y == 0]
    south_positions = [(x, y) for x, y in positions if y == height - 1]
    return path_exists_between_position_lists(positions, north_positions, south_positions)
def path_exists_between_position_lists(positions, position_list_a, position_list_b):
    for a in position_list_a:
        if path_exists(positions, a, position_list_b):
            return True
    return False
def path_exists(positions, source, target_list):
    reachable_positions = dijkstra(positions, source)
    return any(t in reachable_positions for t in target_list)
def dijkstra(positions, source):
    position_set = set(positions)
    node_queue = set(positions)
    distances = create_distance_map(positions, source)
    while node_queue:
        position = min(
            node_queue,
            key=lambda p: distances[p]
        )
        node_queue.remove(position)
        for neighbour in neighbours(position_set, position):
            distances[neighbour] = min([
                distances[neighbour],
                distances[position] + 1
            ])
    return set(p for p, distance in distances.items() if distance != sys.maxsize)
def create_distance_map(positions, source):
    dist = dict()
    for position in positions:
        dist[position] = sys.maxsize
    dist[source] = 0
    return dist
def neighbours(position_set, position):
    return [
        n for n in possible_neighbours(position)
        if n in position_set
    ]
def possible_neighbours(position):
    px, py = position
    yield (px, py - 1)
    yield (px + 1, py - 1)
    yield (px - 1, py)
    yield (px + 1, py)
    yield (px - 1, py + 1)
    yield (px, py + 1)
