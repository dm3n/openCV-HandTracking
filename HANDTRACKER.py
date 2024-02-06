import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

# THIS IS INITIALIZING WEBCAM
cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.8, maxHands=10)


while True:
    #defining variables
    success, img = cap.read()
    width = int(cap.get(3)) # 3 is the number to get the width
    height = int(cap.get(4)) # 4 to get the height
    #gets multiple hands and gets our image and finds hands in img, if we didnt want to draw the hands out on the screen put draw=False
    hands, img = detector.findHands(img, flipType=True)
    '''
        hands is a list full of data for each indivdual hand 
        when it sees a hand it creates a new "Hand"
        data looks like:
            Hand - dict(lmList - center - type - bbox)
        and if theres multiple hands:
            Hand - dict(lmList - center - type - bbox)
            Hand - dict(lmList - center - type - bbox)
            Hand - dict(lmList - center - type - bbox)
    '''
    '''
    THIS HERE CREATES A NEW SMALLER IMAGE AND ADS IT INTO A NEW BOX 4 TIMES displaying 4 videos at the same time
    image = np.zeros(img.shape, np.uint8)
    smaller_img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = smaller_img
    image[height//2:, :width//2] = smaller_img
    image[:height//2, width//2:] = smaller_img
    image[height//2:, width//2:] = smaller_img
    '''


    #if there is a hand on the screen
    if hands:
        #   this is parting out each index of the list hands and all the info so we can print any details we need individually

        #hand1 is now equal to the first index of the data of the hand >>> Hand - dict(lmList - center - type - bbox)
        hand1 = hands[0]
        lmList1 = hand1["lmList"] # list of 21 landmarks points (each joints)
        bbox1 = hand1["bbox"] #bounding box info x,y,w,h
        centerpoint1 = hand1["center"] # gives us center of hand cx, cy
        handType1 = hand1["type"] #gives us left or right


        #this if statement helps printing the type because if there is 2 hands in the screen it will index out all the parameters for hand2 in addition to hand1
        #so we can then print the type for hand1 and hand2
        if len(hands) == 2:
            hand2 = hands[0]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"]
            centerpoint2 = hand2["center"]
            handType2 = hand2["type"]

            print(handType1,handType2)

    #title of webcam box and the webcam box itself(img)
    cv2.imshow("image", img)
    cv2.waitKey(1)
