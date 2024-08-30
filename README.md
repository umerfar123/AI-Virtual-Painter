## AI VIRTUAL PAINTER

This is a python application that allows you draw to based on hand gestures captured from your video capturing device. This Python project leverages computer vision techniques to enable users to draw using hand gestures. By capturing video 
input and analyzing the position of the user's hand, the program can interpret hand movements as drawing strokes.

> [!NOTE]
> Required Libraries
> + OpenCV: For image processing and video capture.
> + MediaPipe: For real-time hand tracking.
  
## Project Structure

The project includes mainly two files that tracks the hand and draw on your webcam window. Understanding these modules is necessary to know how the system works.

-> handtracking.py  
-> main.py

  * Handtracking Module
    
    Initializes MediaPipe's Hands solution, which is designed to detect and track human hands in real-time. It provides functions to process input images, identify the presence of hands, and extract the positions of key points on the detected hands.
    These key points, known as landmarks, represent specific locations on the hand, such as the fingertips, wrist, and joints.

  * Main Module

    The code first establishes a video capture stream to obtain real-time video input. It then creates an instance of the HandTracker class, which is responsible for hand detection and landmark extraction. Within a continuous loop, each frame from the
    video stream is processed by the HandTracker to identify the presence of hands and determine the positions of their key points. Based on the detected finger positions, the drawing logic will create corresponding drawing strokes on a virtual canvas. Finally, the processed image, with the drawn strokes overlaid, is displayed to the user.

  * Drawing Logic

    The drawing mode is activated when the index finger is raised, while the selection mode is engaged when two fingers are held aloft. The program utilizes a [finger counter](https://github.com/umerfar123/um_Finger_Counter) to determine the number of raised fingers, enabling it to accurately differentiate
    between these two modes. In drawing mode, the system tracks the position of the index fingertip using landmarks provided by the hands module. As the fingertip moves, a line is drawn, connecting its current position to its previous location. This dynamic
    line creation allows users to draw various shapes and patterns based on their hand movements.

## Installation

1. Clone this repository using

   ```
   git clone https://github.com/umerfar123/AI-Virtual-Painter.git 
   ```

2. Install required libraries using

    ```python
      pip install -r requirements.txt
    ```
3. Run the main file using

    ```python
      python run main.py
    ```
___

>[!TIP]
> While drawing remember that:
>   + Two finger for selecting colour and eraser.
>   + One finger for drawing with that selection
