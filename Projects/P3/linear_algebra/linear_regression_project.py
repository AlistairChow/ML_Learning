
# coding: utf-8

# In[1]:


# 任意选一个你喜欢的整数，这能帮你得到稳定的结果
seed = 9999


# # 欢迎来到线性回归项目
# 
# 若项目中的题目有困难没完成也没关系，我们鼓励你带着问题提交项目，评审人会给予你诸多帮助。
# 
# 所有选做题都可以不做，不影响项目通过。如果你做了，那么项目评审会帮你批改，也会因为选做部分做错而判定为不通过。
# 
# 其中非代码题可以提交手写后扫描的 pdf 文件，或使用 Latex 在文档中直接回答。

# # 1 矩阵运算
# 
# ## 1.1 创建一个 4*4 的单位矩阵

# In[2]:


# 这个项目设计来帮你熟悉 python list 和线性代数
# 你不能调用任何NumPy以及相关的科学计算库来完成作业


# 本项目要求矩阵统一使用二维列表表示，如下：
A = [[1,2,3], 
     [2,3,3], 
     [1,2,5]]

B = [[1,2,3,5], 
     [2,3,3,5], 
     [1,2,5,1]]

# 向量也用二维列表表示
C = [[1],
     [2],
     [3]]

#TODO 创建一个 4*4 单位矩阵
I = [[1,0,0,0],
     [0,1,0,0],
     [0,0,1,0],
     [0,0,0,1]]


# ## 1.2 返回矩阵的行数和列数

# In[3]:


# TODO 返回矩阵的行数和列数
def shape(M):
    
    row = len(M)
    
    try:
        col = len(M[0]) if row > 0 else 0
    except TypeError:
        col = 0
    
    return row, col


# In[4]:


# 运行以下代码测试你的 shape 函数
get_ipython().magic(u'run -i -e test.py LinearRegressionTestCase.test_shape')


# ## 1.3 每个元素四舍五入到特定小数数位

# In[5]:


# TODO 每个元素四舍五入到特定小数数位
# 直接修改参数矩阵，无返回值
def matxRound(M, decPts=4):
    
    row, col = shape(M)
    for r in range(row):
        for c in range(col):
            M[r][c] = round(M[r][c], decPts)


# In[6]:


# 运行以下代码测试你的 matxRound 函数
get_ipython().magic(u'run -i -e test.py LinearRegressionTestCase.test_matxRound')


# ## 1.4 计算矩阵的转置

# In[7]:


# TODO 计算矩阵的转置
def transpose(M):
    '''
    matrix = []
    row, col = shape(M)
    
    if col == 0:
        return [[m] for m in M]
    
    for c in range(col):
        m = []
        for r in range(row):
            m.append(M[r][c])
        matrix.append(m)
        
    return matrix
    '''
    #zip()函数将可迭代对象打包为成一个个元组
    #zip(*M)与zip()相反，将元组解压为二维矩阵
    #再用列表推导式遍历解压的二维矩阵，并将遍历出的元组转换为list对象
    return [list(col) for col in zip(*M)]
    


# In[8]:


# 运行以下代码测试你的 transpose 函数
get_ipython().magic(u'run -i -e test.py LinearRegressionTestCase.test_transpose')


# ## 1.5 计算矩阵乘法 AB

# In[9]:


# TODO 计算矩阵乘法 AB，如果无法相乘则raise ValueError
def matxMultiply(A, B):
    
    row_a, col_a = shape(A)
    row_b, col_b = shape(B)
    
    #矩阵A的列数等于矩阵B的行数才能相乘
    if col_a != row_b:
        raise ValueError
    
    '''
    matrix = []
    
    #乘积的行数等于矩阵A的行数，乘积的列数等于矩阵B的列数
    for r in range(row_a):
        m = []
        for c in range(col_b):
            #乘积的第r行第c列的元素等于矩阵A的第r行的元素与矩阵B的第c列的元素的乘积之和
            m.append(sum(a*b for a,b in zip(A[r], [b[c] for b in B])))

        matrix.append(m)
        
    return matrix
    '''
    
    #将B进行转置,即B_T的行为B的列
    B_T = transpose(B)
    #遍历A的行与B_T的行的元素，返回乘积的和所构成的列表
    return [[sum((a*b) for a, b in zip(row, col)) for col in B_T] for row in A]


# In[10]:


# 运行以下代码测试你的 matxMultiply 函数
get_ipython().magic(u'run -i -e test.py LinearRegressionTestCase.test_matxMultiply')


# ---
# 
# # 2 Gaussign Jordan 消元法
# 
# ## 2.1 构造增广矩阵
# 
# $ A = \begin{bmatrix}
#     a_{11}    & a_{12} & ... & a_{1n}\\
#     a_{21}    & a_{22} & ... & a_{2n}\\
#     a_{31}    & a_{22} & ... & a_{3n}\\
#     ...    & ... & ... & ...\\
#     a_{n1}    & a_{n2} & ... & a_{nn}\\
# \end{bmatrix} , b = \begin{bmatrix}
#     b_{1}  \\
#     b_{2}  \\
#     b_{3}  \\
#     ...    \\
#     b_{n}  \\
# \end{bmatrix}$
# 
# 返回 $ Ab = \begin{bmatrix}
#     a_{11}    & a_{12} & ... & a_{1n} & b_{1}\\
#     a_{21}    & a_{22} & ... & a_{2n} & b_{2}\\
#     a_{31}    & a_{22} & ... & a_{3n} & b_{3}\\
#     ...    & ... & ... & ...& ...\\
#     a_{n1}    & a_{n2} & ... & a_{nn} & b_{n} \end{bmatrix}$

# In[11]:


# TODO 构造增广矩阵，假设A，b行数相同
def augmentMatrix(A, b):
    '''
    matrix = []
    for row in range(len(A)):
        matrix.append(A[row]+b[row])

    return matrix
    '''
    
    #使用列表推导式简化实现
    return [row_a + row_b for row_a, row_b in zip(A, b)]


# In[12]:


# 运行以下代码测试你的 augmentMatrix 函数
get_ipython().magic(u'run -i -e test.py LinearRegressionTestCase.test_augmentMatrix')


# ## 2.2 初等行变换
# - 交换两行
# - 把某行乘以一个非零常数
# - 把某行加上另一行的若干倍：

# In[13]:


# TODO r1 <---> r2
# 直接修改参数矩阵，无返回值
def swapRows(M, r1, r2):
    if r1 == r2:
        return
    
    M[r1], M[r2] = M[r2], M[r1]


# In[14]:


# 运行以下代码测试你的 swapRows 函数
get_ipython().magic(u'run -i -e test.py LinearRegressionTestCase.test_swapRows')


# In[15]:


# TODO r1 <--- r1 * scale
# scale为0是非法输入，要求 raise ValueError
# 直接修改参数矩阵，无返回值
def scaleRow(M, r, scale):
    
    if scale == 0:
        raise ValueError
        
    M[r] = [value*scale for value in M[r]]


# In[16]:


# 运行以下代码测试你的 scaleRow 函数
get_ipython().magic(u'run -i -e test.py LinearRegressionTestCase.test_scaleRow')


# In[17]:


# TODO r1 <--- r1 + r2*scale
# 直接修改参数矩阵，无返回值
def addScaledRow(M, r1, r2, scale):
    
    M[r1] = [a+b*scale for a,b in zip(M[r1], M[r2])]


# In[18]:


# 运行以下代码测试你的 addScaledRow 函数
get_ipython().magic(u'run -i -e test.py LinearRegressionTestCase.test_addScaledRow')


# ## 2.3  Gaussian Jordan 消元法求解 Ax = b

# ### 2.3.1 算法
# 
# 步骤1 检查A，b是否行数相同
# 
# 步骤2 构造增广矩阵Ab
# 
# 步骤3 逐列转换Ab为化简行阶梯形矩阵 [中文维基链接](https://zh.wikipedia.org/wiki/%E9%98%B6%E6%A2%AF%E5%BD%A2%E7%9F%A9%E9%98%B5#.E5.8C.96.E7.AE.80.E5.90.8E.E7.9A.84-.7Bzh-hans:.E8.A1.8C.3B_zh-hant:.E5.88.97.3B.7D-.E9.98.B6.E6.A2.AF.E5.BD.A2.E7.9F.A9.E9.98.B5)
#     
#     对于Ab的每一列（最后一列除外）
#         当前列为列c
#         寻找列c中 对角线以及对角线以下所有元素（行 c~N）的绝对值的最大值
#         如果绝对值最大值为0
#             那么A为奇异矩阵，返回None (你可以在选做问题2.4中证明为什么这里A一定是奇异矩阵)
#         否则
#             使用第一个行变换，将绝对值最大值所在行交换到对角线元素所在行（行c） 
#             使用第二个行变换，将列c的对角线元素缩放为1
#             多次使用第三个行变换，将列c的其他元素消为0
#             
# 步骤4 返回Ab的最后一列
# 
# **注：** 我们并没有按照常规方法先把矩阵转化为行阶梯形矩阵，再转换为化简行阶梯形矩阵，而是一步到位。如果你熟悉常规方法的话，可以思考一下两者的等价性。

# ### 2.3.2 算法推演
# 
# 为了充分了解Gaussian Jordan消元法的计算流程，请根据Gaussian Jordan消元法，分别手动推演矩阵A为***可逆矩阵***，矩阵A为***奇异矩阵***两种情况。

# In[19]:


# 不要修改这里！
from helper import *

A = generateMatrix(4,seed,singular=False)
b = np.ones(shape=(4,1)) # it doesn't matter
Ab = augmentMatrix(A.tolist(),b.tolist()) # please make sure you already correct implement augmentMatrix
printInMatrixFormat(Ab,padding=4,truncating=0)


# 请按照算法的步骤3，逐步推演***可逆矩阵***的变换。
# 
# 在下面列出每一次循环体执行之后的增广矩阵。
# 
# 要求：
# 1. 做分数运算
# 2. 使用`\frac{n}{m}`来渲染分数，如下：
#  - $\frac{n}{m}$
#  - $-\frac{a}{b}$
# 
# 增广矩阵
# $ Ab = \begin{bmatrix}
#     7 & 5 & 3 & -5 & 1\\
#     -4 & 6 & 2 & -2 & 1\\
#     -9 & 4 & -5 & 9 & 1\\
#     -9 & -10 & 5 & -4 & 1\end{bmatrix}$
#     
# $ --> \begin{bmatrix}
#     1 & -\frac{4}{9} & \frac{5}{9} & -1 & -\frac{1}{9}\\
#     0 & \frac{38}{9} & \frac{38}{9} & -6 & \frac{5}{9}\\
#     0 & \frac{73}{9} & -\frac{8}{9} & 2 & \frac{16}{9}\\
#     0 & -14 & 10 & -13 & 0\end{bmatrix}$
#     
# $ --> \begin{bmatrix}
#     1 & 0 & \frac{5}{21} & -\frac{37}{63} & -\frac{1}{9}\\
#     0 & 1 & -\frac{5}{7} & \frac{13}{14} & 0\\
#     0 & 0 & \frac{103}{21} & -\frac{697}{126} & \frac{16}{9}\\
#     0 & 0 & \frac{152}{21} & -\frac{625}{63} & \frac{5}{9}\end{bmatrix}$
#     
# $ --> \begin{bmatrix}
#     1 & 0 & 0 & -\frac{119}{456} & -\frac{59}{456}\\
#     0 & 1 & 0 & -\frac{23}{456} & \frac{25}{456}\\
#     0 & 0 & 1 & -\frac{625}{456} & \frac{35}{456}\\
#     0 & 0 & 0 & \frac{181}{152} & \frac{213}{152}\end{bmatrix}$
#     
# $ --> \begin{bmatrix}
#     1 & 0 & 0 & 0 & \frac{193}{1086}\\
#     0 & 1 & 0 & 0 & -\frac{62}{543}\\
#     0 & 0 & 1 & 0 & \frac{1835}{1086}\\
#     0 & 0 & 0 & 1 & \frac{213}{181}\end{bmatrix}$

# In[20]:


# 不要修改这里！
A = generateMatrix(4,seed,singular=True)
b = np.ones(shape=(4,1)) # it doesn't matter
Ab = augmentMatrix(A.tolist(),b.tolist()) # please make sure you already correct implement augmentMatrix
printInMatrixFormat(Ab,padding=4,truncating=0)


# 请按照算法的步骤3，逐步推演***奇异矩阵***的变换。
# 
# 在下面列出每一次循环体执行之后的增广矩阵。
# 
# 要求：
# 1. 做分数运算
# 2. 使用`\frac{n}{m}`来渲染分数，如下：
#  - $\frac{n}{m}$
#  - $-\frac{a}{b}$
# 
# 增广矩阵
# $ Ab = \begin{bmatrix}
#     -7 & -3 & 1 & -9 & 1\\
#     0 & 0 & 0 & 0 & 1\\
#     -2 & 7 & 7 & -3 & 1\\
#     8 & -5 & -6 & 3 & 1\end{bmatrix}$
# 
# $ --> \begin{bmatrix}
#     1 & -\frac{5}{8} & -\frac{3}{4} & \frac{3}{8} & \frac{1}{8}\\
#     0 & 0 & 0 & 0 & 1\\
#     0 & \frac{23}{4} & \frac{11}{2} & -\frac{9}{4} & \frac{5}{4}\\
#     0 & -\frac{59}{8} & -\frac{17}{4} & -\frac{51}{8} & \frac{15}{8}\end{bmatrix}$
#     
# $ --> \begin{bmatrix}
#     1 & 0 & -\frac{23}{59} & \frac{54}{59} & -\frac{2}{59}\\
#     0 & 1 & \frac{34}{59} & \frac{51}{59} & -\frac{15}{59}\\
#     0 & 0 & \frac{129}{59} & -\frac{426}{59} & \frac{160}{59}\\
#     0 & 0 & 0 & 0 & 1\end{bmatrix}$
#     
# $ --> \begin{bmatrix}
#     1 & 0 & 0 & -\frac{16}{43} & \frac{58}{129}\\
#     0 & 1 & 0 & \frac{119}{43} & -\frac{125}{129}\\
#     0 & 0 & 1 & -\frac{426}{59} & \frac{160}{129}\\
#     0 & 0 & 0 & 0 & 0\end{bmatrix}$

# ### 2.3.3 实现 Gaussian Jordan 消元法

# In[21]:


# TODO 实现 Gaussain Jordan 方法求解 Ax = b

""" Gaussian Jordan 方法求解 Ax = b.
    参数
        A: 方阵 
        b: 列向量
        decPts: 四舍五入位数，默认为4
        epsilon: 判读是否为0的阈值，默认 1.0e-16
        
    返回列向量 x 使得 Ax = b 
    返回None，如果 A，b 高度不同
    返回None，如果 A 为奇异矩阵
"""

def gj_Solve(A, b, decPts=4, epsilon = 1.0e-16):
    #1.检查A，b是否行数相同
    if len(A) != len(b):
        raise None
    
    #2.构造增广矩阵Ab
    Matrix = augmentMatrix(A, b)
    row, col = shape(A)

    #3.转化为最简形
    #3.1 按照方阵行遍历
    for r in range(row):
        #3.1 找到列c中 对角线及对角线以下所有元素的绝对值的最大值
        m_col = [b[r] for b in Matrix]
        m_col_abs = [abs(b[r]) for b in Matrix]
        max_value = max(m_col_abs[r:])
        max_index = m_col_abs[r:].index(max_value)+r
        scale = m_col[max_index]

        #3.2 如果最大值为0，则为奇异矩阵，返回None
        if max_value <= epsilon:
            return None
        #3.2 否则
        #3.2.1 使用第一个行变换，将绝对值最大值所在行交换到对角线元素所在行
        swapRows(Matrix, max_index, r)
        #3.2.2 使用第二个行变换，将列c的对角线元素缩放为1
        scaleRow(Matrix, r, 1./scale)

        #3.2.3 将列c的其他元素消为0
        #[addScaledRow(Matrix, r1, r, -Matrix[r1][r]) for r1 in range(row) if r != r1]
        
        for r1 in range(row):
            if r != r1:
                addScaledRow(Matrix, r1, r, -Matrix[r1][r])
   
    matxRound(Matrix, decPts)

    return [[b[col]] for b in Matrix]


# In[22]:


# 运行以下代码测试你的 gj_Solve 函数
get_ipython().magic(u'run -i -e test.py LinearRegressionTestCase.test_gj_Solve')


# ## (选做) 2.4 算法正确判断了奇异矩阵：
# 
# 在算法的步骤3 中，如果发现某一列对角线和对角线以下所有元素都为0，那么则断定这个矩阵为奇异矩阵。
# 
# 我们用正式的语言描述这个命题，并证明为真。
# 
# 证明下面的命题：
# 
# **如果方阵 A 可以被分为4个部分: ** 
# 
# $ A = \begin{bmatrix}
#     I    & X \\
#     Z    & Y \\
# \end{bmatrix} , \text{其中 I 为单位矩阵，Z 为全0矩阵，Y 的第一列全0}$，
# 
# **那么A为奇异矩阵。**
# 
# 提示：从多种角度都可以完成证明
# - 考虑矩阵 Y 和 矩阵 A 的秩
# - 考虑矩阵 Y 和 矩阵 A 的行列式
# - 考虑矩阵 A 的某一列是其他列的线性组合

# 证明：若A为非奇异的，则另$B=A^{-1}$，且B采用与A相同的方法分块，因为
# 
# $BA=I=AB$
# 
# 则可得
# $\begin{bmatrix}
# B_{11} & B_{12}\\
# B_{21} & B_{22}
# \end{bmatrix}
# \begin{bmatrix}
# I & X \\
# Z & Y
# \end{bmatrix}
# =
# \begin{bmatrix}
# I_k & Z \\
# Z & I_{n-k}
# \end{bmatrix}
# =
# \begin{bmatrix}
# I & X \\
# Z & Y
# \end{bmatrix}
# \begin{bmatrix}
# B_{11} & B_{12}\\
# B_{21} & B_{22}
# \end{bmatrix}
# $
# 
# $
# =>
# \begin{bmatrix}
# B_{11}I+B_{12}Z & B_{11}X+B_{12}Y\\
# B_{21}I+B_{22}Z & B_{21}X+B_{22}Y
# \end{bmatrix}
# =
# \begin{bmatrix}
# I_k & Z \\
# Z & I_{n-k}
# \end{bmatrix}
# =
# \begin{bmatrix}
# IB_{11}+XB_{21} & IB_{12}+XB_{22}\\
# ZB_{11}+YB_{21} & ZB_{12}+YB_{22}
# \end{bmatrix}
# $
# 
# $
# =>
# \begin{bmatrix}
# B_{11} & B_{11}X+B_{12}Y\\
# B_{21} & B_{21}X+B_{22}Y
# \end{bmatrix}
# =
# \begin{bmatrix}
# I_k & Z \\
# Z & I_{n-k}
# \end{bmatrix}
# =
# \begin{bmatrix}
# B_{11}+XB_{21} & B_{12}+XB_{22} \\
# YB_{21} & YB_{22}
# \end{bmatrix}
# $
# 
# 因此
# 
# $
# B_{11} = I_k = B_{11}+XB_{21}=>B_{11}=I_k, B_{21}=Z\\
# B_{21}X+B_{22}Y = I_{n-k} = YB_{22}=>YB_{22} = I_{n-k}
# $
# 
# 要使等式成立，则必须满足Y为非奇异矩阵
# 
# 然而由已知条件可知，Y的第一列为全0
# 
# $det(Y)=y_{11}Y_{11}+y_{12}Y_{12}+...+y_{1n}Y_{1n}=0$，Y为奇异矩阵，
# 
# 即Y没有逆，无法使$YB_{22}=I_{n-k}$成立
# 
# 因此以上假设不成立，则A为奇异矩阵
# 

# # 3  线性回归

# ## 3.1 随机生成样本点

# In[23]:


# 不要修改这里！
# 运行一次就够了！
from helper import *
from matplotlib import pyplot as plt
get_ipython().magic(u'matplotlib inline')

X,Y = generatePoints(seed,num=100)

## 可视化
plt.xlim((-5,5))
plt.xlabel('x',fontsize=18)
plt.ylabel('y',fontsize=18)
plt.scatter(X,Y,c='b')
plt.show()


# ## 3.2 拟合一条直线
# 
# ### 3.2.1 猜测一条直线

# In[24]:


#TODO 请选择最适合的直线 y = mx + b
m = 3.22
b = 7.24

# 不要修改这里！
plt.xlim((-5,5))
x_vals = plt.axes().get_xlim()
y_vals = [m*x+b for x in x_vals]
plt.plot(x_vals, y_vals, '-', color='r')

plt.xlabel('x',fontsize=18)
plt.ylabel('y',fontsize=18)
plt.scatter(X,Y,c='b')

plt.show()


# ### 3.2.2 计算平均平方误差 (MSE)

# 我们要编程计算所选直线的平均平方误差(MSE), 即数据集中每个点到直线的Y方向距离的平方的平均数，表达式如下：
# $$
# MSE = \frac{1}{n}\sum_{i=1}^{n}{(y_i - mx_i - b)^2}
# $$

# In[25]:


# TODO 实现以下函数并输出所选直线的MSE

def calculateMSE(X,Y,m,b):
    n = len(X)
    result = sum([(y - m*x - b)**2 for x, y in zip(X, Y)])/n
    return result

print(calculateMSE(X,Y,m,b))


# ### 3.2.3 调整参数 $m, b$ 来获得最小的平方平均误差
# 
# 你可以调整3.2.1中的参数 $m,b$ 让蓝点均匀覆盖在红线周围，然后微调 $m, b$ 让MSE最小。

# ## 3.3 (选做) 找到参数 $m, b$ 使得平方平均误差最小
# 
# **这一部分需要简单的微积分知识(  $ (x^2)' = 2x $ )。因为这是一个线性代数项目，所以设为选做。**
# 
# 刚刚我们手动调节参数，尝试找到最小的平方平均误差。下面我们要精确得求解 $m, b$ 使得平方平均误差最小。
# 
# 定义目标函数 $E$ 为
# $$
# E = \frac{1}{2}\sum_{i=1}^{n}{(y_i - mx_i - b)^2}
# $$
# 
# 因为 $E = \frac{n}{2}MSE$, 所以 $E$ 取到最小值时，$MSE$ 也取到最小值。要找到 $E$ 的最小值，即要找到 $m, b$ 使得 $E$ 相对于 $m$, $E$ 相对于 $b$ 的偏导数等于0. 
# 
# 因此我们要解下面的方程组。
# 
# $$
# \begin{cases}
# \displaystyle
# \frac{\partial E}{\partial m} =0 \\
# \\
# \displaystyle
# \frac{\partial E}{\partial b} =0 \\
# \end{cases}
# $$
# 
# ### 3.3.1 计算目标函数相对于参数的导数
# 首先我们计算两个式子左边的值
# 
# 证明/计算：
# $$
# \frac{\partial E}{\partial m} = \sum_{i=1}^{n}{-x_i(y_i - mx_i - b)}
# $$
# 
# $$
# \frac{\partial E}{\partial b} = \sum_{i=1}^{n}{-(y_i - mx_i - b)}
# $$

# TODO 证明:

# ### 3.3.2 实例推演
# 
# 现在我们有了一个二元二次方程组
# 
# $$
# \begin{cases}
# \displaystyle
# \sum_{i=1}^{n}{-x_i(y_i - mx_i - b)} =0 \\
# \\
# \displaystyle
# \sum_{i=1}^{n}{-(y_i - mx_i - b)} =0 \\
# \end{cases}
# $$
# 
# 为了加强理解，我们用一个实际例子演练。
# 
# 我们要用三个点 $(1,1), (2,2), (3,2)$ 来拟合一条直线 y = m*x + b, 请写出
# 
# - 目标函数 $E$, 
# - 二元二次方程组，
# - 并求解最优参数 $m, b$

# TODO 写出目标函数，方程组和最优参数

# ### 3.3.3 将方程组写成矩阵形式
# 
# 我们的二元二次方程组可以用更简洁的矩阵形式表达，将方程组写成矩阵形式更有利于我们使用 Gaussian Jordan 消元法求解。
# 
# 请证明 
# $$
# \begin{bmatrix}
#     \frac{\partial E}{\partial m} \\
#     \frac{\partial E}{\partial b} 
# \end{bmatrix} = X^TXh - X^TY
# $$
# 
# 其中向量 $Y$, 矩阵 $X$ 和 向量 $h$ 分别为 :
# $$
# Y =  \begin{bmatrix}
#     y_1 \\
#     y_2 \\
#     ... \\
#     y_n
# \end{bmatrix}
# ,
# X =  \begin{bmatrix}
#     x_1 & 1 \\
#     x_2 & 1\\
#     ... & ...\\
#     x_n & 1 \\
# \end{bmatrix},
# h =  \begin{bmatrix}
#     m \\
#     b \\
# \end{bmatrix}
# $$

# TODO 证明:

# 至此我们知道，通过求解方程 $X^TXh = X^TY$ 来找到最优参数。这个方程十分重要，他有一个名字叫做 **Normal Equation**，也有直观的几何意义。你可以在 [子空间投影](http://open.163.com/movie/2010/11/J/U/M6V0BQC4M_M6V2AJLJU.html) 和 [投影矩阵与最小二乘](http://open.163.com/movie/2010/11/P/U/M6V0BQC4M_M6V2AOJPU.html) 看到更多关于这个方程的内容。

# ### 3.4 求解 $X^TXh = X^TY$ 
# 
# 在3.3 中，我们知道线性回归问题等价于求解 $X^TXh = X^TY$ (如果你选择不做3.3，就勇敢的相信吧，哈哈)

# In[26]:


# TODO 实现线性回归
'''
参数：X, Y
返回：m，b
'''
def linearRegression(X, Y):
    x = [[x, 1] for x in X]
    y = [[y] for y in Y]
    x_t = transpose(x)
    x_t_y = matxMultiply(x_t, y)
    x_t_x = matxMultiply(x_t, x)
    h = gj_Solve(x_t_x, x_t_y)
    
    return h[0][0], h[1][0]

m,b = linearRegression(X,Y)
print(m,b)


# 你求得的回归结果是什么？
# 请使用运行以下代码将它画出来。

# In[27]:


# 请不要修改下面的代码
x1,x2 = -5,5
y1,y2 = x1*m+b, x2*m+b

plt.xlim((-5,5))
plt.xlabel('x',fontsize=18)
plt.ylabel('y',fontsize=18)
plt.scatter(X,Y,c='b')
plt.plot((x1,x2),(y1,y2),'r')
plt.text(1,2,'y = {m}x + {b}'.format(m=m,b=b))
plt.show()


# 你求得的回归结果对当前数据集的MSE是多少？

# In[28]:


calculateMSE(X, Y, m, b)


# In[ ]:




