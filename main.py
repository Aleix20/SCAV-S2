import os


def trim(in_file, out_file, start, end):
    if os.path.exists(out_file):
        os.remove(out_file)
    # command to trim the video in our case only working until 59 seconds
    command = 'ffmpeg -ss 00:00:' + str(start) + ' -i ' + in_file + ' -t 00:00:' + str(end) + ' -c copy ' + out_file
    print(command)
    os.system(command)


def scale(in_file, out_file, width, height):
    if os.path.exists(out_file):
        os.remove(out_file)
    # Command to scale the video
    command = 'ffmpeg -i ' + in_file + ' -vf scale=' + str(width) + ':' + str(height) + ',setsar=1:1 ' + out_file
    print(command)
    os.system(command)


def videoToYuv(in_file, out_file):
    if os.path.exists(out_file):
        os.remove(out_file)
    # Take the histogram and rescale the video.(we will have histogram+video on screen)
    command = 'ffmpeg -y -i ' + in_file + ' -filter_complex "[0:v]split=2[v0][v1];' \
                                          '[v0]histogram=display_mode=parade,scale=1280:720,setsar=1[v2];' \
                                          '[v1]scale=1280/5:720/5,setsar=1[v3];' \
                                          '[v2][v3]overlay=x=50:y=0[v]" -map [v] -an ' + out_file
    print(command)
    os.system(command)


def monoToStereo(input_file, out_file, swap):
    if os.path.exists(out_file):
        os.remove(out_file)
    # mono slectin number of channels (ac)
    if swap:
        command = 'ffmpeg -i ' + input_file + " -c:v copy -ac 1 " + "mono_" + out_file
    else:
        command = 'ffmpeg -i ' + input_file + " -c:v copy -ac 2 " + "stereo_" + out_file
    print(command)
    os.system(command)


mainMenu = True

while mainMenu:
    print("******************\n"
          "1.Trim\n"
          "2.YUV\n"
          "3.Scale\n"
          "4.Mono/Stereo\n"
          "5.Exit\n"
          "******************\n")
    option = input("Choose your option")
    if option == "1":
        input_file = input("Input file name: \n")
        output_file = input("Output file name: \n")
        start = int(input("Start trim point: \n"))
        end = int(input("End trim point: \n"))

        trim(input_file, output_file, start, end)

    elif option == "2":
        input_file = input("Input file name: \n")
        output_file = input("Output file name: \n")
        videoToYuv(input_file, output_file)
        # This line below works if you have the video from github
        # videoToYuv('BBB_30s.mp4', 'BBBOut_Histogram.mp4')
    elif option == "3":
        print("*******************\n"
              "SCALE OPTIONS\n"
              "*******************\n"
              "1. 720p\n"
              "2. 480p\n"
              "3. 360x240\n"
              "4. 160x120\n")
        scaleOption = input("Choose your scale")
        width = 0
        height = 0
        if scaleOption == "1":
            width = 1280
            height = 720
        elif scaleOption == "2":
            width = 854
            height = 480
        elif scaleOption == "3":
            width = 360
            height = 240
        else:
            width = 160
            height = 120

        if width != 0 and height != 0:
            input_file = input("Input file name: \n")
            output_file = input("Output file name: \n")
            scale(input_file, output_file, width, height)

    elif option == "4":
        input_file = input("Input file name: \n")
        output_file = input("Output file name: \n")
        print("********************\n"
              "MONO/STEREO\n"
              "********************\n"
              "1. Mono\n"
              "2. Stereo\n")
        monoStereoOption = input("Choose your option")
        swap = False
        if monoStereoOption == "1":
            swap = True

        monoToStereo(input_file, output_file, swap)

    elif option == "5":
        mainMenu = False
    else:
        print("Invalid option\n")
