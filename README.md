#### raspberry-pi-opencv

This project is a program that directs a camera to point at an object using AI object detection and a Raspberry Pi 4. Through a Raspberry Pi camera attached to an Arducam rotating platform, an object detection program detects then directs the platform to tilt up/down and left/right so that the camera follows the desired object.  As of yet, a custom model has not yet been trained, so an existing model trained on a variety of objects must be instructed to react to a specific class of object. 

The program accesses the camera and reads video for to object detection model using OpenCV. The model used for testing was [yolov3-tiny](https://pjreddie.com/darknet/yolo/), which was trained on the COCO dataset and can identify [80 classes of objects](https://github.com/pjreddie/darknet/blob/master/data/coco.names). The dependency necessary to control the servos of the pan-tilt platform was extracted from Arducam's servo demo [program](https://github.com/ArduCAM/PCA9685). 

Despite the primary advantage of using yolov3-tiny over other object detection models - its speed, in frame rate - the model achieved a frame rate of only 5-7 fps after the input was downscaled to 128x128. The low resolution and frame rate compounded the already low accuracy, measured by mAP, of yolov3-tiny.

#### Components Used
- Raspberry Pi 4
- Raspberry Pi Camera V2
- Arducam Pan-Tilt Camera Platform
