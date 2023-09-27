import pyclibrary
import ctypes

parser = pyclibrary.CParser([r"C:\Users\11386\Desktop\wxPython_WallpaperEngine\libdav1d\dav1d.h",
                             r'C:\Users\11386\Desktop\wxPython_WallpaperEngine\libdav1d\headers.h',
                             r'C:\Users\11386\Desktop\wxPython_WallpaperEngine\libdav1d\picture.h',
                             r'C:\Users\11386\Desktop\wxPython_WallpaperEngine\libdav1d\data.h',
                             r'C:\Users\11386\Desktop\wxPython_WallpaperEngine\libdav1d\common.h'
							 ])

clib = pyclibrary.CLibrary(
	r"C:\Users\11386\Desktop\wxPython_WallpaperEngine\libdav1d\libdav1d.dll",
	parser,
	prefix="Lib_",
	lock_calls=False,
	convention="cdll",
	backend="ctypes",
)

re = clib.dav1d_version()()
print('libdav1d.dll-version:',int(re,16))

settings = ctypes.c_char_p()
re = clib.dav1d_default_settings(settings)()