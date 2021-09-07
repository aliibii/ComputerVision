## Importing OpenCV library 
import cv2


#if you want to hear a sound after movement detection import
import simpleaudio 

#starting the cam to capture
cam = cv2.VideoCapture(0)

#creating a while loop for making the related setup
while cam.isOpened():
    #we'll create 2 vareables with the value of camera image so we can detect the deffrents by using opencv
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)

    #in computer viseion and opencv the best practice is to use gray color for image proccessing by using opencv
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)


    #we'll make the image blur so we could exclude the noises of the image and movements by using opencv
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)

    #at this point we make the contours by using opencv
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        ################################################################
        #making sound after movement detection###

        # wave_obj = simpleaudio.WaveObject.from_wave_file("alert.wav")
        # play_obj = wave_obj.play()
        # play_obj.wait_done()


### pressing Q to exit the program ###
    if cv2.waitKey(10) == ord('q'):
        break
    ### Showing the proccessed frame or image ###
    cv2.imshow('Security Cam', frame1)
