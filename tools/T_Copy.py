import os
import re
import shutil

def copy_included_files(header_file, destination_folder):
    with open(header_file, 'r') as f:
        content = f.read()

    # 使用正则表达式匹配#include语句中的文件名
    pattern = r'#include\s+[<"](.+?)[>"]'
    matches = re.findall(pattern, content)

    for file_name in matches:
        included_file = None
        
        # 检查是否有尖括号包裹的头文件
        if '<' in file_name and '>' in file_name:
            # 假设这里是处理系统头文件的逻辑
            # 参照系统头文件路径查找并构建完整路径
            system_include_path = "/usr/include"
            included_file = os.path.join(system_include_path, file_name)
        else:
            # 假设这里是处理普通头文件的逻辑
            # 构建被包含文件的完整路径
            included_file = os.path.join(os.path.dirname(header_file), file_name)

        if os.path.exists(included_file):
            # 复制文件到目标文件夹
            shutil.copy(included_file, destination_folder)
        else:
            print(f"无法找到文件: {included_file}")


if __name__ == "__main__":
    # 示例用法：
    header_file = 'libwin/mfapi.h'  # 替换为要解析的.h文件的路径
    destination_folder = "test"  # 替换为指定的目标文件夹路径

    copy_included_files(header_file, destination_folder)
