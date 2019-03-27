import numpy
import cv2
import serial

cap = cv2.VideoCapture(0)

#ser = serial.Serial('COM9', 9600)

lower = numpy.array([29, 86, 6])
upper = numpy.array([64, 255, 255])

while(True):
    ret, frame = cap.read()

    blur = cv2.GaussianBlur(frame, (25, 25), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    canny = cv2.Canny(frame, 100, 150)

    mask = cv2.inRange(hsv, lower, upper)

    ret, thresh = cv2.threshold(mask, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(frame, contours, -1, (100, 255, 0), 3)

    res = cv2.bitwise_and(frame, frame, mask = mask)

    if len(contours) != 0:
        c = max(contours, key = cv2.contourArea)

        x,y,w,h = cv2.boundingRect(c)

        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

        cv2.line(frame, (x, y + (h - y)/2), (w, y + (h - y)/2), (10, 10, 255), 2)
        cv2.line(frame, (x + (w - x)/2, y), (x + (w - x)/2, h), (10, 10, 255), 2)

        cv2.line(frame, (x, y), (x + w, y + h), (10, 10, 255), 2)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('canny', canny)
    cv2.imshow('hsv', hsv)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()