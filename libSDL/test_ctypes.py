import ctypes

sdll = ctypes.CDLL(r'C:\Users\11386\Desktop\wxPython_WallpaperEngine\libSDL\SDL2.dll')

re = sdll.SDL_CreateWindow('1')

print(re)