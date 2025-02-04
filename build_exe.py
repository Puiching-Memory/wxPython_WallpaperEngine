import os

if __name__ == "__main__":
    command = "nuitka ./Manager.py --msvc=latest --mode=standalone"
    print(f"running command: {command}")
    os.system(command)
