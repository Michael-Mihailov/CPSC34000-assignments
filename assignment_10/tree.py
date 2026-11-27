class Node:
    def __init__(self, data):
        self.key = data[0]
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def print_record(self):
        print("Item Number:", self.data[0])
        print("Item:", self.data[1])
        print("Cost:", "${:.2f}".format(self.data[2]))
        print("Type:", self.data[3])
        print("Category:", self.data[4])
        print("Quantity in Stock:", self.data[5])

    def insert(self, other_node):
        if other_node.key == self.key:
            return False
        elif other_node.key < self.key:
            if self.left is None:
                self.left = other_node
                other_node.parent = self
                return True
            return self.left.insert(other_node)
        else:
            if self.right is None:
                self.right = other_node
                other_node.parent = self
                return True
            return self.right.insert(other_node)

    def search(self, key):
        if self.key == key:
            return self
        if key < self.key:
            if self.left is None:
                return None
            return self.left.search(key)
        if self.right is None:
            return None
        return self.right.search(key)


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return True
        if self.root.insert(new_node):
            return True
        print("The key already existed. Record not added")
        return False

    def search(self, key):
        if self.root is None:
            return None
        return self.root.search(key)

    def delete(self, key):
        target_node = self.search(key)
        if target_node is None:
            return False

        if target_node.left is not None and target_node.right is not None:
            successor = target_node.right
            while successor.left is not None:
                successor = successor.left

            target_node.key = successor.key
            target_node.data = successor.data
            
            target_node = successor # we still need to delete the successor now

        child_node = None # the target node has at most one child in this case
        if target_node.left is not None:
            child_node = target_node.left
        elif target_node.right is not None:
            child_node = target_node.right

        if target_node.parent is None: # we are deleting the root
            self.root = child_node
        elif target_node.parent.left == target_node:
            target_node.parent.left = child_node
        else:
            target_node.parent.right = child_node

        if child_node is not None:
            child_node.parent = target_node.parent

        return True

    def _display_inorder(self, node):
        if node is not None:
            self._display_inorder(node.left)
            node.print_record()
            print("--------------------")
            self._display_inorder(node.right)

    def display(self):
        if self.root is None:
            print("Nothing to display. Tree is empty")
        else:
            self._display_inorder(self.root)