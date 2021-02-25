# Import everything needed to edit video clips
#from moviepy.editor import *

# loading video dsa gfg intro video
#clip = VideoFileClip("TEST.mp4")

# clipping of the video
# getting video for only starting 10 seconds
#clip = clip.subclip(0, 1)

# Reduce the audio volume (volume x 0.8)
#clip = clip.volumex(0.8)

# Generate a text clip
#txt_clip = TextClip("DICKS", fontsize=75, color='black')

# setting position of text in the center and duration will be 10 seconds
#txt_clip = txt_clip.set_pos('center').set_duration(10)

# Overlay the text clip on the first video clip
#video = CompositeVideoClip([clip, txt_clip])

# showing video
#video.ipython_display(width=280)

import cv2

cap = cv2.VideoCapture('Test.mp4')
out = cv2.VideoWriter('output.mp4', -1, 20.0, (640, 480))
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
n_frames = 0
startTime = 0
endTime = [1, 2]
timeCounter = 0
textOnScreen = ["TEXT 1", "TEXT 2"]


while True:
    ret, frame = cap.read()
    n_frames += 1
    duration = n_frames / float(fps)
    font = cv2.FONT_HERSHEY_PLAIN
    if startTime - 1 <= duration <= endTime[timeCounter]:
        cv2.putText(frame, textOnScreen[timeCounter], (50, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4)
        out.write(frame)
        cv2.imshow('video', frame)
        if duration == endTime[timeCounter]:
            startTime = endTime[timeCounter]
            timeCounter += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    if duration == float(frame_count)/ float(fps):
        cap.release()
        cv2.destroyWindow()
