import os
import cv2
import numpy as np

def photocutter(img):
        
    img1 = cv2.imread(img)

    # height, width, number of channels in image
    height, width, channels = img1.shape
    
    #It takes the dimensions of every single photo.
    #So it is compatible with all dimensions.
    height1 = (height*0)/6
    height2 = (height*2)/6
    height3 = (height*4)/6
    height4 = (height*6)/6

    width1 = (width*0)/6
    width2 = (width*2)/6
    width3 = (width*4)/6
    width4 = (width*6)/6

    #cropping image into pieces.
    cropped_image1 = img1[int(height1):int(height2), int(width1):int(width2)]
    cropped_image2 = img1[int(height2):int(height3), int(width1):int(width2)]
    cropped_image3 = img1[int(height3):int(height4), int(width1):int(width2)]
    cropped_image4 = img1[int(height1):int(height2), int(width2):int(width3)]
    cropped_image5 = img1[int(height1):int(height2), int(width3):int(width4)]
    cropped_image6 = img1[int(height3):int(height4), int(width2):int(width3)]
    cropped_image7 = img1[int(height3):int(height4), int(width3):int(width4)]
    cropped_image8 = img1[int(height2):int(height3), int(width3):int(width4)]
    cropped_image9 = img1[int(height2):int(height3), int(width2):int(width3)]

    cv2.imshow("cropped1", cropped_image1)
    cv2.imshow("cropped2", cropped_image2)
    cv2.imshow("cropped3", cropped_image3)
    cv2.imshow("cropped4", cropped_image4)
    cv2.imshow("cropped5", cropped_image5)
    cv2.imshow("cropped6", cropped_image6)
    cv2.imshow("cropped7", cropped_image7)
    cv2.imshow("cropped8", cropped_image8)
    cv2.imshow("cropped9", cropped_image9)
    
    file_name = os.path.splitext(img)[0]
    
    cv2.imwrite(file_name+"-1.jpg", cropped_image1)
    cv2.imwrite(file_name+"-2.jpg", cropped_image2)
    cv2.imwrite(file_name+"-3.jpg", cropped_image3)
    cv2.imwrite(file_name+"-4.jpg", cropped_image4)
    cv2.imwrite(file_name+"-5.jpg", cropped_image5)
    cv2.imwrite(file_name+"-6.jpg", cropped_image6)
    cv2.imwrite(file_name+"-7.jpg", cropped_image7)
    cv2.imwrite(file_name+"-8.jpg", cropped_image8)
    cv2.imwrite(file_name+"-9.jpg", cropped_image9)
    
for imgs in os.listdir("./"):
    photocutter(imgs)