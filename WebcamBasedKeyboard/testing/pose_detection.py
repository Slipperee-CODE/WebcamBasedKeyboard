import mediapipe as mp
import cv2

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=2)
mp_drawing = mp.solutions.drawing_utils

vid = cv2.VideoCapture(1)

#Research how to make on screen UI, then use the on screen UI pixel positions and compare those to the landmark pixel positions
#Make it so you can both create, move and delete the points
#Make it so you can create, save and load presets for groupings of points including one for the QWERTY Keyboard layout
#Make it so you have to be relatively near a point for a certain amount of time for the key to be held/pressed
    #Make distance, time and held or pressed once all settings, make the last one toggleable
#Get the landmark pixel positions using the code from the ArmArduinoTurret

while True:
    _, frame = vid.read()

    imageRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(imageRGB)

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(image=imageRGB, landmark_list=results.pose_landmarks, connections=mp_pose.POSE_CONNECTIONS)

    cv2.imshow("video", imageRGB)
    cv2.waitKey(1)