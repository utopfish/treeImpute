# coding=utf-8
import pandas as pd
import numpy as np
class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.visited = False
        self.tracker = None

    def set_val(self, val):
        self.val = val

    def get_val(self):
        return self.val

    def set_left(self, left):
        self.left = left

    def get_left(self):
        return self.left

    def set_right(self, right):
        self.right = right

    def get_right(self):
        return self.right

    def is_visited(self):
        return self.visited

    def visit(self):
        self.visited = True

    def clear_visit(self):
        self.visited = False
def readDataTxt(path):
    data = pd.read_table(path, header=None, sep=" ")
    return data
class Tree:
    def __init__(self, general_lists):
        self.root = self.findMid(general_lists)

    def postorderInit(self, root, stateList):
        if (root is None):
            return
        self.postorderInit(root.left, stateList)
        self.postorderInit(root.right, stateList)
        if len(root.val) == 1:
            for i in root.val:
                try:
                    root.val = set([stateList[int(i)]])
                except:
                    # 抓住出现(1)情况错误
                    root.val = set([stateList[int(i[1:-1])]])
                break

    # 后序遍历打印
    def postorderPrint(self, root):
        if (root is None):
            return
        self.postorderPrint(root.left)
        self.postorderPrint(root.right)
        print(root.val)

    def postorderPrintTracker(self, root):
        if (root is None):
            return
        self.postorderPrintTracker(root.left)
        self.postorderPrintTracker(root.right)
        print(root.tracker)
    def postorderGetgenerList(self,root):
        if root is None:
            return
        self.postorderGetgenerList(root.left)
        self.postorderGetgenerList(root.right)
        if root.val ==None:
            root.val='({},{})'.format(root.left.val,root.right.val)
    def getBinList(self,root):
        '''
        获取二分的物种列表，在进行广义表还原之后进行
        :param root:
        :return:
        '''
        if root.val==None:
            self.postorderGetgenerList(root)
        else:
            return root.left.val.replace("(","").replace(")","").split(","),root.right.val.replace("(","").replace(")","").split(",")

    def findMid(self, general_lists):
        # 二叉分类
        mark = 0
        bigmark = 0
        mid = 0
        if general_lists[0] == "{":
            return Node(general_lists[1:-1].split(","))
        else:
            for index, i in enumerate(general_lists[1:-1]):
                if (i == "("):
                    mark += 1
                elif (i == ")"):
                    mark -= 1
                elif i == "{":
                    bigmark += 1
                elif i == "}":
                    bigmark -= 1
                elif (i == "," and mark == 0 and bigmark == 0):
                    mid = index
                    break
            if mid == 0:
                return Node(general_lists)
            else:
                root = Node(None)
                root.left = self.findMid(general_lists[1:mid + 1])
                root.right = self.findMid(general_lists[mid + 2:-1])
                return root


if __name__=="__main__":
    path = r"011号简化数据集奇虾/011号完整数据集.txt"
    data = readDataTxt(path)
    li = np.array(data)
    te = ["((0,1),(2,(3,4)))", "({0,1,2,3},4)"]
    tree = Tree(te[0])

    tree.postorderPrint(tree.root)
    tree.postorderGetgenerList(tree.root)
    print("+++++")
    print(tree.root.val)
    print(tree.getBinList(tree.root))
    # print("{}:{}".format(te[0], getFict(te[0], li)))
