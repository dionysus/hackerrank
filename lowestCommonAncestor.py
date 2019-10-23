class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
#------------------------------------------------------------------------------#

def lca(root, v1, v2):
  #Enter your code here
    v1_path = helper(root, v1)
    v2_path = helper(root, v2)

    if len(v1_path) <= len(v2_path):
        return helperIndex(v1_path, v2_path)
    else:
        return helperIndex(v2_path, v1_path)
    
def helperIndex(v1_path, v2_path):
    i = 0
    j = 0

    while i < len(v1_path) and j < len(v2_path):
        if v1_path[i] == v2_path[j]:
            return v1_path[i]
        if v1_path[i] > v2_path[j]:
            j += 1
        if v1_path[i] < v2_path[j]:
            i += 1

def helper(root, val):

    if root is None:
        return None

    if root.info == val:
        return [root]
    
    if root.left is None and root.right is None:
        return None
    
    else:
        if val < root.info:
            branch = helper(root.left, val)
        else:
            branch = helper(root.right, val)

        if branch is None:
            return None
        else:
            branch.append(root)
            return branch

#------------------------------------------------------------------------------#

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
