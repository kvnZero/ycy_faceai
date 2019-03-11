import cv2
import face_recognition
import os
from random import randint
from PIL import Image

def signImage(model_name, images_path):
    filesname = os.listdir(images_path)
    for filed in filesname:
        print(filed)
        filepath = images_path + "/" + filed
        frame = cv2.imread(filepath)
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        for (top, right, bottom, left), face_encoding in zip(
                face_locations, face_encodings):
            testImg = frame[top:bottom, left:right]
            i = randint(10000, 99999)
            savefilename = '%s/%s_%s.jpg' % (os.path.join(os.path.dirname(os.path.abspath(__name__)),'app/static/test','ycy'), model_name, i)
            cv2.imwrite(savefilename, testImg, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
            img = Image.open(savefilename)
            img.show()

            isface = input("图内脸是否是杨超越(1是,其他不是/跳过)：")
            if isface == "1":
                cutImage("ycy",filepath,left,top,right,bottom)

def cutImage(model_name, filepath, left,top,right,bottom):
    frame = cv2.imread(filepath)
    frame = frame[top:bottom, left:right]
    i = randint(10000, 99999)
    cv2.imwrite('%s/%s_%s.jpg' % (os.path.join(os.path.dirname(os.path.abspath(__name__)),'app/static/faces','ycy'), model_name, i), frame, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])

signImage("ycy","app/static/images")