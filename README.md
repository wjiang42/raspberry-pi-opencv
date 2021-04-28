# raspberry-pi-opencv

This project is an attempt at object tracking using a Raspberry Pi. Through a the Raspberry Pi camera attached to a rotating platform, an object detection model directed the platform to tilt up/down and left/right and follow the desired object.  As of yet, a custom model has not yet been programmed, so the model must be instructed to react to a certain class of object. 

Camera access and object detection used OpenCV. The model used for testing is [yolov3-tiny](https://pjreddie.com/darknet/yolo/), one of the fastest object detection models currently available. 

Despite speed of yolov3-tiny, the model achieves a frame rate of 5-7 fps when the input is scaled to 128x128. This compounds the already relatively low mAP of yolov3-tiny. 

#### Components Used
- Raspberry Pi 4
- Raspberry Pi Camera V2
- Arducam Pan-Tilt Camera Platform
