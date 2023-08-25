import ctypes

cdll = ctypes.CDLL(
    r"C:\Users\11386\Desktop\wxPython_WallpaperEngine\lib264\openh264-2.3.1-win64.dll"
)

# 编码器对象
pSvcDecoder = None
# 输入：编码后的位流开始位置，应该包含开始码前缀
pBuf = ...
# 输入：编码后的位流长度，应该包含开始码前缀的大小
iSize = ...
# 输出：用于解码的Y,U,V缓冲区，范围为[0~2]
pData = [None] * 3
# in-out:仅用于解码:声明并初始化输出缓冲区信息，这绝不应该与仅解析共存
##sDstBufInfo = SBufferInfo()
##memset(&sDstBufInfo, 0, sizeof(SBufferInfo))
# in-out:仅用于解析:声明并初始化仅用于解析的输出位流缓冲区信息，这绝不应该与仅解码共存
##sDstParseInfo = SParserBsInfo()
##memset(&sDstParseInfo, 0, sizeof(SParserBsInfo))
##sDstParseInfo.pDstBuff = new unsigned char[PARSE_SIZE]
# 仅在解析时，分配足够的缓冲区来保存一个帧的转码比特流

err = cdll.CreateDecoder()
print(err)