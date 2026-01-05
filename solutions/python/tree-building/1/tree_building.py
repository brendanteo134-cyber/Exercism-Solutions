class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id
class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []
def BuildTree(records):
    if not records:
        return None
    # Sort records by id
    records.sort(key=lambda r: r.record_id)
    n = len(records)
    # ---- BASIC SHAPE CHECKS ----
    # Root must exist and be id 0
    if records[0].record_id != 0:
        raise ValueError("Record id is invalid or out of order.")
    # IDs must be contiguous 0..n-1 and unique
    seen = set()
    for i, r in enumerate(records):
        if r.record_id in seen:
            raise ValueError("Record id is invalid or out of order.")
        seen.add(r.record_id)
        if r.record_id != i:
            raise ValueError("Record id is invalid or out of order.")
        if r.record_id < 0 or r.record_id >= n:
            raise ValueError("Record id is invalid or out of order.")
    # ---- PARENT RELATION CHECKS ----
    for r in records:
        # Parent id must be in range
        if r.parent_id < 0 or r.parent_id >= n:
            raise ValueError("Record id is invalid or out of order.")
        if r.record_id == 0:
            # For the root, we let the general parent rules handle wrong parent_id,
            # so that for Record(0, 1) we get the "parent_id smaller" message.
            # Equal id/parent is still OK for root, so skip that here.
            continue
        # Equal id and parent only allowed for root
        if r.parent_id == r.record_id:
            raise ValueError("Only root should have equal record and parent id.")
        # Parent must be smaller than child
        if r.parent_id > r.record_id:
            raise ValueError("Node parent_id should be smaller than its record_id.")
    # Extra explicit check that the *intended* root is valid:
    root = records[0]
    if not (root.record_id == 0 and root.parent_id == 0):
        # By now, if parent_id > record_id we already raised the "parent smaller"
        # message; the only remaining bad case is a root whose parent < child,
        # which we also want to treat as bad parent ordering.
        if root.parent_id != 0:
            raise ValueError("Node parent_id should be smaller than its record_id.")
    # ---- BUILD NODES ----
    nodes = [Node(i) for i in range(n)]
    # ---- CONNECT CHILDREN ----
    for r in records:
        if r.record_id == 0:
            continue
        parent = nodes[r.parent_id]
        child = nodes[r.record_id]
        parent.children.append(child)
    return nodes[0]