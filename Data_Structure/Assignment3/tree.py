class EndOfTreeReached(BaseException):
    pass


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class BSTN:
    rot = 0

    def __init__(self):
        self.treeRoot = None
        self.tree = None
        setattr(BSTN, "rot", self.treeRoot)

    def addNode(self, node):
        root = self.treeRoot
        ro = root

        while root is not None:
            ro = root
            if node > root.value:
                root = root.right
            else:
                root = root.left
        if ro is None:
            self.treeRoot = Node(node)
        elif node > ro.value:
            ro.right = Node(node)
        else:
            ro.left = Node(node)

    def inorder(self, r, x=None):
        if x is None:
            x = []
        if r is None:
            return
        else:
            self.inorder(r.left, x)
            x.append(r.value)
            self.inorder(r.right, x)
            return x

    def searchNode(self, node, root=-1):
        if type(root) == int and root == -1:
            root = self.treeRoot
        ro = root
        while root is not None and root.value != node:
            ro = root
            if root is None:
                return False, None, ro
            if node > root.value:
                root = root.right
            else:
                root = root.left
        if root is None:
            return False, None, ro
        return True, root, ro

    def _getMostLeft(self, root):
        root = root.right
        ro = root
        while root is not None:
            ro = root
            root = root.left
        return ro

    def delNode(self, node):
        if type(node) == Node:
            exist = self.searchNode(node.value, node.right)
            s = False
        else:
            s = True
            exist = self.searchNode(node)
        if not exist[0]:
            if s:
                raise Exception("Element not found in tree")
            else:
                return
        else:
            root = exist[1]
            if root.left is None and root.right is None:
                if root is exist[2].right:
                    exist[2].right = None
                else:
                    exist[2].left = None
                return
            else:
                n = self._getMostLeft(root)
                if exist[2].right == root:
                    exist[2].right = n
                else:
                    exist[2].left = n
                self.delNode(n)

    def getHigh(self, node, root=-1):
        if type(root) == int and root == -1:
            z = self.searchNode(node)
            if not z[0]:
                return Exception("Element not in Tree")
            root = z[1]
        if root is None:
            return -1
        return 1 + self.getHigh(node, root.left)

    def leavesNum(self, root=-1):
        if type(root) == int and root == -1:
            root = self.treeRoot
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        s = self.leavesNum(root.left) + self.leavesNum(root.right)
        return s

    def maxPathSum(self, root=-1):
        if type(root) == int and root == -1:
            root = self.treeRoot
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.value
        s = self.maxPathSum(root.left), self.maxPathSum(root.right)
        return max(s) + root.value

    def __str__(self):
        if self.tree is None:
            self.tree = self.inorder(self.treeRoot)
        else:
            self.tree = None
            self.tree = self.inorder(self.treeRoot)
        return self.tree.__str__()

    def mirror(self, root=-1):
        if type(root) == int and root == -1:
            root = self.treeRoot
        if root is None:
            return
        root.left, root.right = root.right, root.left
        self.mirror(root.left)
        self.mirror(root.right)


class BSTA:
    def __init__(self):
        self.tree = [None]
        self.s = []

    @staticmethod
    def _getChildPairIndices(n):
        return n * 2 + 1, n * 2 + 2

    def addNode(self, node):
        root = 0
        while self.tree[root] is not None and self.tree[root] != node:
            l, r = self._getChildPairIndices(root)
            if r > len(self.tree):
                self.tree += [None] * 2 ** (self.getHigh(0))
            if node >= self.tree[root]:
                root = r
            else:
                root = l
        self.tree[root] = node

    def searchNode(self, node):
        root = 0
        while self.tree[root] is not None and self.tree[root] != node:
            l, r = self._getChildPairIndices(root)
            if r > len(self.tree):
                return False, None
            if node > self.tree[root]:
                root = r
            else:
                root = l
        if self.tree[root] is None:
            return False, None
        return True, root

    def _getMostLeft(self, node):
        l, r = self._getChildPairIndices(node)
        node = r
        while self.tree[node] is not None:
            l, r = self._getChildPairIndices(node)
            if r > len(self.tree) or self.tree[l] is None:
                break
            node = l
        return node

    def delNode(self, node):
        exist = self.searchNode(node)
        if not exist[0]:
            raise Exception("Element not found in tree")
        else:
            root = exist[1]
            l, r = self._getChildPairIndices(root)
            if r > len(self.tree) or (self.tree[r] == self.tree[l] is None):
                self.tree[root] = None
                return
            else:
                n = self._getMostLeft(root)
                v = self.tree[n]
                self.delNode(self.tree[n])
                self.tree[root] = v

    def getHigh(self, root=0):
        l, r = self._getChildPairIndices(root)
        if r > len(self.tree):
            return 1
        return 1 + self.getHigh(l)

    def leavesNum(self, root=0):
        if self.getHigh(root) == 1:
            if self.tree[root] is not None:
                return 1
            return 0
        l, r = self._getChildPairIndices(root)
        s = self.leavesNum(l) + self.leavesNum(r)
        return s

    def sort(self, root=0, x=None):
        if x is None:
            x = []
        l, r = self._getChildPairIndices(root)
        if r > len(self.tree):
            return
        self.sort(l, x)
        if self.tree[root] is not None:
            x.append(self.tree[root])
        self.sort(r, x)
        return x

    def maxPathSum(self, root=0):
        if self.getHigh(root) == 1:
            if self.tree[root] is not None:
                return self.tree[root]
            return 0
        l, r = self._getChildPairIndices(root)
        s = self.maxPathSum(l), self.maxPathSum(r)
        return max(s) + self.tree[root]

    def mirror(self, root=0):
        if self.getHigh(root) == 1:
            return
        l, r = self._getChildPairIndices(root)
        self.tree[l:r + 1] = self.tree[l:r + 1][::-1]
        self.mirror(l)
        self.mirror(r)

    def __str__(self):
        return self.tree.__str__()


t = BSTN()
t2 = BSTA()
x = [4, 2, 5, 1, 3, 12, 13]
for i in x:
    t.addNode(i)
    t2.addNode(i)
print(t2)
print(t)
(t.delNode(5))
(t2.delNode(5))
print(t2)
# print(t.getHigh(4))
print(t.leavesNum())
print(t2.leavesNum())
print(t.maxPathSum())
t.mirror()
# print(t.mirror())
print(t)
# print(t.getMostLeft(0))
