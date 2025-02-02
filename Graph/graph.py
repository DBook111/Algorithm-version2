# 以下是基于邻接矩阵表示图的实现代码：

class GraphAdjMat:
    """基于邻接矩阵实现的无向图类"""
    def __init__(self, vertices: list[int], edges: list[list[int]]):
        # vertices list
        self.vertices: list[int] = []
        self.adj_mat: list[list[int]] = []
        # add vertex
        for val in vertices:
            self.add_vertex(val)
        # add edge
        for e in edges:
            self.add_edge(e[0], e[1])
    
    def size(self) -> int:
        """num of vertices"""
        return len(self.vertices)
    
    def add_vertex(self, val: int):
        """add vertex"""
        # 向顶点列表中添加新顶点的值
        self.vertices.append(val)
        # 在邻接矩阵中添加一行, 一列
        n = self.size()
        new_row = [0] * n
        self.adj_mat.append(new_row)
        for row in self.adj_mat:
            row.append(0)
    
    def remove_vertex(self, index: int):
        """删除顶点"""
        if index >= self.size():
            raise IndexError("越界")
        # 在顶点列表中移除索引 index 的顶点
        self.vertices.pop(index)
        # 在邻接矩阵中删除索引 index 的行, 列
        self.adj_mat.pop(index)
        for row in self.adj_mat:
            row.pop(index)
    
    def add_edge(self, i: int, j: int):
        """add edge"""
        # outline
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError()
        self.adj_mat[i][j] = 1
        self.adj_mat[j][i] = 1
    
    def remove_edge(self, i: int, j: int):
        """delete edge"""
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError()
        self.adj_mat[i][j] = 0
        self.adj_mat[j][i] = 0
    
    def print(self):
        """"""
        print("顶点列表 = ", self.vertices)
        print("邻接矩阵 = ")
        print_matrix(self.adj_mat)  

"""Driver Code"""
if __name__ == "__main__":
    # 初始化无向图
    vertices = [1, 3, 2, 5, 4]
    edges = [[0, 1], [0, 3], [1, 2], [2, 3], [2, 4], [3, 4]]
    graph = GraphAdjMat(vertices, edges)

    # 添加边
    # 顶点 1, 2 的索引分别为 0, 2
    graph.add_edge(0, 2)

    # 删除边
    # 顶点 1, 3 的索引分别为 0, 1
    graph.remove_edge(0, 1)

    # 添加顶点
    graph.add_vertex(6)

    # 删除顶点
    # 顶点 3 的索引为 1
    graph.remove_vertex(1)