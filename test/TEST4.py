import win32com.client

def play_video(file_path):
		player = win32com.client.Dispatch("{90377834-21D0-4DEE-8214-BA2E3E6C1127}")

		print(player)

# 调用示例
video_file = r"C:\Users\11386\Desktop\wxPython_WallpaperEngine\src\114514.mp4"
play_video(video_file)
