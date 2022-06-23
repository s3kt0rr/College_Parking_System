from datetime import datetime
from os import read
import cv2
import imutils
import numpy as np
import easyocr
import os
from tkinter import messagebox
import tkinter as tk


def capture_image_from_cam_into_temp():
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    cv2.namedWindow("test")

    # img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            if not os.path.isdir('temp'):
                os.mkdir('temp', mode=0o777)  # make sure the directory exists
            # img_name = "./temp/opencv_frame_{}.png".format(img_counter)
            img_name = "./temp/test_img.png"
            print('imwrite=', cv2.imwrite(filename=img_name, img=frame))
            print("{} written!".format(img_name))
            # img_counter += 1
    cam.release()
    cv2.destroyAllWindows()
    return True


def captureFace(ent):
    filename = os.getcwd()+'\\temp\\test_img.png'
    # messagebox.showinfo(
    #     'SUCCESS!!!', 'Press Space Bar to click picture and ESC to exit')
    res = None
    res = messagebox.askquestion(
        'Click Picture', 'Press Space Bar to click picture and ESC to exit')
    if res == 'yes':
        capture_image_from_cam_into_temp()
        ent.insert(tk.END, filename)
    return True


def getNumberPlateSting(image):
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bfilter = cv2.bilateralFilter(gray, 11, 17, 17)  # noise removal
    edged = cv2.Canny(bfilter, 30, 200)  # edge detection
    keypoints = cv2.findContours(
        edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    location = None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if(len(approx) == 4):
            location = approx
            break
    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [location], 0, 255, -1)
    new_image = cv2.bitwise_and(img, img, mask=mask)
    (x, y) = np.where(mask == 255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))
    cropped_image = gray[x1:x2+1, y1:y2+1]
    reader = easyocr.Reader(['en'])
    result = reader.readtext(cropped_image)
    text = result[0][-2]
    return text


# function accepts two timestamps and returns the hr difference
def find_hr_diff(start_time, end_time):
    if(type(start_time) == str):
        print('is_string')
    duration = end_time - start_time
    duration_in_s = duration.total_seconds()
    hours = max(divmod(duration_in_s, 3600)[0], 1)
    return hours

'''
# function to accept start,end time and base charge and computes total charge
def save_to_database(outtime=outtime):

    #time_parked = find_hr_diff(start_time=start_time, end_time=end_time)
    #total_charges = time_parked*base_charge
    return (time_parked, base_name,pov) 


then = datetime(2012, 3, 5, 23, 8, 15)
now = datetime.now()
'''
# print(calculate_charges(then, now))
# print('1', getNumberPlateSting('1.jpg'))
# print('2', getNumberPlateSting('2.jfif'))
# print('3', getNumberPlateSting('3.jfif'))
# print('4', getNumberPlateSting('4.jfif'))
# print('5', getNumberPlateSting('5.jpeg'))
