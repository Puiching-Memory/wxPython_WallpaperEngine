# import the necessary packages
from deffcode import FFdecoder
import cv2

ffparams = {
    "-vcodec": None,
    "-enforce_cv_patch": True,
    "-ffprefixes": [
        "-vsync",
        "0",
        "-hwaccel",
        "cuda",
        "-hwaccel_output_format",
        "cuda",
    ],
    "-custom_resolution": "null",
    "-framerate": "null",
    "-vf": "scale_cuda=640:360,"
    + "fps=60.0,"
    + "hwdownload,"
    + "format=nv12",
}

# initialize and formulate the decoder
decoder = FFdecoder(
    f"C:\workspace\github\wxPython_WallpaperEngine\src\H265.mp4",
    custom_ffmpeg=r"C:\workspace\github\wxPython_WallpaperEngine\ffmpeg7.1\bin",
    frame_format="null",
    verbose=True,
    **ffparams,
).formulate()

# grab RGB24(default) frame from decoder
for frame in decoder.generateFrame():

    # check if frame is None
    if frame is None:
        break

    # {do something with the frame here}
    frame = cv2.cvtColor(frame, cv2.COLOR_YUV2BGR_NV12)

    # lets print its shape
    #print(frame.shape)  # for e.g. (1080, 1920, 3)

    # Show output window
    cv2.imshow("Output", frame)

    # check for 'q' key if pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# close output window
cv2.destroyAllWindows()

# terminate the decoder
decoder.terminate()
