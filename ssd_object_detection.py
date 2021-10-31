import numpy as np
import cv2
import time

import adafruit_servokit
global image_count
image_count = 0

#orient camera
class ServoKit(object):
    default_angle = 90

    def __init__(self, num_ports):
        self.kit = adafruit_servokit.ServoKit(channels=16)
        self.num_ports = num_ports
        self.resetAll()

    def setAngle(self, port, angle):
        if angle < 0:
            self.kit.servo[port].angle = 0
        elif angle > 180:
            self.kit.servo[port].angle = 180
        else:
            self.kit.servo[port].angle = angle
    
    def getAngle(self, port):
        return self.kit.servo[port].angle

    def reset(self, port):
        self.kit.servo[port].angle = self.default_angle

    def resetAll(self):
        for i in range(self.num_ports):
            self.kit.servo[i].angle = self.default_angle

servoKit = ServoKit(4)

#access camera
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS, 7)

#import model and classes
config_path = "/home/pi/raspberry-pi-opencv/yolov3-tiny.cfg"
weights_path = "/home/pi/raspberry-pi-opencv/yolov3-tiny.weights"
min_prob = 0.2

CLASSES = open('/home/pi/raspberry-pi-opencv/coco.names').read().strip().split('\n')

net = cv2.dnn.readNetFromDarknet(config_path, weights_path)

while True:
    start = time.time()
    ret, image = cam.read()
    (h, w) = image.shape[:2] #process image
    blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (128, 128), swapRB=True, crop=False)
    net.setInput(blob)
    detections = net.forward()
    
    boxes = []
    confidences = []
    classIDs = []
    
    for output in detections:
        scores = output[5:]
        classID = np.argmax(scores)
        confidence = scores[classID]
        if confidence > 0.2: #filter detections
            box = output[0:4] * np.array([w, h, w, h])
            (centerX, centerY, width, height) = box.astype("int")
            x = int(centerX - (width / 2))
            y = int(centerY - (height / 2))
            boxes.append([x, y, int(width), int(height)])
            confidences.append(float(confidence))
            classIDs.append(classID)
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.2, 0.3)
    if len(idxs) > 0:
        for i in idxs.flatten(): #draw detections
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 250, 180), 2)
            text = "{}: {:.4f}".format(CLASSES[classIDs[i]], confidences[i])
            cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 250, 180), 2)
            if CLASSES[classIDs[i]] == "person": #filter detections for a specific object
                mx = int(x + (w/2))
                my = int(y + (h/2))
                cv2.rectangle(image, (mx, my), (mx + 1, my + 1), (0, 250, 180), 2)
                cx = 640/2
                cy = 480/2
                motor_step = 2 #rotate camera to be roughly centered on object
                if abs(mx-cx) > 20:
                    if mx < cx:
                        servoKit.setAngle(1, servoKit.getAngle(1) - motor_step)
                    else:
                        servoKit.setAngle(1, servoKit.getAngle(1) + motor_step)
                if abs(my-cy) > 20:
                    if my < cy:
                        servoKit.setAngle(0, servoKit.getAngle(0) + motor_step)
                    else:
                        servoKit.setAngle(0, servoKit.getAngle(0) - motor_step)
    end = time.time()
    print("fps = ", 1/(end-start))
    cv2.imshow("Output", image)
    cv2.waitKey(1)


