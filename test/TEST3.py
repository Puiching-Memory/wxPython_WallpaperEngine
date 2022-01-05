import ctypes

lib = ctypes.cdll.LoadLibrary('lib264/openh264-2.3.1-win64.dll')

re = lib.WelsCreateDecoder()

print(re)
