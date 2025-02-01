# 多次增删后，二叉搜索树可能退化为链表

# 节点的高度
class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.height: int = 0
        self.left: TreeNode | None = None
        self.ritht: TreeNode | None = None

# “节点高度”是指从该节点到它的最远叶节点的距离，即所经过的“边”的数量。需要特别注意的是，叶节点的高度为 
#  ，而空节点的高度为 
#  。我们将创建两个工具函数，分别用于获取和更新节点的高度：

def height(self, node: TreeNode | None) -> int:
    if node is not None:
        return node.height
    return -1

def update_height(self, node: TreeNode | None):
    """更新节点高度"""
    # 节点高度等于最高子树 + 1
    node.height = max([self.height(node.left), self.height(node.right)]) + 1


# 节点平衡因子 = 左子树高度 - 右子树高度
# 规定空节点的平衡因子为0。
def balance_factor(self, node: TreeNode | None) -> int:
    """获取平衡因子"""
    # 空节点平衡因子为0
    if node is None:
        return 0
    return self.height(node.left) - self.height(node.right)

# 设平衡因子为f，则一棵AVL树的平衡因子皆满足 -1 <= f <= 1

# AVL树旋转：在不影响二叉树的中序遍历的前提下，使失衡节点重新恢复平衡。

# 1.右旋
