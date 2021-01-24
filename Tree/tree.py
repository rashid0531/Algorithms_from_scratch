
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BinaryTree:

    def __init__(self, root=None):
        self.root = root

    def traverse(self, starting_node=None, default_traversal='in-order'):
        
        def in_order_traversal(node):
            if node.left is not None:
                in_order_traversal(node.left)
            print(node.data)
            if node.right is not None:
                in_order_traversal(node.right)
        
        def pre_order_traversal(node):
            print(node.data)
            if node.left is not None:
                pre_order_traversal(node.left)
            if node.right is not None:
                pre_order_traversal(node.right)

        def post_order_traversal(node):
            if node.left is not None:
                post_order_traversal(node.left)
            if node.right is not None:
                post_order_traversal(node.right)
            print(node.data)
        
        traversal_logics = {
            'in-order' : in_order_traversal,
            'pre-order' : pre_order_traversal,
            'post-order' : post_order_traversal
        }

        try:
            traversal_func = traversal_logics[default_traversal]
        except KeyError:
            print('Invalid traversal requested. Please select any from : in-order, pre-order, postorder')

        if not starting_node:
            starting_node = self.root

        traversal_func(starting_node)

if __name__ == "__main__":
    
    # Tree used as example was taken from this link : https://www.tutorialspoint.com/data_structures_algorithms/tree_traversal.htm

    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')
    F = Node('F')
    G = Node('G')

    tree = BinaryTree(A)
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.left = F
    C.right = G

    # set either 'in-order', 'pre-order' or 'post-order' as the default-traversal.
    tree.traverse(default_traversal='post-order')