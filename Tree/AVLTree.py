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
def right_rotate(self, node: TreeNode | None) -> TreeNode | None:
    """右旋"""
    child = node.left
    grand_child = child.right
    # 以 child 为原点，将 node 向右旋转
    child.right = node
    node.left = grand_child
    # 更新节点高度
    self.update_height(node)
    self.update_height(child)
    # 返回旋转后子树的根节点
    return child

# 2.左旋
def left_rotate(self, node: TreeNode | None) -> TreeNode | None:
    """左旋"""
    child = node.right
    grand_child = child.left
    # 以 child 为原点，将 node 向左旋转
    child.left = node
    node.right = grand_child
    # 更新节点高度
    self.update_height(node)
    self.update_height(child)
    # 返回旋转后子树的根节点
    return child

# 3.先左旋后右旋 & 先右旋后左旋
def rotate(self, node: TreeNode | None) -> TreeNode | None:
    """执行旋转操作，使该子树重新恢复平衡"""
    # 获取节点 node 的平衡因子
    balance_factor = self.balance_factor(node)
    # 左偏树
    if balance_factor > 1:
        if self.balance_factor(node.left) >= 0:
            # 右旋
            return self.right_rotate(node)
        else:
            # 先左旋后右旋
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
    # 右偏树
    elif balance_factor < -1:
        if self.balance_factor(node.right) <= 0:
            # 左旋
            return self.left_rotate(node)
        else:
            # 先右旋后左旋
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
    # 平衡树，无需旋转，直接返回
    return node

# 4.AVL树常见操作：插入节点
def insert(self, val):
    """插入节点"""
    self._root = self.insert_helper(self._root, val)

def insert_helper(self, node: TreeNode | None, val: int) -> TreeNode:
    """递归插入节点（辅助方法）"""
    if node is None:
        return TreeNode(val)
    # 1. 查找插入位置并插入节点
    if val < node.val:
        node.left = self.insert_helper(node.left, val)
    elif val > node.val:
        node.right = self.insert_helper(node.right, val)
    else:
        # 重复节点不插入，直接返回
        return node
    # 更新节点高度
    self.update_height(node)
    # 2.执行旋转操作，使该子树重新恢复平衡
    return self.rotate(node)

# 5.删除节点
def remove(self, val: int):
    """delete"""
    self._root = self.remove_helper(self._root, val)

def remove_helper(self, node: TreeNode | None, val: int) -> TreeNode | None:
    """递归删除节点"""
    if node is None:
        return None
    # 1.查找节点并删除
    if val < node.val:
        node.left = self.remove_helper(node.left, val)
    elif val > node.val:
        node.right = self.remove_helper(node.right, val)
    else:
        if node.left is None or node.right is None:
            child = node.left or node.right
            # 子节点数量 = 0 ，直接删除 node 并返回
            if child is None:
                return None
            # 子节点数量 = 1 ，直接删除 node
            else:
                node = child
        else:
            # 子节点数量 = 2，则将中序遍历的下一个节点删除，并用该节点替换当前节点
            temp = node.right
            while temp.left is not None:
                temp = temp.left
            node.right = self.remove_helper(node.right, temp.val)
            node.val = temp.val
    # 更新节点高度
    self.update_height(node)
    # 2.执行旋转操作，使该子树重新恢复平衡
    return self.rotate(node)
