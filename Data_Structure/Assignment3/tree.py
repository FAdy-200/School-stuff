class EndOfTreeReached(BaseException):
    pass


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class BST:
    """
    exam night
    """

    def __init__(self):
        self.__lastFound = None

    def addNode(self, root, val):
        if val >= root.value:
            if root.right is None:
                root.right = Node(val)
            else:
                self.addNode(root.right, val)
        else:
            if root.left is None:
                root.left = Node(val)
            else:
                self.addNode(root.left, val)

    def search(self, root, val):
        if val > root.value:
            if root.right is None:
                return False
            else:
                return self.search(root.right, val)
        elif val < root.value:
            if root.left is None:
                return False
            else:
                return self.search(root.left, val)
        else:
            self.__lastFound = root
            return True

    def __findNodeParent(self, root, node):
        if root.left is node:
            return root, "left"
        elif root.right is node:
            return root, "right"
        elif node.value > root.value:
            return self.__findNodeParent(root.right, node)
        elif node.value < root.value:
            return self.__findNodeParent(root.left, node)
        else:
            return root, "right"

    def __hiddenDelete(self, root, DNode):
        if root is None:
            return
        parent, pos = self.__findNodeParent(root, DNode)
        if DNode.left is None:
            if DNode.right is None:
                exec(f"parent.{pos} = None")
            else:
                exec(f"parent.{pos} = DNode.right")
        elif DNode.right is None:
            exec(f"parent.{pos} = DNode.left")
        else:
            toReplace = self.__leftMost(root.right)
            self.__hiddenDelete(DNode, toReplace)
            toReplace.left = DNode.left
            toReplace.right = DNode.right
            exec(f"parent.{pos} = toReplace")
        if root is not parent:
            return parent
        return root

    def delete(self, root, val):
        s = self.search(root, val)
        if s:
            self.__hiddenDelete(root, self.__lastFound)
        else:
            raise Exception("Value not in Tree")
        return root

    def __leftMost(self, root):
        if root.left is None:
            return root
        return self.__leftMost(root.left)


ro = Node(8)
b = BST()
b.addNode(ro, 5)
b.addNode(ro, 7)
b.addNode(ro, 4)
b.addNode(ro, 9)
print()
ro = b.delete(ro, 5)
print(ro)

#
# class BSTN:
#     rot = 0
#
#     def __init__(self):
#         self.treeRoot = None
#         self.tree = None
#         BSTN.rot = self.treeRoot
#
#     def addNode(self, node):
#         ro = self.treeRoot
#         ro = ro
#
#         while ro is not None:
#             ro = ro
#             if node > ro.value:
#                 ro = ro.right
#             else:
#                 ro = ro.left
#         if ro is None:
#             self.treeRoot = Node(node)
#         elif node > ro.value:
#             ro.right = Node(node)
#         else:
#             ro.left = Node(node)
#
#     def inorder(self, r, x=None):
#         if x is None:
#             x = []
#         if r is None:
#             return
#         else:
#             self.inorder(r.left, x)
#             x.append(r.value)
#             self.inorder(r.right, x)
#             return x
#
#     def searchNode(self, node, ro=-1):
#         if type(ro) == int and ro == -1:
#             ro = self.treeRoot
#         ro = ro
#         while ro is not None and ro.value != node:
#             ro = ro
#             if ro is None:
#                 return False, None, ro
#             if node > ro.value:
#                 ro = ro.right
#             else:
#                 ro = ro.left
#         if ro is None:
#             return False, None, ro
#         return True, ro, ro
#
#     def _getMostLeft(self, ro):
#         ro = ro.right
#         ro = ro
#         while ro is not None:
#             ro = ro
#             ro = ro.left
#         return ro
#
#     def delNode(self, node):
#         if type(node) == Node:
#             exist = self.searchNode(node.value, node.right)
#             s = False
#         else:
#             s = True
#             exist = self.searchNode(node)
#         if not exist[0]:
#             if s:
#                 raise Exception("Element not found in tree")
#             else:
#                 return
#         else:
#             ro = exist[1]
#             if ro.left is None and ro.right is None:
#                 if ro is exist[2].right:
#                     exist[2].right = None
#                 else:
#                     exist[2].left = None
#                 return
#             else:
#                 n = self._getMostLeft(ro)
#                 if exist[2].right == ro:
#                     exist[2].right = n
#                 else:
#                     exist[2].left = n
#                 self.delNode(n)
#
#     def getHigh(self, node, ro=-1):
#         if type(ro) == int and ro == -1:
#             z = self.searchNode(node)
#             if not z[0]:
#                 return Exception("Element not in Tree")
#             ro = z[1]
#         if ro is None:
#             return -1
#         return 1 + self.getHigh(node, ro.left)
#
#     def leavesNum(self, ro=-1):
#         if type(ro) == int and ro == -1:
#             ro = self.treeRoot
#         if ro is None:
#             return 0
#         if ro.left is None and ro.right is None:
#             return 1
#         s = self.leavesNum(ro.left) + self.leavesNum(ro.right)
#         return s
#
#     def maxPathSum(self, ro=-1):
#         if type(ro) == int and ro == -1:
#             ro = self.treeRoot
#         if ro is None:
#             return 0
#         if ro.left is None and ro.right is None:
#             return ro.value
#         s = self.maxPathSum(ro.left), self.maxPathSum(ro.right)
#         return max(s) + ro.value
#
#     def __str__(self):
#         if self.tree is None:
#             self.tree = self.inorder(self.treeRoot)
#         else:
#             self.tree = None
#             self.tree = self.inorder(self.treeRoot)
#         return self.tree.__str__()
#
#     def mirror(self, ro=-1):
#         if type(ro) == int and ro == -1:
#             ro = self.treeRoot
#         if ro is None:
#             return
#         ro.left, ro.right = ro.right, ro.left
#         self.mirror(ro.left)
#         self.mirror(ro.right)
#
#
# class BSTA:
#     def __init__(self):
#         self.tree = [None]
#         self.s = []
#
#     @staticmethod
#     def _getChildPairIndices(n):
#         return n * 2 + 1, n * 2 + 2
#
#     def addNode(self, node):
#         ro = 0
#         while self.tree[ro] is not None and self.tree[ro] != node:
#             l, r = self._getChildPairIndices(ro)
#             if r > len(self.tree):
#                 self.tree += [None] * 2 ** (self.getHigh(0))
#             if node >= self.tree[ro]:
#                 ro = r
#             else:
#                 ro = l
#         self.tree[ro] = node
#
#     def searchNode(self, node):
#         ro = 0
#         while self.tree[ro] is not None and self.tree[ro] != node:
#             l, r = self._getChildPairIndices(ro)
#             if r > len(self.tree):
#                 return False, None
#             if node > self.tree[ro]:
#                 ro = r
#             else:
#                 ro = l
#         if self.tree[ro] is None:
#             return False, None
#         return True, ro
#
#     def _getMostLeft(self, node):
#         l, r = self._getChildPairIndices(node)
#         node = r
#         while self.tree[node] is not None:
#             l, r = self._getChildPairIndices(node)
#             if r > len(self.tree) or self.tree[l] is None:
#                 break
#             node = l
#         return node
#
#     def delNode(self, node):
#         exist = self.searchNode(node)
#         if not exist[0]:
#             raise Exception("Element not found in tree")
#         else:
#             ro = exist[1]
#             l, r = self._getChildPairIndices(ro)
#             if r > len(self.tree) or (self.tree[r] == self.tree[l] is None):
#                 self.tree[ro] = None
#                 return
#             else:
#                 n = self._getMostLeft(ro)
#                 v = self.tree[n]
#                 self.delNode(self.tree[n])
#                 self.tree[ro] = v
#
#     def getHigh(self, ro=0):
#         l, r = self._getChildPairIndices(ro)
#         if r > len(self.tree):
#             return 1
#         return 1 + self.getHigh(l)
#
#     def leavesNum(self, ro=0):
#         if self.getHigh(ro) == 1:
#             if self.tree[ro] is not None:
#                 return 1
#             return 0
#         l, r = self._getChildPairIndices(ro)
#         s = self.leavesNum(l) + self.leavesNum(r)
#         return s
#
#     def sort(self, ro=0, x=None):
#         if x is None:
#             x = []
#         l, r = self._getChildPairIndices(ro)
#         if r > len(self.tree):
#             return
#         self.sort(l, x)
#         if self.tree[ro] is not None:
#             x.append(self.tree[ro])
#         self.sort(r, x)
#         return x
#
#     def maxPathSum(self, ro=0):
#         if self.getHigh(ro) == 1:
#             if self.tree[ro] is not None:
#                 return self.tree[ro]
#             return 0
#         l, r = self._getChildPairIndices(ro)
#         s = self.maxPathSum(l), self.maxPathSum(r)
#         return max(s) + self.tree[ro]
#
#     def mirror(self, ro=0):
#         if self.getHigh(ro) == 1:
#             return
#         l, r = self._getChildPairIndices(ro)
#         self.tree[l:r + 1] = self.tree[l:r + 1][::-1]
#         self.mirror(l)
#         self.mirror(r)
#
#     def __str__(self):
#         return self.tree.__str__()

#
# t = BSTN()
# t2 = BSTA()
# x = [4, 2, 5, 1, 3, 12, 13]
# for i in x:
#     t.addNode(i)
#     t2.addNode(i)
# print(t2)
# print(t)
# (t.delNode(5))
# (t2.delNode(5))
# print(t2)
# # print(t.getHigh(4))
# print(t.leavesNum())
# print(t2.leavesNum())
# print(t.maxPathSum())
# t.mirror()
# # print(t.mirror())
# print(t)
# # print(t.getMostLeft(0))
