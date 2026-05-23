import cv2
import time
import pygame
from src.detector import HandDetector
from src.overlay_utils import load_gif_frames

frames_cat = load_gif_frames("assets/cat_animation.gif", scale=2.5)
frames_nick = load_gif_frames("assets/nick_animation.gif", scale=1.0)
sound_path = "assets/scubbaaa.mp3"

WINDOW_MARGIN = 30
scuba_window_pos = (WINDOW_MARGIN, WINDOW_MARGIN)
nick_window_pos = (WINDOW_MARGIN * 2 + frames_cat[0].shape[1], WINDOW_MARGIN)

all_frames = [frames_cat, frames_nick]
current_indices = [0, 0]
prev_x_positions = [0, 0]
last_frame_advance_times = [time.perf_counter(), time.perf_counter()]
frame_intervals = [1 / 15, 1 / 15]

unified_last_move_time = 0
both_windows_active = False

sound_available = False
try:
    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    sound_available = True
except Exception as exc:
    print(f"No se pudo inicializar el audio: {exc}")


def start_window_sound():
    if sound_available and not pygame.mixer.music.get_busy():
        pygame.mixer.music.play(-1)


def stop_window_sound():
    if sound_available:
        pygame.mixer.music.stop()

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
    detected_hands = detector.results.multi_hand_landmarks or []

    if len(detected_hands) >= 2:
        for i, hand_lms in enumerate(detected_hands):
            if i < 2:
                h, w, c = img.shape
                curr_x = int(hand_lms.landmark[0].x * w)

                if abs(curr_x - prev_x_positions[i]) > 10:
                    prev_x_positions[i] = curr_x
                    movement_detected = True

    if movement_detected:
        unified_last_move_time = time.time()

    if len(detected_hands) >= 2 and time.time() - unified_last_move_time < 0.5:
        now = time.perf_counter()

        if not both_windows_active:
            cv2.namedWindow("Scuba Cat", cv2.WINDOW_AUTOSIZE)
            cv2.namedWindow("Nick Wilde", cv2.WINDOW_AUTOSIZE)
            cv2.resizeWindow("Nick Wilde", 400, 400)
            cv2.moveWindow("Scuba Cat", scuba_window_pos[0], scuba_window_pos[1])
            cv2.moveWindow("Nick Wilde", nick_window_pos[0], nick_window_pos[1])
            last_frame_advance_times = [now, now]
            start_window_sound()
            both_windows_active = True

        for i, frames in enumerate(all_frames):
            if not frames:
                continue

            if now - last_frame_advance_times[i] >= frame_intervals[i]:
                steps = int((now - last_frame_advance_times[i]) / frame_intervals[i])
                current_indices[i] = (current_indices[i] + steps) % len(frames)
                last_frame_advance_times[i] += steps * frame_intervals[i]
        
        cv2.imshow("Scuba Cat", frames_cat[current_indices[0]])
        cv2.imshow("Nick Wilde", frames_nick[current_indices[1]])
    else:
        if both_windows_active:
            cv2.destroyWindow("Scuba Cat")
            cv2.destroyWindow("Nick Wilde")
            stop_window_sound()
            both_windows_active = False

    cv2.imshow("Minha Camera", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
stop_window_sound()
cv2.destroyAllWindows()