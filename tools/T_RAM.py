import psutil


def Get_RAM():
    # 获取当前Python进程的内存占用情况
    process = psutil.Process()
    memory_info = process.memory_info()

    # 内存占用以字节为单位
    print("内存占用：", memory_info.rss, "字节")
    print("内存占用：", memory_info.rss / 1024, "KB")
    print("内存占用：", memory_info.rss / (1024 * 1024), "MB")

