def resolutionSelector(resolution, streams):

    if resolution == "1080":
        print(resolution + " selector")
        for x in streams:
            print(x)
            if "video/mp4" in x:
                if "res=1080p" in x:
                    return x

    if resolution == "720":
        print(resolution)
        for x in streams:
            print(x)
            #if "video/mp4" in streams[x]:
            #    if "res=720p" in streams[x]:
            #        return streams[x]

    if resolution == "480":
        print(resolution)
        for x in streams:
            print(x)
            #if "video/mp4" in streams[x]:
            #    if "res=480p" in streams[x]:
            #        return streams[x]

    if resolution == "360":
        print(resolution)
        for x in streams:
            print(x)
            if "video/mp4" in streams[x]:
                if "res=360" in streams[x]:
                    return streams[x]
