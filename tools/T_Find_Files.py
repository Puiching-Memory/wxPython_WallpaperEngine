"""
寻找一个文件夹下指定类型的所有文件
返回文件路径列表

exp:
>>Find_Files('./','.py')
['test.py','test2.py','test3.py']
"""


import os
import glob


def Find_Files(path:str, type:str):

    folder_path = path  # 替换为你的文件夹路径

    # 使用glob模块获取文件夹下所有.h文件的路径
    file_paths = glob.glob(os.path.join(folder_path, "*." + type))

    return file_paths
