import cv2                                                                                       #focuses on image processing, video capture and analysis including features like face detection and object detection.
import winsound                                                                                  # provides access to the basic sound-playing machinery provided by Windows platforms.
cam = cv2.VideoCapture(0)                                                                        # capture video from 1 camera( single webcam)
                                                    
while cam.isOpened():                                                                            # weh cam is on
    ret, frame1= cam.read()                                                                      # read data from capture video
    ret, frame2= cam.read() 
    
    diff= cv2.absdiff ( frame1, frame2)                                                          # capture absoluteb diiference between frame1 one and frame2
    gray=cv2.cvtColor(diff , cv2.COLOR_RGB2GRAY)                                                 # convert the colful difference into gray color 
    # blur=cv2.GaussianBlur(gray, (5,5), 0)
    _ , thresh= cv2.threshold(gray ,20, 255 , cv2.THRESH_BINARY)                                 # convert the gray color into sharpen object 20(min) 255(max) useing threshold     
                                                                                                 #  cv2. THRESH_BINARY: If pixel intensity is greater than the set threshold, value set to 255, else set to 0 (black)
    dialated= cv2.dilate(thresh ,(3,3), iterations=3)                                            # dilation Increases the object area.  interation is size of gap
    contours, _ =cv2.findContours(dialated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)          # an outline representing or bounding the shape or form of something.
    # cv2.drawContours(frame1 ,contours , -1 ,(0,255,0),2)
    for c in contours:
        if cv2.contourArea(c)<5000:                                                              # not detect small moving object value less than 5k millimeter
            continue
        X,Y,W,H = cv2.boundingRect(c)                                                            # create boundary of detect object
        cv2.rectangle(frame1, (X,Y),(X+W, Y+H),(0,255,0),2)                                      # image: It is the image on which rectangle is to be drawn.
                                                                                                 # start_point: It is the starting coordinates of rectangle. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
                                                                                                 # end_point: It is the ending coordinates of rectangle. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
                                                                                                 # color: It is the color of border line of rectangle to be drawn. For BGR, we pass a tuple. eg: (0,255, 0) for green color.
                                                                                                 # thickness: It is the thickness of the rectangle border line in px. Thickness of -1 px will fill the rectangle shape by the specified color.
                                                                                                 # Return Value: It returns an image."""

        winsound.Beep(5000 ,200)                                                                 # play beep sound on 5000fz for 200m milsec
                                                                                                 # playsound function is used to change sound                         
                           

    if cv2.waitKey(10)== ord('q'):                                                               # wait for 10 sec if press 'q' then cam turned off
                                                                                                 # waitKey(0) you see a still image until you actually press something while for waitKey(10) the function will show a frame for at least 10 ms only.

        
        break
    cv2.imshow('camera on', frame1)                                                              # show video through frame variable
    











