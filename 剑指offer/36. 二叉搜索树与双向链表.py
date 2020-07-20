# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。
#
#
#
#  为了让您更好地理解问题，以下面的二叉搜索树为例：
#
#
#
#
#
#
#
#  我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是
# 第一个节点。
#
#  下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。
#
#
#
#
#
#
#
#  特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。
#
#
#
#  注意：本题与主站 426 题相同：https://leetcode-cn.com/problems/convert-binary-search-tree-
# to-sorted-doubly-linked-list/
#
#  注意：此题对比原题有改动。
#  Related Topics 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    pre = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        dummy = Node(0, None, None)
        self.pre = dummy
        self.process(root)
        # 循环链表，表头和尾节点链接
        self.pre.right = dummy.right
        dummy.right.left = self.pre
        return dummy.right

    def process(self, cur):
        if not cur:
            return None
        # 中序递归，在二叉搜索树中值为“从小到大”
        self.process(cur.left)
        # 前节点和当前节点双向链接
        self.pre.right = cur
        cur.left = self.pre
        self.pre = cur
        self.process(cur.right)

# leetcode submit region end(Prohibit modification and deletion)
