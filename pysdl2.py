import os
import sys

dllpath = os.path.join('./libSDL/')
print(dllpath)
os.environ["PYSDL2_DLL_PATH"] = dllpath


import sdl2,sdl2.ext
print(sdl2.SDL_GetRevision())

def run():
	sdl2.ext.init()
	winflag = (sdl2.SDL_WINDOW_ALLOW_HIGHDPI)
	window = sdl2.ext.Window("The Pong Game", size=(800, 600) ,flags=winflag)
	window.show()

	renderer = sdl2.ext.Renderer(window)

	video_file = "./src/2233.mp4"  
	renderer.
	video_texture = renderer.create_texture_from_file(video_file)

	running = True
	while running:
		events = sdl2.ext.get_events()
		##print(events)
		for event in events:
			if event.type == sdl2.SDL_QUIT:
				running = False
				break

		window.refresh()
	return 0

if __name__ == "__main__":
	sys.exit(run())