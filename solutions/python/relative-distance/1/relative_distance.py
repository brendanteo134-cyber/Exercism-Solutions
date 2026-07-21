from collections import deque, defaultdict
class RelativeDistance:
    """
    Calculates the degree of separation between individuals in a family tree.
    """
    adj: dict[str, set[str]]
    family_tree: dict[str, list[str]]
    def __init__(self, family_tree: dict[str, list[str]]):
        """
        Initializes the RelativeDistance with a family tree.
 
        Args:
            family_tree (dict[str, list[str]]): A dictionary where keys are individuals
                and values are lists of their children.
        """
        self.family_tree = family_tree
        adjacency_list: defaultdict[str, set[str]] = defaultdict(set)
        for parent, children in family_tree.items():
             
            adjacency_list[parent].update(children)
            for child in children:
                
                adjacency_list[child].add(parent)
               
                adjacency_list[child].update(sibling for sibling in children if sibling != child)
        self.adj = adjacency_list
    def degree_of_separation(self, person_a: str, person_b: str) -> int:
       
        if person_a not in self.adj:
            raise ValueError("Person A not in family tree.")
        if person_b not in self.adj:
            raise ValueError("Person B not in family tree.")
       
        search_queue: deque[tuple[int, str]] = deque([(0, person_a)])
        visited_people: set[str] = {person_a}
        while search_queue:
            distance, current_person = search_queue.popleft()
            
            if current_person == person_b:
                return distance
      
            for relative in self.adj[current_person]:
                if relative not in visited_people:
                    visited_people.add(relative)
                    search_queue.append((distance + 1, relative))
    
        raise ValueError("No connection between person A and person B.")