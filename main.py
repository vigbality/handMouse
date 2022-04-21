import cv2
import mediapipe as mp
import time
from pyautogui import dragTo, moveTo
cap=cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
mpHands = mp.solutions.hands
hands = mpHands.Hands(False,1, min_detection_confidence=0.25, min_tracking_confidence=0.25)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):

                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 8:
                    cv2.circle(img, (cx, cy), 10, (0, 200, 0), cv2.FILLED)
                    # print(id, cx, cy)
                    x8,y8=cx,cy
                    # dragTo(cx, cy, duration=1 / 10000)
                if id==12:
                    cv2.circle(img, (cx, cy), 10, (0, 200, 0), cv2.FILLED)
                    if cx-50 <x8 and cy<y8:
                        moveTo(x8, y8)
                    else:
                        cv2.circle(img, (x8, y8), 10, (0, 0, 200), cv2.FILLED)
                        dragTo(x8, y8)

            mpDraw.draw_landmarks(img, handLms)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
