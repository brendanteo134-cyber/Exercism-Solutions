from json import dumps
from typing import List
class Tree:
    def __init__(self, label: str, children: List["Tree"] = []):
        self.label = label
        self.children = children
    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}
    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)
    def __lt__(self, other) -> bool:
        return self.label < other.label
    def __eq__(self, other) -> bool:
        return self.__dict__() == other.__dict__()
    def copy(self):
        return Tree(self.label, [c.copy() for c in self.children])
    def from_pov(self, from_node: str) -> "Tree":
        new_tree = self.copy()
        if new_tree.label == from_node:
            return new_tree
        path = new_tree.path_from_self(from_node)
        if not path:
            raise ValueError("Tree could not be reoriented")
        assert path[0] is new_tree
        for a, b in zip(path[0:-1], path[1:]):
            a.children.remove(b)
            b.children.append(a)
        return path[-1]
    def path_to(self, from_node: str, to_node: str) -> List[str]:
        new_tree = self.from_pov(from_node)
        path = new_tree.path_from_self(to_node)
        if not path:
            raise ValueError("No path found")
        return [node.label for node in path]
    def path_from_self(self, to_node: str) -> List["Tree"]:
        if self.label == to_node:
            return [self]
        for c in self.children:
            res = c.path_from_self(to_node)
            if res:
                return [self] + res
        else:
            return [] 