from functools import partial
class Zipper(object):
    @staticmethod
    def from_tree(tree):
        return Zipper(tree)
    def __init__(self, tree, parents=[]):
        self.tree, self.parents = tree, parents
        for val in ('left', 'right', 'value'):
            setattr(self, 'set_%s'%val, partial(self.set, val))
            setattr(self, val, partial(self.get, val))
    def get(self, key):
        if key == 'value':
            return self.tree['value']
        return (Zipper(self.tree[key], self.parents + [self]) if self.tree[key] else None)
    
    def set(self, key, item):
        self.tree[key] = item
        return self.parents[0] if self.parents else self
    def up(self):
        return (self.parents[-1] if self.parents else None)
    def to_tree(self):
        return self.parents[0].tree if self.parents else self.tree