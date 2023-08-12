import ctypes

MFPlay = ctypes.WinDLL('MFPlay.dll')


sURL = 'test_vedio.mp4'
hwnd = 114514 #_hwnd
MFPlay.MFPCreateMediaPlayer(
    sURL,
    True,
    0,
    None,
    hwnd,
    None
    )
