import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

# vid_input = 'race_car.mp4'

# def draw_rectangle(frame,bbox):
#     p1 =(int(bbox[0]),int(bbox[1]))
#     p2=(int(bbox[0]+bbox[2]),int(bbox[1]+bbox[3]))
#     cv2.rectangle(frame,p1,p2,(255,0,0),2,1)

# def display_rectangle(frame,bbox):
#     plt.figure(figsize=(20,10))
#     frameCopy = frame.copy()
#     draw_rectangle(frameCopy,bbox)
#     frameCopy = cv2.cvtColor(frameCopy,cv2.COLOR_BGR2RGB)
#     plt.imshow(frameCopy)
#     plt.axis('off')

# def drawText(frame, txt, location, color=(50, 170, 50)):
#     cv2.putText(frame, txt, location, cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

# tracker_types = [
#     "BOOSTING",
#     "MIL",
#     "KCF",
#     "CSRT",
#     "TLD",
#     "MEDIANFLOW",
#     "GOTURN",
#     "MOSSE",
# ]

# tracker_type = tracker_types[2]

# tracker_type = tracker_types[2]

# if tracker_type == "BOOSTING":
#     tracker = cv2.legacy.TrackerBoosting.create()
# elif tracker_type == "MIL":
#     tracker = cv2.legacy.TrackerMIL.create()
# elif tracker_type == "KCF":
#     tracker = cv2.TrackerKCF.create()
# elif tracker_type == "CSRT":
#     tracker = cv2.TrackerCSRT.create()
# elif tracker_type == "TLD":
#     tracker = cv2.legacy.TrackerTLD.create()
# elif tracker_type == "MEDIANFLOW":
#     tracker = cv2.legacy.TrackerMedianFlow.create()
# elif tracker_type == "GOTURN":
#     tracker = cv2.TrackerGOTURN.create()
# else:
#     tracker = cv2.legacy.TrackerMOSSE.create()

# viedo = cv2.VideoCapture(vid_input)
# ok,frame = viedo.read()

# if not viedo.isOpened():
#     print('Cant open Vid')
#     sys.exit()
# else:
#     width = int(viedo.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height =int(viedo.get(cv2.CAP_PROP_FRAME_HEIGHT))

# video_output_file_name = 'race_Car-' + tracker_type + ".mp4"
# viedo_out = cv2.VideoWriter(video_output_file_name,cv2.VideoWriter_fourcc(*"XVID"),10,(width,height))

# video_output_file_name

video_input_file_name = "race_car.mp4"


def drawRectangle(frame, bbox):
    p1 = (int(bbox[0]), int(bbox[1]))
    p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
    cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)


def displayRectangle(frame, bbox):
    plt.figure(figsize=(20, 10))
    frameCopy = frame.copy()
    drawRectangle(frameCopy, bbox)
    frameCopy = cv2.cvtColor(frameCopy, cv2.COLOR_RGB2BGR)
    plt.imshow(frameCopy)
    plt.axis("off")


def drawText(frame, txt, location, color=(50, 170, 50)):
    cv2.putText(frame, txt, location, cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

# Set up tracker
tracker_types = [
    "BOOSTING",
    "MIL",
    "KCF",
    "CSRT",
    "TLD",
    "MEDIANFLOW",
    "GOTURN",
    "MOSSE",
]

# Set up tracker
tracker_types = [
    "BOOSTING",
    "MIL",
    "KCF",
    "CSRT",
    "TLD",
    "MEDIANFLOW",
    "GOTURN",
    "MOSSE",
]

# Change the index to change the tracker type
tracker_type = tracker_types[3]

if tracker_type == "BOOSTING":
    tracker = cv2.legacy.TrackerBoosting.create()
elif tracker_type == "MIL":
    tracker = cv2.legacy.TrackerMIL.create()
elif tracker_type == "KCF":
    tracker = cv2.TrackerKCF_create()
elif tracker_type == "CSRT":
    tracker = cv2.TrackerCSRT_create()  # Poprawiona linia
elif tracker_type == "TLD":
    tracker = cv2.legacy.TrackerTLD.create()
elif tracker_type == "MEDIANFLOW":
    tracker = cv2.legacy.TrackerMedianFlow.create()
elif tracker_type == "GOTURN":
    tracker = cv2.TrackerGOTURN.create()
else:
    tracker = cv2.legacy.TrackerMOSSE.create()


# Read video
video = cv2.VideoCapture(video_input_file_name)
ok, frame = video.read()

# Exit if video not opened
if not video.isOpened():
    print("Could not open video")
    sys.exit()
else:
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

video_output_file_name = "race_car-" + tracker_type + ".mp4"
video_out = cv2.VideoWriter(video_output_file_name, cv2.VideoWriter_fourcc(*"XVID"), 10, (width, height))

video_output_file_name
# Define a bounding box
bbox = (1300, 405, 160, 120)
# bbox = cv2.selectROI(frame, False)
# print(bbox)
displayRectangle(frame, bbox)
ok = tracker.init(frame,bbox)

while True:
    ok ,frame = video.read()
    if not ok:
        break
    timer = cv2.getTickCount()
    ok , bbox = tracker.update(frame)
    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    if ok:
        drawRectangle(frame,bbox)
    else:
        drawText(frame, "Tracking failure detected", (80, 140), (0, 0, 255))
        drawText(frame, tracker_type + " Tracker", (80, 60))
    drawText(frame, "FPS : " + str(int(fps)), (80, 100))

    # Write frame to video
    video_out.write(frame)

video.release()
video_out.release()