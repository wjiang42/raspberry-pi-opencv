## raspberry-pi-opencv

### **Abstract**
The final project of my independent study was a portable object detection system designed to track objects using AI. From a Raspberry Pi 4 connected to a camera, the program detects a specific object and points the camera toward it, tracking it. Such a program has a variety of applications, such as moving cinematography, but a real world application will require extensive improvement to be effective. 

### **Overview**
The project consists broadly of physical components and the AI program itself. The Raspberry Pi 4 is connected to a Raspberry Pi Camera mounted on an Arducam rotating platform, which can pitch and yaw. The program reads camera footage, an AI object detection model detects the specified object - in the final code, a person - and rotates the camera toward it. All code is written in Python and the Raspberry Pi runs on Linux. 

When the program was written, a custom model had not yet been trained. As such, an existing model trained on a variety of objects and instructed to react to a specific class of object was used instead. A variety of different models were used, but the most successful model was [yolov3-tiny](https://pjreddie.com/darknet/yolo/), a YOLO objection model, which was trained on the COCO dataset and can identify [80 classes of objects](https://github.com/pjreddie/darknet/blob/master/data/coco.names). yolov3-tiny was selected as, even among YOLO models, it is remarkably efficient (at a detriment to accuracy). Since the program was designed to run on a Raspberry Pi 4, efficiency was highly desirable. 

The code necessary to control the servos of the pan-tilt platform was extracted from Arducam's servo demo 
[program](https://github.com/ArduCAM/PCA9685), and the program reads camera data and for the object detection model using OpenCV. 

### **Analysis**
While the program succeeds in its objective, it is flawed. Despite the speed YOLO offers, the model achieved a frame rate of only 5-7 fps, even after the input was downscaled to 128x128. The program also suffered input lag upwards of 2 seconds. This is almost certainly due to the relatively low computational power of Raspberry Pis, as the object detection model performed well on my laptop. The low resolution, poor frame rate, inaccuracy inherent to YOLO and outrageous delay mean that while the project works, it leaves much to be desired. Future improvements include installing an AI accelerator or using more powerful hardware and a custom model to mitigate the resource-intensive nature of object detection. 

### **Code Summary**
After importing and setting up the camera, models and data, the program reads camera data. In every frame, the model detects objects matching any of the 80 classes of objects it was trained on. For each detection, if the model is confident above a certain threshold and that detection is not determined by a function to be a duplicate, it is added to a list of detections. 

If the list of detections is not empty, the program draws them on the frame. If the detection is of a specified class - in this case, a person - the program also draws the center of the detection and rotates the camera toward it. The program then displays the edited frame and frame rate before transitioning to the next frame. 

### **Components**
- Raspberry Pi 4 
- Raspberry Pi Camera V2 
- Arducam Pan-Tilt Camera Platform

### **Software**
- Google Colab
- Gedit
- VSCode
