class SuffixTree:
    def __init__(self, string):
        self.string = string
        self.root = Node(-1, -1)  # initialize root node with start and end indices of -1
        self.nodes = [self.root]
        self.active_node = self.root
        self.active_edge = None
        self.active_length = 0
        self.remainder = 0
        
        for i, char in enumerate(string):
            self.extend(i, char)
    
    def extend(self, i, char):
        self.remainder += 1
        last_new_node = None
        
        while self.remainder > 0:
            if self.active_length == 0:
                self.active_edge = i
            
            if self.active_edge not in self.active_node.edges:
                leaf_node = Node(i, len(self.string))
                self.active_node.edges[self.active_edge] = leaf_node
                self.nodes.append(leaf_node)
                last_new_node = None
            else:
                next_node = self.active_node.edges[self.active_edge]
                if self.walk_down(next_node):
                    continue
                
                if self.string[next_node.start + self.active_length] == char:
                    self.active_length += 1
                    if last_new_node is not None and self.active_node != self.root:
                        last_new_node.suffix_link = self.active_node
                        last_new_node = None
                    break
                
                split_node = Node(next_node.start, next_node.start + self.active_length)
                self.nodes.append(split_node)
                parent_node = next_node.parent
                parent_node.edges[self.active_edge] = split_node
                split_node.edges[char] = Node(i, len(self.string))
                next_node.start += self.active_length
                split_node.edges[self.string[next_node.start]] = next_node
                self.nodes.append(next_node)
                if last_new_node is not None:
                    last_new_node.suffix_link = split_node
                last_new_node = split_node
                
            self.remainder -= 1
            if self.active_node == self.root and self.active_length > 0:
                self.active_length -= 1
                self.active_edge = i - self.remainder + 1
            else:
                self.active_node = self.active_node.suffix_link if self.active_node.suffix_link is not None else self.root
         
    def walk_down(self, node):
        if self.active_length >= node.edge_length(self.active_edge):
            self.active_edge += node.edge_length(self.active_edge)
            self.active_length -= node.edge_length(self.active_edge)
            self.active_node = node
            return True
        return False
        

class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.edges = {}
        self.parent = None
        self.suffix_link = None
        
    def edge_length(self, edge):
        return min(self.end, edge + 1) - self.start
    

def build_suffix_tree(string):
    return SuffixTree(string)



tree = build_suffix_tree('xabcab')
print(tree.nodes)








