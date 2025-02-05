import PyNvVideoCodec as nvc

demuxer = nvc.CreateDemuxer(
          filename=r"src\H265.mp4")

decoder = nvc.CreateDecoder(
    gpuid=0,
    codec=nvc.cudaVideoCodec.HEVC,
    cudacontext=0,
    cudastream=0,
    usedevicememory=True,
    enableasyncallocations=False,
)

for packet in demuxer:
    print(packet)
    for decoded_frame in decoder.Decode(packet):
        print(decoded_frame)
        #print(type(decoded_frame))
        #print(dir(decoded_frame))
        #print(decoded_frame.nvcv_image)
        
    # break