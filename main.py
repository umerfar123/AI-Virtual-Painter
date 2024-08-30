import cv2
import numpy as np
import time
import os
import handtracking as ht

###Variables_________________________________
imagecanvas=np.zeros((480,640,3),dtype=np.uint8)
c=(0,0,0)
xp,yp= 0,0
#_________________________________________

#accessing the overlay images
folderpath='Dashboard'
mylist=os.listdir(folderpath)

#Storing address of overlay images to a list
overlayList=[]
for imagepath in mylist:
    image = cv2.imread(f"{folderpath}/{imagepath}" )
    overlayList.append(image)     
header = overlayList[0]

#Creating object for videocapture module
cap=cv2.VideoCapture(0)
cap.set(3,720)
cap.set(4,720)

#class object from handtracking.py
handtracker=ht.handDetector(detectionCon=0.8)

#continously processing each frame
while True:
    
    #Capturing Webcam
    ret,img=cap.read()
    img=cv2.flip(img,1)
    
    #Handtracking
    img=handtracker.findHands(img)
    
    #Marking joints
    landList=handtracker.findPosition(img,draw=False)

    #further processing if hand has tracked
    if len(landList)!=0:
        
        text='hi'
        xp,yp= 0,0
        #Counting fingers to switch to selection and drawing mode
        fingers=handtracker.fingersUp(landList)  

        #getting coordinates of index finger and middle finger tip
        x1 , y1 = landList[8][1:]
        x2 , y2 = landList[12][1:]
        x_avg = (x1+x1)//2
        y_avg = (y1+y2)//2 
         
        #Selection mode 
        if fingers[1] and fingers[2] and (not fingers[3]) and (not fingers[4]):
            text='select'
        
        if fingers[1] and fingers[2]:
            if y_avg< 105:
                if 175<x_avg<295:
                    header=overlayList[1]
                    c=(0,0,255)
                    
                elif 296<x_avg<396:
                    header=overlayList[2]
                    c=(0,255,255)
                elif 400<x_avg<500:
                    header=overlayList[3]
                    c=(0,255,0)
                elif 510<x_avg<610:
                    header=overlayList[4]
                    c=(0,0,0)
                    
        #Drawing mode              
        elif fingers[1]:
            text='Draw'
            #Selection indicator on real feed
            cv2.circle(img,center=(x1,y1),color=c,radius=10,thickness=-1)
            
            #Eraser
            if c==(0,0,0):
                cv2.circle(imagecanvas,center=(x1,y1),color=c,radius=30,thickness=-1)
            
            #Brush
            else:  
                print("Drawing mode")
                if xp == 0 and yp ==0:
                    xp,yp=x1,y1
                
                cv2.line(imagecanvas,pt1=(xp,yp),pt2=(x1,y1),thickness=15,color=c)
                xp,yp= x1,y1
    
        cv2.rectangle(img,pt1=(0,400),pt2=(100,480),color=(255,255,0),thickness=-1)
        
        height, width, _ = img.shape
        x1,y1= 100,480
        x2,y2=0,400
        # Get text font and size
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5
        # Calculate text dimensions
        text_width, text_height = cv2.getTextSize(text, font, font_scale, 1)[0]
        # Calculate text position
        x_text = x1 + (x2 - x1 - text_width) // 2
        y_text = y1 + (y2 - y1 + text_height) // 2

        cv2.putText(img, text, (x_text, y_text), font, font_scale, (0, 0, 0), 1)
    
 
    #Setting the overlay dashboard over webcam
    overlay_image_resized=cv2.resize(header,(640,105))
    img[0:105,0:640] = overlay_image_resized
    
    #overlaying canvas with real feed from camera
    imgCanva_gray=cv2.cvtColor(imagecanvas,cv2.COLOR_BGR2GRAY)
    _,canva_inv=cv2.threshold(imgCanva_gray,50,255,cv2.THRESH_BINARY_INV)
    canva_inv=cv2.cvtColor(canva_inv,cv2.COLOR_GRAY2BGR)
    img=cv2.bitwise_and(img,canva_inv)
    img=cv2.bitwise_or(img,imagecanvas)
    
    #printing the frame
    cv2.imshow("Real Feed",img)
    
    #Setting variable x to be the keyword for exiting the webcam
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    
cap.release()
cv2.destroyAllWindows()
    