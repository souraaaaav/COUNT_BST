class newNode:
    
    def __init__(self, value):
        self.key=value
        self.left = None
        self.right = None
 
def preorder(root) :
 
    if (root != None) :
        print(root.key, end = " " )
        preorder(root.left)
        preorder(root.right)
     
def constructTrees(start, end):
 
    list = []

    if (start > end) :    
        list.append(None)
        return list

    for i in range(start, end + 1):
     
        leftSubtree = constructTrees(start, i - 1)
        rightSubtree = constructTrees(i + 1, end)
 
        for j in range(len(leftSubtree)) :
            left = leftSubtree[j]
            for k in range(len(rightSubtree)):
                right = rightSubtree[k]
                node = newNode(i)   
                node.left = left 
                node.right = right 
                list.append(node) 
    return list
 
if __name__ == '__main__':
    x=int(input("How many node you want to insert:"))
    
    if x==0:
        print("The tree is empty")
    else:
        totalTreesFrom1toN = constructTrees(1, x)
        print("total number of tree is : ",len(totalTreesFrom1toN))
        print("############################")      
        print("Preorder traversals of all constructed BSTs are")    
        for i in range(len(totalTreesFrom1toN)):
            print("Tree",i+1,"in Preorder --> ",end="")
            preorder(totalTreesFrom1toN[i])
            print()
 