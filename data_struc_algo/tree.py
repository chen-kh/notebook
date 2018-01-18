class Tree(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    @staticmethod
    def pre_traverse(t):
        if t is not None:
            print(t.value)
            Tree.pre_traverse(t.left)
            Tree.pre_traverse(t.right)
    
    @staticmethod
    def mid_traverse(t):
        if t is not None:
            Tree.mid_traverse(t.left)
            print(t.value)
            Tree.mid_traverse(t.right)


    @staticmethod
    def mid_tree2list(t):
        if t is not None:
            Tree.mid_tree2list(t.left).right=t
            t.left = Tree.mid_tree2list(t.left)
            t.right=Tree.mid_tree2list(t.right)
            Tree.mid_tree2list(t.right).left=t
        return t


if __name__ == '__main__':
    t1 = Tree(10)
    t1.left = Tree(6)
    t1.right = Tree(12)
    Tree.pre_traverse(t1)
    Tree.mid_traverse(t1)



        
    