import cv2
import mediapipe as mp
import serial
import time

arduino = serial.Serial('COM4', 115200)
time.sleep(2)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)

    angles = [0, 0, 0, 0, 0]

    if result.multi_hand_landmarks:

        for hand in result.multi_hand_landmarks:

            lm = hand.landmark

            # Thumb
            if lm[4].x < lm[3].x:
                angles[0] = 180
            else:
                angles[0] = 0

            # Index
            if lm[8].y < lm[6].y:
                angles[1] = 180
            else:
                angles[1] = 0

            # Middle
            if lm[12].y < lm[10].y:
                angles[2] = 180
            else:
                angles[2] = 0

            # Ring
            if lm[16].y < lm[14].y:
                angles[3] = 180
            else:
                angles[3] = 0

            # Pinky
            if lm[20].y < lm[18].y:
                angles[4] = 180
            else:
                angles[4] = 0

            data = f"{angles[0]},{angles[1]},{angles[2]},{angles[3]},{angles[4]}\n"

            arduino.write(data.encode())

            mp_draw.draw_landmarks(
                frame,
                hand,
                mp_hands.HAND_CONNECTIONS
            )

    cv2.putText(
        frame,
        f"T:{angles[0]} I:{angles[1]} M:{angles[2]} R:{angles[3]} P:{angles[4]}",
        (10, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    cv2.imshow("Hand Servo Control", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()