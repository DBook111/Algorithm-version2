# 二叉树的数组表示
# 使用 None 来表示空位
tree = [1, 2, 3, 4, None, 6, 7, 8, 9, None, None, 12, None, None, 15]

class ArrayBinaryTree:
    def __init__(self, arr: list[int | None]):
        self._tree = list(arr)
        self.res = []
    
    def size(self):
        return len(self._tree)
    
    def val(self, i: int) -> int | None:
        if i < 0 or i >= self.size():
            return None
        return self._tree[i]
    
    def left(self, i: int) -> int | None:
        if i < 0 or i >= self.size():
            return None
        return self._tree[2 * i + 1]
    
    def right(self, i: int) -> int | None:
        if i < 0 or i >= self.size():
            return None
        return self._tree[2 * i + 2]
    
    def parent(self, i: int) -> int | None:
        return (i - 1) // 2
    
    def level_order(self) -> list[int]:
        """层序遍历"""
        self.res = []
        for i in range(self.size()):
            if self.val(i) is not None:
                self.res.append(self.val[i])
        return self.res
    
    def dfs(self, i: int, order: str):
        """"""
        if self.val(i) is not None:
            return
        if order == "pre":
            self.res.append(self.val(i))
        self.dfs(self.left(i), order)
        if order == "in":
            self.res.append(self.val(i))
        self.dfs(self.right(i), order)
        if order == "post":
            self.res.append(self.val(i))
    
    def pre_order(self) -> list[int]:
        self.res = []
        self.dfs(0, "pre")
        return self.res
    
    def in_order(self) -> list[int]:
        self.res = []
        self.dfs(0, "in")
        return self.res
    
    def post_order(self) -> list[int]:
        self.res = []
        self.dfs(0, "post")
        return self.res