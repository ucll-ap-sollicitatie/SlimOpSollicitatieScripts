import cv2
import sys
import textwrap

videoName = sys.argv[1]
file = open(sys.argv[2], 'r')
lines = file.readlines()
endTime = []
textOnScreen = []
if len(lines) > 2:
    lines.pop(0)
    for x in range(0, len(lines)):
        if x % 2 == 0:
            endTime.append(float(lines[x].strip('\n')))
        else:
            textOnScreen.append(lines[x].strip('\n'))

cap = cv2.VideoCapture(videoName)
fps = cap.get(cv2.CAP_PROP_FPS)
out = cv2.VideoWriter('processed_' + videoName, -1, fps, (640, 480))
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
n_frames = 0
timeCounter = 0
cx, cy = 0, 375
#print(float(frame_count) / float(fps))
#print(fps, frame_count)
#print(len(endTime))

while True:
    ret, frame = cap.read()
    n_frames += 1
    duration = n_frames / float(fps)
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    if n_frames - 1 <= round(endTime[timeCounter] * fps):
        #print('END TIME: ' + str(endTime[timeCounter]))
        #print("DURATION: " + str(duration))
        wrapped = textwrap.wrap(textOnScreen[timeCounter], 40)
        cv2.rectangle(frame, (0, 480), (640, 350), (255, 255, 255), -2)
        for he, line in enumerate(wrapped):
            gap = 20
            cv2.putText(frame, line, (cx, cy + he * gap), font, 1, (235, 144, 65), 1, cv2.LINE_AA)

            if duration >= endTime[timeCounter]:
                timeCounter += 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        out.write(frame)
        cv2.imshow('video', frame)
    if duration == float(frame_count) / float(fps):
        cap.release()
        cv2.destroyWindow()
