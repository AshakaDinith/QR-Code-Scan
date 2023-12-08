import cv2
from pyzbar.pyzbar import decode
import time

cam = cv2.VideoCapture(0)
cam.set(5, 640)
cam.set(6, 480)

camera = True
while camera:
    success, frame = cam.read()

    try:
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            print(obj.type)
            print(obj.data.decode('utf-8'))
            time.sleep(6)
    except Exception as e:
        print(f"Error: {e}")

    cv2.imshow("QR Code scan", frame)
    cv2.waitKey(3)
