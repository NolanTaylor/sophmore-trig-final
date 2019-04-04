import numpy
import cv2
import serial
import time
import struct

cap = cv2.VideoCapture(0)

ser = serial.Serial('COM9', 9600)

lower = numpy.array([160, 60, 170])
upper = numpy.array([255, 180, 255])

count = 0

string = ''

time.sleep(2)

ser.write("X250Y380")

while(True):

    time.sleep(0.01)

    ret, frame = cap.read()

    blur = cv2.GaussianBlur(frame, (25, 25), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    canny = cv2.Canny(frame, 100, 150)

    mask = cv2.inRange(blur, lower, upper)

    ret, thresh = cv2.threshold(mask, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(frame, contours, -1, (100, 255, 0), 3)

    res = cv2.bitwise_and(frame, frame, mask = mask)

    if len(contours) != 0:
        c = max(contours, key = cv2.contourArea)

        x,y,w,h = cv2.boundingRect(c)

        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

        cv2.line(frame, (x, y + h/2), (x + w, y + h/2), (10, 10, 255), 2)
        cv2.line(frame, (x + w/2, y), (x + w/2, y + h), (10, 10, 255), 2)

        cv2.circle(frame, (x + w/2, y + h/2), 10, (255, 255, 255), -1)

        x_out = x + w/2
        y_out = y + h/2

        x_out = str(x_out)
        y_out = str(y_out)

        if count % 10 == 0:
            ser.write("X" + x_out + "Y" + y_out)
            print (x + w/2, y + h/2)
            count = 1
        else:
            count += 1

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('canny', canny)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        ser.write("X250Y380")
        time.sleep(2)
        break

ser.close()
cap.release()
cv2.destroyAllWindows()