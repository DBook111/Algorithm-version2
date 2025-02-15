# 给定一棵二叉树的前序遍历 preorder 和中序遍历 inorder ，请从中构建二叉树，
# 返回二叉树的根节点。假设二叉树中没有值重复的节点

# 为了提升查询 m 的效率，我们借助一个哈希表 hmap 来存储数组 inorder 中元素到索引的映射
class TreeNode():
    def __init__(self, val: int):
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


def dfs(preorder: list[int], 
        inorder_map: dict[int, int],
        i: int,
        l: int,
        r: int
        ) -> TreeNode | None:
    """构建二叉树：分治"""
    # 子树区间为空时终止
    if r - l < 0:
        return None
    # 初始化根节点
    root = TreeNode(preorder[i])
    # 查询 m ，从而划分左右子树
    m = inorder_map[preorder[i]]
    # 子问题：构建左子树
    root.left = dfs(preorder, inorder_map, i + 1, l, m - 1)
    # 子问题：构建右子树
    root.right = dfs(preorder, inorder_map, i + 1 + m - l, m + 1, r)
    # 返回根节点
    return root



def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    """构建二叉树"""
    # 初始化哈希表，存储 inorder 元素到索引的映射
    inorder_map = {val: i for i, val in enumerate(inorder)}
    root = dfs(preorder, inorder_map, 0, 0, len(inorder) - 1)
    return root


"""Driver Code"""
if __name__ == "__main__":
    preorder = [3, 9, 2, 1, 7]
    inorder = [9, 3, 1, 2, 7]
    print(f"前序遍历 = {preorder}")
    print(f"中序遍历 = {inorder}")
    root = build_tree(preorder, inorder)
    
    # 后序遍历
    res = []
    def post(root: TreeNode, res: list[int]):
        if root is None:
            return
        post(root.left, res)
        post(root.right, res)
        res.append(root.val)
    post(root, res)
    print("后序遍历", res)