import pyclibrary
import ctypes
import time

from pyclibrary import CParser

parser = CParser([r"C:\Users\11386\Desktop\wxPython_WallpaperEngine\lib265\de265.h"])

from pyclibrary import CLibrary

clib = CLibrary(
	r"C:\Users\11386\Desktop\wxPython_WallpaperEngine\lib265\libde265.dll",
	parser,
	prefix="Lib_",
	lock_calls=False,
	convention="cdll",
	backend="ctypes",
)

DE265_ERROR_CODED_PARAMETER_OUT_OF_RANGE = 8
DE265_ERROR_WAITING_FOR_INPUT_DATA = 13
DE265_OK = 0

de265_decoder_context = clib.de265_new_decoder()()

err = clib.de265_start_worker_threads(de265_decoder_context,1)()


with open(r"C:\Users\11386\Desktop\wxPython_WallpaperEngine\src\H265.mp4",'rb') as data:

	more = ctypes.c_long(1)
	while more.value == 1:
		break
		err = clib.de265_decode(de265_decoder_context, more)()

		if err == DE265_ERROR_WAITING_FOR_INPUT_DATA:
			decode = data.read(10000)
			lenth = len(decode) #10000
			data.seek(10000,1)
			err = clib.de265_push_data(de265_decoder_context,decode,lenth,0)()
		elif err == 0:
			img = clib.de265_get_next_picture(de265_decoder_context)()
		else:
			print(err)

	err = clib.de265_flush_data(de265_decoder_context)()
	print(err)


with open(r"C:\Users\11386\Desktop\wxPython_WallpaperEngine\src\H265.mp4",'rb') as data:

	more = ctypes.c_long(1)
	decode = data.read()
	lenth = len(decode)
	err = clib.de265_push_data(de265_decoder_context,decode,lenth,0)()
	err = clib.de265_decode(de265_decoder_context, more)()
	
	img = clib.de265_get_next_picture(de265_decoder_context)()
	pic = clib.de265_get_image_width(img,1)()


	##err = clib.de265_flush_data(de265_decoder_context)()
	print(err)
	
	##err = clib.de265_release_next_picture(img)()
	##err = clib.de265_get_image_width(img,0)()

