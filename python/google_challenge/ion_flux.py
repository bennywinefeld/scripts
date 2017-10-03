# This class represents an individual node in a binary tree
class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.label = -1
    
    def __iter__(self):    
        yield self
        if self.left is not None:
            for t in self.left:
                yield t
        if self.right is not None:
            for t in self.right:
                yield t
        
    # Traverse the tree in order left->right->root and assign label fields
    def traversePostorder(self):
        global Label
        if (self.left):
            self.left.traversePostorder()
            self.right.traversePostorder()
        self.label = Label
        Label += 1

    def addLevel(self):
        global Val
        if (self.left):
            self.left.addLevel()
            self.right.addLevel()
        else:
            self.left = Node()
            self.right = Node()

    # Print the tree in the following format
    # 7
    # +-3
    # | +-1
    # | +-2
    # +-6
    #   +-4
    #   +-5
    def printTree(self,indentStr):
        if(indentStr==""):
            # This is for the reall root of the tree - no indent or prefix 
            print(self.label)
        else:
            # Replace last two chars of the indentStr with "+-"
            print('{}+-{}'.format(indentStr[:-2],self.label))
        # Increase indent for both left and right subtrees, but differently
        if (self.left):
            self.left.printTree(indentStr + "| ")
        if (self.right):
            self.right.printTree(indentStr + "  ")

def answer(h,q):
    global Label
    # 1) Construct node tree
    root = Node()
    for level in range(2,h+1):
        root.addLevel()
    
    # 2) Add post-order labels to all tree nodes. We use global var label for keeping track of traversing sequence
    Label = 1
    root.traversePostorder()    
    root.printTree("")

    # 3) Find a list of parent node labels
    # root is iterable
    parentLabels = []
    for label in q:
        if (root.label == label):
            parentLabels.append(-1)
            continue
        for node in root:
            if (node.left and ((node.left.label==label) or (node.right.label==label))):
                parentLabels.append(node.label)
                break    
    return(parentLabels)

# Testing
if(__name__ == '__main__'):
    print(answer(5,[7,3,5,1]))
    #print(answer(5,[19,14,28]))
    