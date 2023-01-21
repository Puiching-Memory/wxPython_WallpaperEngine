
import subprocess
import os

def Update():
    # pip显示需要更新的python列表
    Lib_list = 'pip list -o' 
    # 执行命令并返回结果
    p = subprocess.Popen(Lib_list, shell=True, stdout=subprocess.PIPE)
    # 取命令返回结果，结果是一个二进制字符串，包含了我们上面执行pip list -o后展现的所有内容
    out = p.communicate()[0]
    out = str(out, 'utf-8')

    # 取出待升级的包名, 并存入列表
    need_update = []
    for i in out.splitlines()[2:]:
        need_update.append(i.split(' ')[0])

    # 执行升级命令，pip每次取一个包进行升级，
    for nu in need_update:
        com_update = 'python -m pip install --upgrade {py}'.format(py=nu)
        print("执行命令:", com_update)
        subprocess.call(com_update)
        print("---------- 执行结束-----------\n".format(com=com_update))

if __name__ == "__main__":
    print("检查更新:")
    os.system('pip list -o')
    Update()
