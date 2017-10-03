# This class represents an individual node in a binary tree
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
        self.descendents_count = 0
        self.label = -1
    
    # Add a child node to this node
    def addChild(self,child_node):
        self.descendents_count += 1 
        if (not self.left):
            self.left = child_node
            #print("Adding %d as a left child of %d" % (child_node.val, self.val))
        elif (not self.right):
            self.right = child_node
            #print("Adding %d as a right child of %d" % (child_node.val, self.val))
        else:
            if(not self.left.isSubtreeFull()):
                self.left.addChild(child_node)
            elif(not self.right.isSubtreeFull()):
                self.right.addChild(child_node)   
            elif(self.left.descendents_count > self.right.descendents_count):
                self.right.addChild(child_node)
            else:
                self.left.addChild(child_node)

    # Given a node find the depth of the tree 
    # by traversing the leftmost branches down
    def getSubtreeDepth(self):
        if (not self.left):
            return(1)
        else:
            return(1 + self.left.getSubtreeDepth()) 

    # Determine if down from this node total number of descendents is
    #  2^depth - 2  
    def isSubtreeFull(self):
        if (self.descendents_count == 2**self.getSubtreeDepth() - 2):
            return True
        return False

    # Traverse the tree in order let->right->root and assign label fields
    def traversePostorder(self):
        global Label
        if (self.left):
            self.left.traversePostorder()
            self.right.traversePostorder()
        self.label = Label
        Label += 1

    # Print the tree in the following format
    #  1 (7)  <== 1 is a value of the node, 7 is a label - order of the node during postorder traverse
    #   2 (3)
    #    4 (1)
    #    5 (2)
    #   3 (6)
    #    6 (4)
    #    7 (5)
    def printTree(self,indent=0):
        indentStr = ""
        for i in range(0,indent+1):
            indentStr += " "
        print('{}{} ({})'.format(indentStr,self.val,self.label))
        if (self.left):
            self.left.printTree(indent+1)
        if (self.right):
            self.right.printTree(indent+1)

    # Return all nodes of the tree including and below the given node   
    def getAllNodes(self):
        nodes = [self]
        if (self.left):
            nodes += self.left.getAllNodes()
        if (self.right):
            nodes += self.right.getAllNodes()
        return(nodes)


# Generate new nodes starting with values from start to stop
def nodeGen(start,stop):
    i = start
    while i <= stop:
        yield Node(i)
        i += 1

# leaf nodes are expected to have no children yet,
# number of children nodes shouls be 2x of leaf nodes
def addChildrenToLeafNodes(leafNodes,start,stop):
    newLeafNodes = []
    myNodeIter = nodeGen(start,stop)
    for leafNode in leafNodes:
        leftChild = next(myNodeIter)
        leafNode.left = leftChild

        rightChild = next(myNodeIter)
        leafNode.right = rightChild

        newLeafNodes.append(leftChild)
        newLeafNodes.append(rightChild)
    return(newLeafNodes)


def answer(h,q):
    global Label
    # 1) Construct node tree
    root = Node(1)

    # This method is  more elegant, but too slow
    # for val in range(2,2**h):
    #     root.addChild(Node(val))

    # This is faster
    leafNodes = [root]
    start = 2
    for level in range(1,h):
        stop = start + 2**level
        leafNodes = addChildrenToLeafNodes(leafNodes,start,stop)
        start = stop + 1

    
    # Add post-order labels to all tree nodes. We use global var label for keeping track of traversing sequence
    Label = 1
    root.traversePostorder()    
    #root.printTree()

    # Create a hash nodePostorderLabel => parentPostorderlabel
    labelHash = {}
    for node in root.getAllNodes():
        if(node.left):      
            labelHash[node.left.label]  = node.label
            labelHash[node.right.label]  = node.label

    # Loop through the list of labels and return correspondent list of parent labels
    parentLabels = []
    for label in q:
        if(label in labelHash):
            parentLabels.append(labelHash[label])
        else:
            parentLabels.append(-1)
    return(parentLabels)


# Testing
if(__name__ == '__main__'):
    print(answer(3,[7,3,5,1]))
    print(answer(5,[19,14,28]))
    
    #for node in nodeGen(4,8):
    #    print(node.val)
    
    