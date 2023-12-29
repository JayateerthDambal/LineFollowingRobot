import cv2
import numpy as np
from motor_control import forward, turn_left, turn_right, stop
from simple_pid import PID


def process_image(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY_INV)

    return thresh


def find_largest_contour(processed_frame):
    contours, _ = cv2.findContours(
        processed_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(largest_contour)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            return (cx, cy), largest_contour
    return None, None


def main():
    camera = cv2.VideoCapture(0)
    pid = PID(0.1, 0.01, 0.01, setpoint=0)
    pid.output_limits = (-1, 1)

    try:
        while True:
            ret, frame = camera.read()
            if not ret:
                break

            processed_frame = process_image(frame)
            center, contour = find_largest_contour(processed_frame)

            if center is not None:
                frame_center = frame.shape[1] // 2
                deviation = center[0] - frame_center

                control = pid(deviation)

                if control > 0.1:
                    turn_right()
                elif control < -0.1:
                    turn_left()
                else:
                    forward()
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
