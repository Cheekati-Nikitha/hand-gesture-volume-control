import cv2
import mediapipe as mp
import math
import pyautogui

x1 = y1 = x2 = y2 = 0

# Initialize webcam
webcam = cv2.VideoCapture(0)

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
drawing_utils = mp.solutions.drawing_utils

while True:
    ret, image = webcam.read()
    image = cv2.flip(image, 1)
    frame_height, frame_width, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = hands.process(rgb_image)
    hand_landmarks = output.multi_hand_landmarks

    if hand_landmarks:
        for hand in hand_landmarks:
            drawing_utils.draw_landmarks(image, hand)
            landmarks = hand.landmark

            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                if id == 8:  # Index fingertip
                    cv2.circle(image, center=(x, y), radius=8, color=(0, 255, 255), thickness=3)
                    x1, y1 = x, y

                if id == 4:  # Thumb tip
                    cv2.circle(image, center=(x, y), radius=8, color=(0, 255, 0), thickness=3)
                    x2, y2 = x, y

            # Calculate distance between thumb and index finger
            dist = math.hypot(x2 - x1, y2 - y1)
            cv2.line(image, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=5)

            # Trigger volume keys based on distance
            if dist > 50:
                pyautogui.press("volumeup")
            else:
                pyautogui.press("volumedown")

    # Show the webcam feed
    cv2.imshow("Hand volume control using python", image)
    key = cv2.waitKey(10)
    if key == 27:
        break

webcam.release()
cv2.destroyAllWindows()
