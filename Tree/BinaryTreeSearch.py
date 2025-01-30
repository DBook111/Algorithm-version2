class TreeNode:
    def __init__(self, val: int):
        self.val: int = val 
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def search(self, num: int) -> TreeNode | None:
    """"""
    cur = self._root
    # 
    while cur is not None:
        if cur.val < num:
            cur = cur.right
        elif cur.val > num:
            cur = cur.left
        else:
            break
    
    return cur

def insert(self, num: int):
    """"""
    # 若树为空，则初始化根节点
    if self._root is None:
        self._root = TreeNode(num)
        return
    # search for loop
    cur, pre = self._root, None
    while cur is not None:
        if cur.val == num:
            return
        pre = cur
        if cur.val < num:
            cur = cur.right
        else:
            cur = cur.left
    # insert
    node = TreeNode(num)
    if pre.val < num:
        pre.right = node
    else:
        pre.left = node
    
def remove(self, num: int):
    # 
    if self._root is None:
        return
    cur, pre = self._root, None
    while cur is not None:
        if cur.val == num:
            break
        pre = cur
        if cur.val > num:
            cur = cur.left
        else:
            cur = cur.right
    # 若无待删除的节点，直接返回
    if cur is None:
        return
    # 子节点的数量，0或1
    if cur.left is None or cur.right is None:
        # 当子节点数量 = 0 / 1 时， child = null / 该子节点
        child = cur.left or cur.right
        # 删除节点 cur
        if cur != self._root:
            if pre.left == cur:
                pre.left = child
            else:
                pre.right = child
        else:
            self._root = child
    # 子节点数量 = 2
    else:
        # 获取中序遍历中 cur 的下一个节点
        tmp: TreeNode = cur.right
        while tmp.left is not None:
            tmp = tmp.left
        # 递归删除节点 tmp
        self.remove(tmp.val)
        cur.val = tmp.val
