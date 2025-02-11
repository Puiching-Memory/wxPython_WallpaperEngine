import cv2

# 创建一个 VideoReader 对象，指定输入视频文件路径
cap = cv2.cudacodec.createVideoReader(r"C:\workspace\github\wxPython_WallpaperEngine\src\H265.mp4")

while True:
    # 读取下一帧
    ret, frame = cap.nextFrame()
    if not ret:
        break  # 如果没有更多帧，则退出循环

    # 将 GPU 上的图像转换为 BGR 格式
    bgr_frame = cv2.cuda.cvtColor(frame, cv2.COLOR_YUV2BGR_NV12)  # 注意：具体的颜色空间转换可能根据视频编码格式有所不同

    # 将图像从 GPU 下载到主机内存
    host_frame = bgr_frame.download()

    # 显示解码后的帧
    cv2.imshow('Decoded Frame', host_frame)

    # 按下 'Esc' 键退出循环
    if cv2.waitKey(30) & 0xFF == 27:
        break

# 清理资源
cap.release()
cv2.destroyAllWindows()