# wxPython_WallpaperEngine

Desktop wallpaper engine based on wxPython Library

基于wxpython库实现的桌面壁纸引擎

# 技术细节

wxpython有自带的视频播放器控件，但是它每次播放完视频后会自动黑屏。为了实现无缝循环播放，我基于wx.DC尝试构建自定义的视频播放器。由于算法的更改，以前实现的功能暂时不可用。

# 环境要求

windows10

windows8/7(理论上)

# 功能计划 || Plan 2022/05/11

* [X] 控制面版
* [ ] 播放音频
* [X] 播放速率调节
* [X] 自定义播放路径
* [X] 支持.mov文件
* [ ] 支持html文件
* [ ] 切片缓存再利用
* [X] 无缝循环播放
* [ ] 列表式播放
* [ ] 拖放式加载

# 所需库

wxpython

pywin32api

pyopencv2

# 版权

所有者:@PUICHING_Memory

协议：GPLV3
