import numpy
import cv2

cap = cv2.VideoCapture(0)

lower = numpy.array([29, 86, 6])
upper = numpy.array([64, 255, 255])

while(True):
    ret, frame = cap.read()

    blur = cv2.blur(frame, (20, 20))
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    canny = cv2.Canny(frame, 100, 150)

    mask = cv2.inRange(hsv, lower, upper)

    ret, thresh = cv2.threshold(mask, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(frame, contours, -1, (100, 255, 0), 3)

    res = cv2.bitwise_and(frame, frame, mask = mask)

    if len(contours) != 0:
        leftmost = tuple(contours[0][contours[0][:,:,0].argmin()][0])
        rightmost = tuple(contours[0][contours[0][:,:,0].argmax()][0])
        topmost = tuple(contours[0][contours[0][:,:,1].argmin()][0])
        bottommost = tuple(contours[0][contours[0][:,:,1].argmax()][0])

        cv2.circle(frame, leftmost, 5, (255, 10, 10), -1)
        cv2.circle(frame, rightmost, 5, (255, 10, 10), -1)
        cv2.circle(frame, topmost, 5, (255, 10, 10), -1)
        cv2.circle(frame, bottommost, 5, (255, 10, 10), -1)

        c = max(contours, key = cv2.contourArea)

        x,y,w,h = cv2.boundingRect(c)

        cv2.rectangle(res, (x,y), (x+w,y+h), (255,0,0), 2)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('canny', canny)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()