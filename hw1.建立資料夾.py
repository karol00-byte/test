import os
def mkdir(path):
    #判斷目錄是否存在
    folder =os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print("----建立成功----")
    else:
        # 如果目錄存在，則不建立．
        print(path + "目錄已存在")

path ="../hw1.test"
mkdir(path)