NODE, EDGE, ATTR = range(3)
class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs
    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs
class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs
    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)
class Graph:
    def __init__(self, data=None):
        self.nodes = []
        self.edges = []
        self.attrs = {}
        if data is None:
            return
        if not hasattr(data, '__getitem__') or type(data) is str:
            raise TypeError("Graph data malformed")
        for d in data:
            if not self._is_good_input(d):
                pass
            if d[0] == NODE:
                self.nodes += [Node(d[1], d[2])]
            elif d[0] == EDGE:
                self.edges += [Edge(d[1], d[2], d[3])]
            elif d[0] == ATTR:
                self.attrs[d[1]] = d[2]
        return
    def _is_good_input(self, d):
        if len(d) < 3 or len(d) > 4:
            raise TypeError("Graph item incomplete")
        elif d[0] not in range(3):
            raise ValueError("Unknown item")
        elif d[0] == NODE and len(d) != 3:
            raise ValueError("Node is malformed")
        elif d[0] == EDGE and len(d) != 4:
            raise ValueError("Edge is malformed")
        elif d[0] == ATTR and len(d) != 3:
            raise ValueError("Attribute is malformed")
        return True