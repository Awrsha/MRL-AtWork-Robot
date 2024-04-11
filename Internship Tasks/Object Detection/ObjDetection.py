import time
import cv2
import numpy as np

def empty(tst):
    pass

def trackbar(minval, maxval, frameSize=[520, 170]):
    frame = cv2.namedWindow("FrameSetup")
    cv2.resizeWindow("FrameSetup", frameSize[0], frameSize[1])
    cv2.createTrackbar("Canny t1", "FrameSetup", minval['canny'][0], minval['canny'][1], empty)
    cv2.createTrackbar("Canny t2", "FrameSetup", maxval['canny'][0], maxval['canny'][1], empty)

def detectShape(contour):
    shape = "unidentified"
    arcLength = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.01*arcLength, True)
    (x, y, w, h) = cv2.boundingRect(contour)

    if len(approx) == 3:
        shape = "triangle"      
    elif len(approx) == 4:        
        ratio = w / h
        shape = "square" if ratio > 0.95 and ratio < 1.05 else "rectangle"   
    elif len(approx) == 5:        
        shape = "pentagon"      
    elif len(approx) == 6:        
        shape = "hexagon"        
    elif len(approx) == 8:        
        shape = "screw"       
    elif len(approx) == 20:
        shape = "Bracket"     
    elif len(approx) > 8 and len(approx) != 20:
        shape = "circle"

    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 150, 150), 2)
    cv2.putText(frame, f"corners: {len(approx)}", (x , y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    cv2.putText(frame, shape, (x , y+h+10), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
    return shape

try:
    cap = cv2.VideoCapture(0)
    cap.set(3, 1080)
    cap.set(4, 720)
except:
    print("Can't read video frame.")

kernel = np.ones((5, 5))

minval = {"canny": (110, 254)}
maxval = {"canny": (250, 254)}
trackbar(minval, maxval)

while True:
    cannyT1 = cv2.getTrackbarPos("Canny t1", "FrameSetup")
    cannyT2 = cv2.getTrackbarPos("Canny t2", "FrameSetup")
    
    isReadOk, frame = cap.read()
    frame = cv2.flip(frame, 1)
    begin = time.time()
    
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameBlured = cv2.GaussianBlur(frameGray, (11, 11), 0)
    frameThresh = cv2.Canny(frameBlured, cannyT1, cannyT2)
    
    frameDilate = cv2.dilate(frameThresh, kernel, iterations=2)

    contours, hierarchy = cv2.findContours(frameThresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 800:
            shape = detectShape(contour)
    
    end = time.time()
    fps = 1 /(end-begin)
    cv2.putText(frame, f"fps:{int(fps)}", (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (20,20,20), 2)
    
    cv2.imshow("frameThresh", frameThresh)
    cv2.imshow("feed", frame)
    
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
