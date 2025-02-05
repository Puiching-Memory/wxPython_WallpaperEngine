# wxPython_WallpaperEngine

[English]  Dynamic desktop wallpaper engine based on wxPython

[中文] 基于wxpython实现的动态桌面壁纸引擎

# 技术细节

wxpython有自带的视频播放器控件，但是它每次播放完视频后会自动黑屏。为了实现无缝循环播放，我基于wx.DC尝试构建自定义的视频播放器。由于算法的更改，以前实现的功能暂时不可用。

瓶颈：软件解算(CPU)在高分辨率(>2K)及高刷新率(>60HZ)的任务下性能表现糟糕

# 结构

Manager.py(管理，时钟刻，设置，数据传输) --> **Engine.py(解码器) & **Player.py(播放器)

# 环境要求

windows10 or 11

```
conda create -n wxwallpaper python=3.10
pip install -r requirements.txt
```

# 路线图 || RoadMap 2025/02/05

* [ ] nvidia视频硬件解码SDK
* [ ] intel视频硬件解码SDK
* [ ] nuitka集成为setup.py
* [ ] gui的文件目录结构调整
* [ ] win32的云母现代化外观

# 致谢

所有者:@PUICHING_Memory

协议：GPLV3
