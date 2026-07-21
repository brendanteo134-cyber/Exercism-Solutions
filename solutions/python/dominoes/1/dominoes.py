def can_chain(dominoes):
    return next(chain(dominoes, []), None if dominoes else [])
def chain(tiles, ordered):
    if not tiles and ordered and ordered[0][0] == ordered[-1][1]:
        yield ordered
    for t in tiles:
        idx = tiles.index(t)
        rest_tiles = tiles[:idx] + tiles[idx + 1 :]
        rev = t[::-1]
        if not ordered:
            yield from chain(rest_tiles, [t])
        elif t[0] == ordered[-1][1]:
            yield from chain(rest_tiles, ordered + [t])
        elif t[0] == ordered[0][0]:
            yield from chain(rest_tiles, [rev] + ordered)
        elif t[1] == ordered[0][0]:
            yield from chain(rest_tiles, [t] + ordered)
        elif t[1] == ordered[-1][1]:
            yield from chain(rest_tiles, ordered + [rev])