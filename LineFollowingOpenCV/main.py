import cv2
import numpy as np
from motor_control import forward, backward, turn_left, turn_right, stop


def process_image(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY_INV)
    return thresh


def find_line_center(processed_frame):
    M = cv2.moments(processed_frame)
    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        return (cx, cy)
    return None


def main():
    camera = cv2.VideoCapture(0)
    try:
        while True:
            ret, frame = camera.read()
            if not ret:
                break

            processed_frame = process_image(frame)
            center = find_line_center(processed_frame)

            if center is not None:
                frame_center = frame.shape[1] // 2
                deviation = center[0] - frame_center

                if abs(deviation) < 10:
                    forward()
                elif deviation >= 10:
                    turn_right()
                elif deviation <= -10:
                    turn_left()
            else:
                stop()

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()
        stop()


if __name__ == "__main__":
    main()
