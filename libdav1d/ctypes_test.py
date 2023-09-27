import ctypes

cdll = ctypes.CDLL(r'C:\Users\11386\Desktop\wxPython_WallpaperEngine\libdav1d\libdav1d.dll')

SettingC = ctypes.c_char_p()

re = cdll.dav1d_default_settings(SettingC)