#### raspberry-pi-opencv

This repository contains the code necessary for an AI object detection program for the final project of an independent study, running on a Raspberry Pi 4. Using a Raspberry Pi camera attached to an Arducam rotating platform, the program uses an AI object detection model to detect a specified object, then pitch and yaw so that the camera points at the desired object. 

As of yet, a custom model has not yet been trained, so an existing model trained on a variety of objects must be instructed to react to a specific class of object. The model used was [yolov3-tiny](https://pjreddie.com/darknet/yolo/), a YOLO objection model, which was trained on the COCO dataset and can identify [80 classes of objects](https://github.com/pjreddie/darknet/blob/master/data/coco.names). The dependency necessary to control the servos of the pan-tilt platform was extracted from Arducam's servo demo [program](https://github.com/ArduCAM/PCA9685), and the program reads camera data and for the object detection model using OpenCV. 

This program succeeds in its objective, but it is flawed. The primary advantage of YOLO is it’s speed, which is achieved with some detriment to accuracy, yet the model achieved a frame rate of only 5-7 fps, even after the input was downscaled to 128x128. The low resolution and frame rate compounded the already low accuracy of the model used, yolov3-tiny. Future improvements to this project include installing an AI accelerator or more powerful hardware and a custom model to mitigate the resource-intensive nature of object detection. 

#### Components Used
- Raspberry Pi 4
- Raspberry Pi Camera V2
- Arducam Pan-Tilt Camera Platform
