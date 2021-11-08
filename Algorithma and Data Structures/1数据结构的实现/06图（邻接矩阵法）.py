#@Time : 2021/11/29:06
#@Author : xujian

#图  (顶点集合，边集合)
#   临近矩阵---》用于节点少，但是节点联系多的图

#       vectices  edge
#       以我手写的笔记图为例


#1.使用list
#顶点集合
vertices=[1,2,3,4]
#边集合
edges=[[0,1,1,1],[1,0,1,0],[1,1,0,1],[1,0,1,0]]

print(edges)   #[[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]

#2.使用numpy
import numpy as np
vertices2=np.array([1,2,3,4])
edges2=np.array([
    [0,1,1,1],
    [1,0,1,0],
    [1,1,0,1],
    [1,0,1,0]
])
print(edges2)
                        # [[0 1 1 1]
                        #  [1 0 1 0]
                        #  [1 1 0 1]
                        #  [1 0 1 0]]


























