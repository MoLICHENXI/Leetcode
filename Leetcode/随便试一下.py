# # import torch
# # from torch.distributions import multinomial
# # from d2l import torch as d2l
# # fair_probs=torch.ones((6))/6
# # counts = multinomial.Multinomial(10, fair_probs).sample((500,))
# # cum_counts = counts.cumsum(dim=0)
# # estimates = cum_counts / cum_counts.sum(dim=1, keepdims=True)

# # d2l.set_figsize((6, 4.5))
# # for i in range(6):
# #     d2l.plt.plot(estimates[:, i].numpy(),
# #                  label=("P(die=" + str(i + 1) + ")"))
# # d2l.plt.axhline(y=0.167, color='black', linestyle='dashed')
# # d2l.plt.gca().set_xlabel('Groups of experiments')
# # d2l.plt.gca().set_ylabel('Estimated probability')
# # d2l.plt.legend()

# # M= [I speak Chinese]
# # print(len(M))
# # M=[[1,2,3],[4,5,6],[7,8,9]]
# # dict={}
# # dict = {i:sum(M[i]) for i in range(3)}
# # print(dict)

# D={}
# D["name"]="Bob"
# print(D)

'''
#zip反函数的应用
# M=['flowerl','flow111','flowers']
# N = ['str','stl','st1']
# for temp in zip(*N):
#     if len(set(temp)) == 1:
#         print("相同")
#     else:
#         print("不相同")

# def xiangtong(X):
#     for item in zip(*X):
#         if len(set(item)) == 1:
#             continue
#         return '不相同'
#     return '相同'

# M=['flowerl','flow111','flowers']
# N = ['str','stl','st1']
# print(xiangtong(N))
'''

# M = {'a':'111','c':'222','b':'333'}
# Ms = list(M.keys())
# Ms1 = sorted(Ms)
# for i in Ms1:
#     print(i,'=>',M[i])

# for key in sorted(M):
#     print(key,'=>',M[key])


# M=[[1,2,3],[4,5,6],[7,8,9]]
# N=[row[1] for row in M]
# print(N)

# L=[1,2,3]
# for i in range()


# print(list(map(lambda x : 2**x, range(7))))

#sort函数的使用

'''
MS=[2,1,4,3,7,9,6]
MS.sort()
print(MS)
'''

'''
# 二分查找

# def binary_search(list,target):
#     idx = 0
#     ends = len(list)
#     while idx < ends:
#         mid = (idx + ends)//2
#         guess = list[mid]
#         if guess == target:
#             return mid
#         elif guess > target:
#             ends = mid
#         elif guess < target:
#             idx =  mid + 1
#     return None
# my_list=[1,3,5,7]
# print(binary_search(my_list,7))


def binary_search(x,target):
    start = 0
    ends = len(x) - 1
    while start <= ends:
        mid = (start + ends)//2
        if x[mid] == target:
            return mid
        elif x[mid] < target:
            start = mid + 1
        elif x[mid] > target:
            ends = mid - 1
    return None

list=[1,2,3,4,5,6,7,8,10]
print(binary_search(list,9))
'''


# def f(a,b=3,c=15):
#     print(a,b,c)
# f(1)

# class Indexer:
#     def __getitem__(self,index):
#         return self.data[index]
# X = Indexer()
# X.data = 'spam'
# print([c for c in X])
# print(list(map(str.upper,X)))
# for item in X:
#     print(item,end=' : ')


# class multiply:
#     def __init__(self,value,stop) -> None:
#         self.start  = value - 1
#         self.ends = stop
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start == self.ends:
#             raise StopIteration
#         self.start += 1
#         return self.start**2
# X=multiply(1,6)
# # for i in X:
# #     print(i,end='\t')
# # X=multiply(1,8)
# # print(list([C for C in X]))
# I=X.__iter__()
# print(I.__next__())
# print(next(I))


# def squares(start,ends):
#     for i in range(start,ends+1):
#         yield i**2
# X=squares(1,4)
# for i in X:
#     print(i,end=' ')
# print('\n')
# for x in squares(2,9):
#     print(x,end=' ')

# L=[2,3,4,5,6]
# print(L[slice(2,None,2)])


#冒泡排序
'''
def maopao(list,reverse = True):
    if reverse ==True:
        i = 0
        while i < len(list):
            j = i + 1
            while j < len(list):
                if list[i] >= list[j]:
                    temp = list[i]
                    list[i] = list[j]
                    list[j] = temp
                j += 1
            i += 1
        return list
    i = 0
    while i < len(list):
        j = i + 1
        while j < len(list):
            if list[i] <= list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
            j += 1
        i += 1
    return list

x = [100,2,1,4,3,8,3,12,10,1,3,5]
print(maopao(x))
'''

#选择排序 找到序列中的最大值 O(n*2)
'''
def paixu(x):
    list =[]
    i = 0
    while len(x) != 0:
        temp = x[0]
        flag = 0
        while i < len(x):
            if temp < x[i]:
                temp = x[i]
                flag = i
            i += 1
        list.append(x.pop(flag))
        #x.pop(flag)
        #list.append(temp)
        i = 0
    return list

x = [2,1,4,3,7,9,8,101,1000]
print(paixu(x))
'''

#选择排序的另一种写法 用两个函数 一个函数用于找出序列中的最小值 并返回对应序列 另一个函数不断调用找到序列中的最小值
'''
def findSmaller(x):
    smallest = x[0]
    smallest_index = 0
    for i in range(1,len(x)):
        if x[i] < smallest:
            smallest = x[i]
            smallest_index = i
    return smallest_index

def paixu(x):
    list = []
    while len(x) != 0:
        list.append(x.pop(findSmaller(x)))
    return list

x = [2,1,4,3,7,9,8,101,15]
print(paixu(x))
'''

#递归尝试
'''
def countdown(i):
    print(i)
    print('调用递归，递去的过程')
    if i >= 1:
        i -= 1
        print('调用递归，看看这里')
        countdown(i)
    else:
        return
print(countdown(4))
'''

#递归求阶乘
'''
def factorial(n):
    if n != 1:
        n = n *factorial(n-1)
        return n
    else:
        return n
print(factorial(5))

最关键的在于第273行 if语句里需要一个返回值
首先fac(5) 进行到 n = n * fac(4)处挂起，以此类推 fac(4) n=4 处 进行到 n = n * fac(3); fac(3)  n=3 进行到 n = n * fac(2); fac(2) 进行到 n = n * fac(1); 而fac(1)给出了
返回值 return n，即返回值为 1，那么递归需要返回前面被挂起的线程并逐个跳出，进行到fac(2)部分 n = 2* fac(1) = 2，但是这里需要把当前的 n 返回到上一线程中，否则递归无法找到程序
退出的出口，无法完成递归的操作 
'''


#递归求序列的和
'''
def sum(x):
    total = 0
    if len(x) != 0:
        total = x.pop(0) + sum(x)
        return total
    else:
        return 0
print(sum([1,2,3,4,7,8,9]))
'''


#递归求列表个数
'''
def count(x):
    flag = 0
    if x != []:
        x.pop(0)
        flag = 1 + count(x)
        return flag
    else:
        return 0
print(count([1,2,3,4,7,8,9]))
'''


#找出序列的最大值
'''
def max(x):
    flag = 0
    for arr in x:
        if arr > flag:
            flag = arr
    return flag
print(max([1,2,3,14,7,8,9]))
'''


#快速排序
'''
def quicksort(x):
    if len(x) < 2:
        return x
    else:
        base = x[(0+len(x))//2]  #选择基准值至关重要
        less = [i for i in x if i < base]
        bigger = [i for i in x if i > base]
        return quicksort(less) + [base] + quicksort(bigger)
print(quicksort([4,2,1,3,7,9,8,101,15]))
#快速排序核心思想 就是分治法，让所处理的事情不断划分成块，并找到最后适合处理的基线问题，在快速排序中，基线问题就是序列长度为1，此时无序排序，否则一直找一个基准值进行排序
'''


#归并排序
'''

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = int (len(lst)/2)

    left = merge_sort(lst[ :middle])#左边
    right = merge_sort(lst[middle: ])#右边
    merged = []
    while left and right:
        merged.append(left.pop(0) if left [0] <= right[0] else right.pop(0))
    merged.extend(right if right else left)  #该方法没有返回值，但会在已存在的列表中添加新的列表内容
    return merged

data_lst = [6,202,100,301,38,8,1]
print(merge_sort(data_lst))
'''


#第四章练习题
'''
def multiply(list):
     x = list
     if len(x) > 1:
         flag =x.pop(0)
         return flag * multiply(list)
     else:
         return x.pop(0)

print(multiply([2,3,5,7]))
'''

#广度优先搜索
'''
from collections import deque
graph = {}
graph["person"] = ["alice","bob","tom"]
graph["bob"] = ["Jack","Peter"]
graph['alice'] = []
graph['Jack'] = []
graph['Peter'] = []

def search(graph,name):
    search_list = deque()
    search_list += graph[name]
    searched = []
    while search_list:
        target = search_list.popleft()
        if target not in searched:
            if is_name(target):
                print('%s is found' %target)
                return True
            else:
                search_list += graph[target]
                searched.append(target)
    print('None')
    return False

def is_name(name):
    return name[-1] == 'm'
search(graph,'person')
'''

#狄克斯克拉算法
'''
#创建图,存储图上信息，表示节点之间的权重值
graph ={}
#在有权重的表示一个图时，value是一个dict，用于储存配对的信息
#start的键值对，值也是一个字典
#a,b都是字典里的key,路径权重是value
graph ['start'] = {}
graph ['start'] ['a'] = 6
graph ['start'] ['b'] = 2
graph ['a'] = {}
graph ['a'] ['ends'] = 1
graph ['b'] = {}
graph ['b'] ['a'] = 3
graph ['b'] ['ends'] =5
graph ['ends'] ={}
# print(graph)

#创建储存更新权重的散列表
max = float('inf')
costs = {}
costs ['a'] = 6
costs ['b'] = 2
costs ['ends'] = max # 1、这里很重要，必须设置重点的初始化为无穷，这样能用较小值去代替
# print(costs)

#创建存储父节点信息的散列表
parent = {}
parent ['a'] = 'start'
parent ['b'] = 'start'
# print(parent)

#已处理过的节点
processed = []

#dijkstra算法
def Dijkstra(graph,costs,parent,processed):
    node = find_mincost(costs)
    while node is not None:
        cost = costs[node]  #当前node的权重值
        neighbours = graph[node]  #neighbours 是一个dict 包含了邻居节点的信息 即节点名称加路径长度
        for n in neighbours.keys():  #处理一个节点的所有邻居节点，处理完将该节点加入processed队列
            new_cost = cost + neighbours[n]   #当前节点的costs 加上到邻居节点的权重
            if new_cost < costs[n]:            #如果邻居节点的新权重小于已有的权重
                costs[n] = new_cost
                parent[n] = node
        processed.append(node)
        node = find_mincost(costs)
    return costs

def find_mincost(costs):
    low_cost_max = float('inf')
    low_cost_node = None           # 2、这是需要注意的设置初始化的最小权重点为None，这样保证最后能够退出主函数循环
    for node in costs:
        cost = costs[node]
        if  cost< low_cost_max and node not in processed:
            low_cost_node = node
            low_cost_max = cost
    return low_cost_node

print(Dijkstra(graph,costs,parent,processed))
'''


#贪婪算法
'''
state_needed = set(['mt','wa','or','id','nv','ut','ca','az'])
stations = {}
stations['kone'] = set(['id','nv','ut'])
stations['ktwo'] = set(['wa','id','mt'])
stations['kthree'] = set(['or','nv','ca'])
stations['kfour'] = set(['nv','ut'])
stations['kfive'] = set(['ca','az'])

final_station = set()
while state_needed:
    best_station = None                          #每次都找到最优的那个基站(station)，贪婪的意义所在
    states_covered = set()                       
    for station, states in stations.items():     #在所需覆盖的集合state_needed不为空时，每次循环来寻找基站(stations)所覆盖的最大数量，并在每次循环结束后将覆盖值从state_needed中删除
        covered = state_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    state_needed -= states_covered
    final_station.add(best_station)
print(final_station)
'''

#关于类的继承和初始化
'''
class FooParent(object):
    def __init__(self):                    #初始化是在对类创建实例时直接自动初始化的，即__init__(self)是类中保存的实例
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print("%s from Parent" % message)
        
class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
        super(FooChild, self).__init__()
        print('Child')

    def bar(self, message):
        super(FooChild, self).bar(message)
        print('Child bar fuction')
        print(self.parent)


if __name__ == '__main__':
    fooChild = FooChild()
    # fooChild.bar('HelloWorld')
    print(fooChild.parent)
'''

'''
class C:
    def act(self):
        self.name = 'Jack'
        print('spam')

class D(C):
    def act(self):
        super().act()
        print('eggs')


A = D()
B = C()
# print(B.act())
# print(B.name)
# print('\n')
print(A.act(),end='\n\n')
# print(A.name)
print(D.__dict__.keys())
print(C.__dict__.keys())
print(B.__dict__.keys())
print(A.__dict__.keys())
'''

'''
class A:
    def act(self):
        print('A')

class B:
    def act(self):
        print('B')

class C(A,B):
    def act(self):
        A.act(self)
        B.act(self)

X = C()
print(X.act())
'''


#递归算法中，时间复杂度最小的，因为每次把递归的部分只计算了一次，一共计算O(log n)，每次完成一次乘法运算，时间复杂度为O(1)，因此总的复杂度为O(log n)
'''
def x1(x,n):
    if n == 0:
        return 1
    # else:
    #     if n % 2 ==1:
    #         return x1(x,n//2)*x1(x,n//2)*x
    #     else:
    #         return x1(x,n//2)*x1(x,n//2)
    
    t = x1(x,n//2)
    if n%2 ==1:
        return t*t*x
    else:
        return t*t
print(x1(2,8))
'''

#两种不同的斐波那契求和方法，时间复杂度不一样
'''
def fabonacci(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fabonacci(n - 1) + fabonacci(n - 2)
print(fabonacci(6))

#下面这个方法很重要
def fabonacci2(first,second,n):
    if n <= 0:
        return 0
    elif n < 3:
        return 1
    elif n ==3:
        return first + second
    else:
        return fabonacci2(second,first+second,n-1)

print(fabonacci2(0,1,6))
# '''

# class A():
#     def __init__(self):
#         print('enter A')
#         print('leave A')
#
#
# class B(A):
#     def __init__(self):
#         print('enter B')
#         super().__init__()
#         print('leave B')
#
#
# class C(A):
#     def __init__(self):
#         print('enter C')
#         super().__init__()
#         print('leave C')
#
#
# class D(B, C):
#     def __init__(self):
#         print('enter D')
#         super().__init__()
#         print('leave D')
#
# d = D()

# class A():
#     def color(self):
#         print('colorful')
#
# class B(A):
#     pass
#
# class C(A):
#     pass
#
# B= B()
# B.color()
# print(B.__class__)


#单链表 Listnode 求取链表长度LinkedList
'''
class ListNode:
    def __init__(self,data,next = None):  #默认一个节点的next部分为None
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self,head):       #给链表设置一个头结点  头结点指向第一个节点ListNode
        self.head = head
    def __len__(self):             #求链表的长度
        curr = self.head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        return count

node1 = ListNode(1)                #给node1一个data值
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2                 #将node1的next指针指向node2
node2.next = node3
x = LinkedList(node1)
print(x.head)
print(len(x))
'''

# from collections import Counter
# c = Counter(a=4, b=2, c=0, d=-2)
# c1 = c.elements()
# print(c1.__iter__())
# print(c1.__next__())
# print(c1.__next__())
# print(c1.__next__())
# print(c1.__next__())
# print(c1.__next__())
# print(c1.__next__())


# class Solution:
#     def next_search(self,a,needle):     #构造前缀表
#         next = ['' for i in range(a)]   #创建一个空的list
#         i = 1                           #i始终指向needle的后缀部分
#         j = 0                           #j始终指向needle的前缀部分
#         next[0] = 0                     #初始化next序列中，第1个位置(index = 0)的最大相同前后缀长度为0
#         for i in range(1,len(needle)):
#             while j > 0 and needle[i] != needle[j]:   #首先，必须保证j 是大于0的，因为后面是需要用到j的前一位j-1对应的最长前后缀长度
#                 j = next[j - 1]         #如果当前位置是不相同的，根据KMP思想，就把回到前面匹配好的前缀部分，也就是回到j -1 位的next数组中记录的对应位置的最长前缀长度
#                                         #回到该位置后，以ababacab为例   i = 5 的时候对应位置为'c'，此时j = 3，对应为'b'，因为此时不相等，开始回到j = 2，也就是前一位记录的最长前后缀长度
#                                         #next[2] = 1，表示 aba中，最长的前后缀为a,所以abac当比较到'abac'的c时，可以从第一个'a'(记录的前缀)开始再次比较，发现'ab'与'ac'还是不一样，那么再往前继续回溯
#                                         #只到j=0,表示就是没有相同的前缀了，那么可以放弃此时的i 值 表示前面没有与之类似的，从i + 1继续开始重新比较
#             if needle[i] == needle[j]:  #这里已经包含了i = 1, j = 0相同的时候
#                 j += 1                  #如果当前位置的后缀和前缀是相同的，就把指向前缀的j也向后移位
#                 next[i] = j             #j在这里就正好是前面相同部分的长度  #因此在这里就把记录needle中i位置的部分填上相同的长度 (j)
#             next[i] = j                 #这里考虑的就是i=1 ,j=0且不相同的情况，例如abac串，next[1]是需要标记为0的
#         return next
#
# X=Solution()
# print(X.next_search(8,'ababacab'))

# class Solution:
#     def canJump(self, nums) -> bool:
#         '''其实就是判断接下来的nums[i] 的片断序列中的最大值能否一直累加大于等于len(nums)'''
#         def digui(numbers, start, ends):
#             #结束条件
#             if ends > len(nums):
#                 return True
#             if start + 1 == ends and numbers == 0:
#                 return False
#             #numbers始终是当前序列中的最大值
#             numbers = max(nums[start: ends])
#             start = nums.index(numbers) + 1 if numbers >= 1 else nums.index(numbers) + 0
#             ends = nums.index(numbers) + numbers + 1
#             return digui(numbers, start, ends)
#         return digui(float('-inf'), 0, 1)
# X = Solution()
# print(X.canJump([3,2,1,0,4]))

# #每日一问1
# def show(list , length):
#     print(list[length - 1], end = '')
#     show(list, length - 1)
#
# show([1,2,3,4,5], 5)

#每日一问2
l1 = [1,[2,3],4]
l2 = l1.copy()
l2[1][1] = 7
print(l1, l2)