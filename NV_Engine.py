import PyNvVideoCodec as nvc
import ctypes as C
import numpy as np
import pycuda.driver as cuda
import pycuda.autoinit  # this is needed for initializing CUDA driver
import colour
from matplotlib import pyplot as plt

demuxer = nvc.CreateDemuxer(filename=r"src\H265.mp4")

decoder = nvc.CreateDecoder(
    gpuid=0,
    codec=demuxer.GetNvCodecId(),
    cudacontext=0,
    cudastream=0,
    usedevicememory=True,
    # enableasyncallocations=False,
)

seq_triggered = False
for packet in demuxer:
    print(packet)
    for decoded_frame in decoder.Decode(packet):
        if not seq_triggered:
            decoded_frame_size = decoder.GetFrameSize()
            # NV12格式,前3分之二的像素是Y，后1/3是UV交错存储的
            # doc:https://blog.csdn.net/byhook/article/details/84037338
            raw_plane = np.ndarray(shape=decoded_frame_size, dtype=np.uint8)
            seq_triggered = True

        # print(dir(decoded_frame)) # 'cuda', 'dtype', 'format', 'framesize', 'nvcv_image', 'shape', 'strides', 'timestamp'
        # print(decoded_frame.shape)

        cuda.memcpy_dtoh(raw_plane, decoded_frame.GetPtrToPlane(0))

        image_shape = np.array((decoded_frame.shape[0] * 2 // 3, decoded_frame.shape[1]))
        print(image_shape)
        y_plane = np.frombuffer(
            raw_plane[0 : decoded_frame.shape[1] * (decoded_frame.shape[0] * 2 // 3)],
            dtype=np.uint8,
        ).reshape(image_shape)
        u_plane = (
            np.array(
                raw_plane[
                    decoded_frame.shape[1] * (decoded_frame.shape[0] * 2 // 3) :: 2
                ],
                dtype=np.uint8,
            )
            .reshape(image_shape//2).repeat(2, axis=0).repeat(2, axis=1)
        )
        v_plane = (
            np.array(
                raw_plane[
                    decoded_frame.shape[1] * (decoded_frame.shape[0] * 2 // 3) + 1 :: 2
                ],
                dtype=np.uint8,
            )
            .reshape(image_shape//2).repeat(2, axis=0).repeat(2, axis=1)
        )

        ouptut_image = np.dstack((y_plane, u_plane, v_plane))
        ouptut_image = colour.YCbCr_to_RGB(
            ouptut_image,
            in_bits=8,
            in_int=True,
            in_legal=True,
            out_bits=8,
            out_legal=True,
        )

        # plt.imshow(
        #     # raw_plane.reshape(decoded_frame.shape[0], decoded_frame.shape[1]),
        #     ouptut_image,
        #     cmap="gray",
        # )
        # plt.show()
