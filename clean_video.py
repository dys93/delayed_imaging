import os
import cv2

video_second = 25 # set video length ot 28s
size = (640, 480) # cut out each frame to 0:360, 0:480
remove_num = 150  # remove first 150 frame
input_avi = "video/time_lapse.avi"
output_mp4 = "big.mp4"



# remove all frame in folder frame
for f in os.listdir("./frame"):
	os.remove("frame/"+f)

# split a video into frames
# need mplayer, get it by --- sudo apt-get install mplayer
command = "mplayer -ao null %s -vo jpeg:outdir=frame" % input_avi
os.system(command)

# frame num
fn = os.listdir("./frame")
fn = len(fn) + 1

# remove first 150 frame because plants don't sprout
for i in range(1, fn):
	if i < remove_num:
		os.remove('frame/%08d.jpg' % i)
	else:
		os.rename('frame/%08d.jpg' % i, 'frame/%08d.jpg' % (i-remove_num))
fn = fn - remove_num

# cut out each frame because some part of pic is fuzzy
# compression video size
for i in range(1, fn):
	file_name = "frame/%08d.jpg" % (i)
	im = cv2.imread(file_name)
	cv2.imwrite(file_name, im[0:size[1], 0:size[0], :])

fps = fn/video_second
video = cv2.VideoWriter("video/tmp.avi", cv2.cv.CV_FOURCC('I','4', '2', '0'), fps, size)
for i in range(1, fn):                                                     
	fileName = "frame/%08d.jpg" % i
	frame = cv2.imread(fileName)
	video.write(frame)

# translate .avi to .mp4
# need avconv, get it by --- sudo apt-get install avconv
command = "avconv -i video/tmp.avi -c:v libx264 -c:a copy %s" % output_mp4
os.system(command)


