import cv2
import time
import sys, select

def mytime_sleep(time):
  i, o, e = select.select([sys.stdin], [], [], time)
  if (i):
    key = sys.stdin.readline().strip()
    return key
  else:
    return None

interval = 540  # seconds
num_frames = 9600 
out_fps = 40 

capture1 = cv2.VideoCapture(0)
size1 =(int(capture1.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
    int(capture1.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
video1 = cv2.VideoWriter("time_lapse.avi", cv2.cv.CV_FOURCC('I','4','2','0'), out_fps, size1)
capture1.release()
# I have to camera to work at one time

capture2 = cv2.VideoCapture(1)
size2 =(int(capture2.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
    int(capture2.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))
video2 = cv2.VideoWriter("time_lapse2.avi", cv2.cv.CV_FOURCC('I','4','2','0'), out_fps, size2)
capture2.release()


# capture frames to video
frame = None
for i in xrange(num_frames):
  capture1 = cv2.VideoCapture(0)
  # for low quality webcams, discard the starting unstable frames
  for j in range(3):
    capture1.read()
  _, frame = capture1.read()
  capture1.release()    
  print frame[1][1]
  if i%2==0:
    video1.write(frame)
 
  ## Optional, in case you need the frames for GIF or so
  filename = 'lapse/c1_{:6}.png'.format(i).replace(' ', '0')
  cv2.imwrite(filename, frame)
  print('c1 Frame {} is captured.'.format(i))
  time.sleep(1)
  for j in range(3):
    capture2.read()
  capture2 = cv2.VideoCapture(1)
  _, frame = capture2.read()
  print frame[1][1]
  capture2.release()
  if i%2==0: 
    video2.write(frame)
  ## Optional, in case you need the frames for GIF or so
  filename = 'lapse/c2_{:6}.png'.format(i).replace(' ', '0')
  cv2.imwrite(filename, frame)

  print('c2 Frame {} is captured.'.format(i))
  if i>=5:
    q = mytime_sleep(interval-3)
    if q=='q':
      video1.release()
      video2.release()
      print q
      break
    elif q:
      print q
    
  else:
    q = mytime_sleep(1)
    if q=='q':
      video1.release()
      video2.release()
      print q
      break
    elif q:
      print q


