import os
from colorama import Fore, Back, Style, init, deinit

# doc:https://nuitka.net/user-documentation/user-manual.html


if __name__ == "__main__":
    init()

    EXE_NAME = "wxWallPaperEngine"

    command_list = [
        rf"nuitka ./{EXE_NAME}.py"
        + rf" --msvc=latest"
        + rf" --mode=onefile"  # --mode=standalone/onefile/app/accelerated
        + rf" -o {EXE_NAME}"
        + rf" --report=compilation-report.xml"
        + rf" --include-data-dir=./icon=./icon"
        + rf" --lto=yes",
    ]

    for index, command in enumerate(command_list):
        print(
            f"{Fore.YELLOW}Building wxPython_WallpaperEngine: running command [{index}]: {Fore.BLUE}{command}{Fore.RESET}"
        )
        os.system(command)

    deinit()
