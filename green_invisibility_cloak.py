import cv2
import numpy as np
import time

# Step 1: Capture the background first
cap = cv2.VideoCapture(0)
time.sleep(2)

for i in range(60):
    ret, background = cap.read()
background = np.flip(background, axis=1)

# Step 2: Fullscreen window
cv2.namedWindow("Invisibility Cloak", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Invisibility Cloak", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = np.flip(frame, axis=1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Step 3: Green color detection
    lower_green = np.array([35, 50, 50])   # Lower HSV bound for green
    upper_green = np.array([90, 255, 255]) # Upper HSV bound for green

    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Step 4: Smooth the mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3,3), np.uint8))
    mask = cv2.GaussianBlur(mask, (15, 15), 0)

    mask_inv = cv2.bitwise_not(mask)

    # Step 5: Combine background and current frame
    res1 = cv2.bitwise_and(background, background, mask=mask)
    res2 = cv2.bitwise_and(frame, frame, mask=mask_inv)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Invisibility Cloak", final_output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
