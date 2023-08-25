import ctypes

clib = ctypes.CDLL(r'C:\Users\11386\Desktop\wxPython_WallpaperEngine\lib265\libde265.dll')

DE265_ERROR_CODED_PARAMETER_OUT_OF_RANGE = 8
DE265_ERROR_WAITING_FOR_INPUT_DATA = 13
DE265_OK = 0

de265_decoder_context = clib.de265_new_decoder()

# <----Bug here
err = clib.de265_start_worker_threads(de265_decoder_context,1)


with open(r"C:\Users\11386\Desktop\wxPython_WallpaperEngine\src\H265.mp4",'rb') as data:
    i = 0
    position = 0
    more = ctypes.c_long(1)
    while more.value == 1:
        err = clib.de265_decode(de265_decoder_context, more)

        if err == DE265_ERROR_WAITING_FOR_INPUT_DATA:
            decode = data.read(position + 10000)
            lenth = len(decode)
            err = clib.de265_push_data(de265_decoder_context,decode,lenth,0)
        elif err == 0:
            img = clib.de265_get_next_picture(de265_decoder_context)
            i += 1

    
    print(i)
    
    err = clib.de265_flush_data(de265_decoder_context)
    print(err)
    
    
err = clib.de265_free_decoder(de265_decoder_context)