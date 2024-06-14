import ctypes

libde265 = ctypes.CDLL(r'./libde265.dll')
print(libde265)

VERSION = str(libde265.de265_get_version_number_major())+'.'+str(libde265.de265_get_version_number_minor())+'.'+str(libde265.de265_get_version_number_maintenance())

print('libde265:',VERSION)


class de265_image(ctypes.Structure):  
    _fields_ = [("width", ctypes.c_int),  # 假设结构体内有一个表示宽度的成员  
                ("height", ctypes.c_int),  # 和一个表示高度的成员  
                # ... 其他可能的成员  
                ]  
    
libde265.de265_new_decoder.restype = ctypes.POINTER(ctypes.c_void_p)  
libde265.de265_new_decoder.argtypes = None
libde265.de265_push_data.restype = ctypes.c_int
#libde265.de265_push_data.argtypes = [ctypes.POINTER(ctypes.c_void_p),ctypes.POINTER(ctypes.c_void_p)]
libde265.de265_decode.restype = ctypes.c_int
libde265.de265_decode.argtypes = [ctypes.POINTER(ctypes.c_void_p),ctypes.POINTER(ctypes.c_int)]  
libde265.de265_get_next_picture.restype = ctypes.POINTER(de265_image)
libde265.de265_get_next_picture.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
libde265.de265_get_image_width.restype = ctypes.c_int
libde265.de265_get_image_width.argtypes = [ctypes.POINTER(de265_image),ctypes.c_int]


de265_decoder_context = libde265.de265_new_decoder()

de265_error = libde265.de265_start_worker_threads(de265_decoder_context, 1)


with open(r'2233.mp4','rb') as file:
    data = bytes(file.read())
    print(len(data))

more = ctypes.c_int()
for i in range(0,len(data),102400):
    #print(len(data[i:i+102400]))
    data_clip = data[i:i+102400]
    data_buffer = ctypes.byref(ctypes.create_string_buffer(data_clip))

    de265_error = libde265.de265_push_data(de265_decoder_context, data_buffer, len(data_clip),0, None)
    #print(de265_error)
    de265_error = libde265.de265_decode(de265_decoder_context, ctypes.byref(more))
    print(de265_error,more.value)

    if de265_error != 13:
        image_ptr = libde265.de265_get_next_picture(de265_decoder_context)
        #image = ctypes.cast(image_ptr,ctypes.POINTER(de265_image)).contents
        #width = libde265.de265_get_image_width(image_ptr,0)
        #print(width)
        #print(de265_image.width)
        pass