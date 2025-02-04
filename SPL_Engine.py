"""
SPL图像解码引擎
---
### Return type: wx.Bitmap

Usage:
```
import SPL_Engine

path:str = 'any path' # Contains absolute and relative paths
frame:int = 1 # Start from 1

Var = SPL_Engine.SPL_Engine()
Var.Load(path)
if Var.IsLoaded == True:
    Var.Get(frame, x_size, y_size)
```
"""

import os
import win32gui, win32print, win32con

class SPL_Engine():
 
    def __init__(self, *karg):
        self.sx, self.sy = get_real_resolution()
        print('SPL_Engine loaded', self.sx,self.sy)

    def Load(self, path):
        if os.path.isabs(path) == True:
            pass
        else:
            pass

    def Get(self, frame=1, x_size=800, y_size=600):
        pass

    def IsLoaded(self):
        return True

    def IsRunning(self):
        return False


def get_real_resolution():
    """获取真实的分辨率"""
    hDC = win32gui.GetDC(0)
    # 横向分辨率
    w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
    # 纵向分辨率
    h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
    return w, h

if __name__ == "__main__":
    SPL_Engine()

 