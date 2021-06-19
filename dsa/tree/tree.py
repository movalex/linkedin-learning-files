class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def search(self, target):
        if self.data == target:
            return self

        if self.left and self.data > target:
            return self.left.search(target)

        if self.right and self.data < target:
            return self.right.search(target)

    def traverseInorder(self):
        if self.left:
            self.left.traversePreorder()

        print(self.data)

        if self.right:
            self.right.traversePreorder()

    def traversePreorder(self):
        print(self.data)

        if self.left:
            self.left.traversePreorder()

        if self.right:
            self.right.traversePreorder()

    def traversePostorder(self):
        if self.left:
            self.left.traversePreorder()

        if self.right:
            self.right.traversePreorder()

        print(self.data)

    def height(self, h=0):
        leftHeight = self.left.height(h+1) if self.left else h
        rightHeight = self.right.height(h+1) if self.right else h
        return max(leftHeight, rightHeight)

    def getNodesAtDepth(self, depth, nodes=[]):

        if depth==0:
            nodes.append(self.data)
            return nodes

        if self.left:
            self.left.getNodesAtDepth(depth-1, nodes)

        if self.right:
            self.right.getNodesAtDepth(depth-1, nodes)

        return nodes

    def add(self, data):
        if self.data == data:
            return

        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.add(data)
                self.left = self.left.fixImbalanceIfExists()

        if data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.add(data)
                self.left = self.right.fixImbalanceIfExists()

    def findmin(self):
        if self.left:
            return self.left.findmin()
        return self.data

    def delete(self, target):
        if target == self.data:
            # do the deletion
            if self.left and self.right:
                #RTFM -  right tree find minimum
                min_value = self.right.findmin()
                self.data = min_value
                self.right = self.right.delete(min_value)
                return self
            else:
                return self.left or self.right

        if self.left and target < self.data:
            self.left = self.left.delete(target)
        if self.right and target > self.data:
            self.right = self.right.delete(target)

        return self.fixImbalanceIfExists()

    def is_balanced(self):
        left_height = self.left.height()+1 if self.left else 0
        right_height = self.right.height()+1 if self.right else 0
        return abs(left_height - right_height) < 2

    def getLeftRightHeightDifference(self):
        left_height = self.left.height()+1 if self.left else 0
        right_height = self.right.height()+1 if self.right else 0
        return left_height - right_height

    def fixImbalanceIfExists(self):
        if self.getLeftRightHeightDifference() > 1:
            #left imbalance
            if self.left.getLeftRightHeightDifference() > 0:
                # left left imbalance
                return rotateRight(self)
            else:
                # leift right
                self.left = rotateLeft(self.left)
                return rotateRight(self)
        elif self.getLeftRightHeightDifference() < -1:
            #right imbalance
            if self.right.getLeftRightHeightDifference() < 0:
                # right right imbalance
                return rotateLeft(self)
            else:
                # left left imbalance
                self.right = rotateRight(self.right)
                return rotateLeft(self)
        return self

    def rebalance(self):
        if self.left:
            self.left.rebalance()
            self.left = self.left.fixImbalanceIfExists()
        if self.right:
            self.right.rebalance()
            self.right = self.right.fixImbalanceIfExists()


def rotateRight(root):
    pivot = root.left
    reattachNode = pivot.right
    root.left = reattachNode
    pivot.right = root
    return pivot

def rotateLeft(root):
    pivot = root.right
    reattachNode = pivot.left
    root.right = reattachNode
    pivot.left = root
    return pivot


class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def search(self, target):
        return self.root.search()

    def traversePreorder(self):
        return self.root.traversePreorder()

    def traversePostorder(self):
        return self.root.traversePostorder()

    def traverseInorder(self):
        return self.root.traverseInorder()

    def getNodesAtDepth(self, depth, nodes=[]):
        return self.root.getNodesAtDepth(depth, nodes=nodes)

    def display(self):
        return self.root.display()
    
    def add(self, data):
        self.root.add(data)
        self.root = self.root.fixImbalanceIfExists()

    def delete(self, data):
        self.root = self.root.delete(data)

    def rebalance(self):
        self.root.rebalance()
        self.root = self.root.fixImbalanceIfExists()

# tree = Tree(Node(50))
# tree.root.left = Node(25)
# tree.root.right = Node(75)
# tree.root.left.left = Node(10)
# tree.root.left.right = Node(35)
# tree.root.right.left = Node(27)
# tree.root.right.right = Node(22)
# tree.root.left.right.left = Node(30)
# tree.root.left.right.right = Node(42)
# tree.root.left.left.left = Node(5)
# tree.root.left.left.right = Node(13)
# tree.root.left.left.left.left = Node(2)

# print("Traverse Preorder")
# tree.traversePreorder()
#
# print("Traverse Inorder")
# tree.traverseInorder()
#
# print("Traverse Postorder")
# tree.traversePostorder()
#
# print(tree.root.height(), "height")

# print(tree.getNodesAtDepth(1), "nodes at depth")

# print(tree.getNodesAtDepth(0))
# print(tree.getNodesAtDepth(1, nodes = []))

tree = Tree(Node(50))
tree.root.left = Node(25)
tree.root.right = Node(75)
tree.add(55)
tree.add(78)
tree.add(77)
tree.add(80)
tree.display()
# tree.delete(50)
print(tree.root.height())
print(tree.root.is_balanced())
print(tree.root.left.is_balanced())

# tree.display()