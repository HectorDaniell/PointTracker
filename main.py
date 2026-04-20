import cv2
import time
from src.detector import HandDetector
from src.overlay_utils import load_gif_frames

frames_cat = load_gif_frames("assets/cat_animation.gif", scale=2.5)
frames_nick = load_gif_frames("assets/nick_animation.gif", scale=1.0)

all_frames = [frames_cat, frames_nick]
current_indices = [0, 0]
prev_x_positions = [0, 0]

unified_last_move_time = 0
both_windows_active = False

detector = HandDetector(detection_con=0.7, track_con=0.7)
cap = cv2.VideoCapture(0)

cap.set(3, 640) 
cap.set(4, 480)

while True:
    success, img = cap.read()
    if not success: break
    img = cv2.flip(img, 1)
    
    img = detector.find_hands(img)
    movement_detected = False

    if detector.results.multi_hand_landmarks:
        for i, hand_lms in enumerate(detector.results.multi_hand_landmarks):
            if i < 2:
                h, w, c = img.shape
                curr_x = int(hand_lms.landmark[0].x * w)

                if abs(curr_x - prev_x_positions[i]) > 10:
                    step = 2 if i == 1 else 1
                    current_indices[i] = (current_indices[i] + step) % len(all_frames[i])
                    
                    prev_x_positions[i] = curr_x
                    movement_detected = True

    if movement_detected:
        unified_last_move_time = time.time()

    if time.time() - unified_last_move_time < 0.5:
        if not both_windows_active:
            cv2.namedWindow("Scuba Cat", cv2.WINDOW_AUTOSIZE)
            cv2.namedWindow("Nick Wilde", cv2.WINDOW_AUTOSIZE)
            cv2.resizeWindow("Nick Wilde", 400, 400)
            both_windows_active = True
        
        cv2.imshow("Scuba Cat", frames_cat[current_indices[0]])
        cv2.imshow("Nick Wilde", frames_nick[current_indices[1]])
    else:
        if both_windows_active:
            cv2.destroyWindow("Scuba Cat")
            cv2.destroyWindow("Nick Wilde")
            both_windows_active = False

    cv2.imshow("Minha Camera", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()