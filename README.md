#### raspberry-pi-opencv

This project is an attempt at object tracking using a Raspberry Pi 4. Through a Raspberry Pi camera attached to a rotating platform, an object detection model directs the platform to tilt up/down and left/right and follow the desired object.  As of yet, a custom model has not yet been trained, so the model must be instructed to react to a certain class of object. 

Camera access and object detection uses OpenCV. The model used for testing was [yolov3-tiny](https://pjreddie.com/darknet/yolo/), which was trained on the COCO dataset and has [80 classes](https://github.com/pjreddie/darknet/blob/master/data/coco.names). The dependency necessary to control the servos of the pan-tilt platform were extracted from Arducam's servo demo [program](https://github.com/ArduCAM/PCA9685). 

Despite speed of yolov3-tiny, the model only achieves a frame rate of 5-7 fps when the input is scaled to 128x128. This compounds the already relatively low mAP of yolov3-tiny. Combined with significant delay, the model often overshoots or fails to detect the object. 

#### Components Used
- Raspberry Pi 4
- Raspberry Pi Camera V2
- Arducam Pan-Tilt Camera Platform
