	

# Document classes and functions with docstrings instead of comments
class Tree(object):
    """A binary tree class"""
    def __init__(self, label, left=None, right=None):
        """Label is the node value, left and right are Tree objects or None"""
        self.label = label
        self.left = left   # Tree() or None
        self.right = right # Tree() or None

    def __repr__(self):
        return 'Tree(%r, %r, %r)' % (self.label, self.left, self.right)

    def __iter__(self):
        # No need for a separate inorder() function
        if self.left is not None:
            for t in self.left:
                yield t
        yield self.label
        if self.right is not None:
            for t in self.right:
                yield t

    def printTree(self,indent=0):
        indentStr = ""
        for i in range(0,indent+1):
            indentStr += " "
        print('{}{}'.format(indentStr,self.label))
        if (self.left):
            self.left.printTree(indent+1)
        if (self.right):
            self.right.printTree(indent+1)

def tree(indexable):
    """Return a tree of anything sliceable"""
    ilen = len(indexable)
    if not ilen:
        # You should be clearer about empty values
        # left and right should be Tree (something with left, right, and __iter__)
        # or None if there is no edge.
        return None 
    center = ilen // 2 # floor division
    return Tree(indexable[center], tree(indexable[:center]), tree(indexable[center+1:]))
    #return Tree(indexable[0],)


def test():
    seq = range(1,8)
    t = tree(seq)
    #for x in t:
    #    print(x)
    # list(t) will consume an iterable
    # no need for "result = []; for x in t: result.append(x)"
    #assert seq == list(t)
    t.printTree()

if __name__ == '__main__':
    test()