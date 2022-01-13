# -*- coding:utf8 -*-
# @Time：2022/1/13 10:22 AM
# @Author： Huang Jeff

import numpy as np

a = np.arange(24)
print(a.ndim)   # a 现只有一个维度，似一维数组
b = a.reshape(2, 4, 3)  # b 现在拥有三个维度，似三维数组
print(b.ndim)


a = np.array([[1, 2, 3], [4, 5, 6]])  # 输出2行3列数组
print(a.shape)
