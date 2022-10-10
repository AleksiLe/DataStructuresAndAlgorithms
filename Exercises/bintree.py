class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None

    
class BST:
    def __init__(self):
        self.root = None

    def search(self,key):
        if self.root is None:
            self.root = Node(key)
            return True
        else:
            node=self.root
            while(True):
                if node == None:
                    return False
                elif node.key == key:
                    return True
                if node.key > key:
                    if node.left == key:
                        return True
                    else:
                        node = node.left
                elif node.key < key:
                    if node.right == key:
                        return True
                    else:
                        node = node.right
    def insert(self,key):
        if self.root is None:
            self.root = Node(key)
            return
        else:
            node=self.root
            while(True):
                if node.key > key:
                    if node.left is None:
                        node.left = Node(key)
                        return
                    else:
                        node = node.left
                elif node.key < key:
                    if node.right is None:
                        node.right = Node(key)
                        return 
                    else:
                        node = node.right
    def preorder(self):
        self.preorderHelper(self.root)
        print()
    def preorderHelper(self,node):
        if node == None:
            return
        print(node.key, end=' ')
        self.preorderHelper(node.left)
        self.preorderHelper(node.right)

    def minValueNode(self,node):
        while(node.right != None):
            node = node.right
        return node
    def remove(self,key):
        self.removeHelper(self.root,key)
    def removeHelper(self,node,key):

        if node == None:
            return node
        if key < node.key:
            node.left = self.removeHelper(node.left, key)
        elif(key > node.key):
            node.right = self.removeHelper(node.right, key)
        else:
            if node.left == None:
                temp = node.right
                node = None
                return temp

            elif node.right == None:
                temp = node.left
                node = None
                return temp

            temp = self.minValueNode(node.left)
            node.key = temp.key
            node.left = self.removeHelper(node.left, temp.key)

        return node
        



    
