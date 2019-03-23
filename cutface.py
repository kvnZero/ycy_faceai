import cv2
import face_recognition
import os
from random import randint
from PIL import Image
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "faceai_web.settings")
django.setup()
from app.models import Face

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
            savefilename = '%s_%s.jpg' % (model_name, i)
            filename = '%s/%s' % (os.path.join(os.path.dirname(os.path.abspath(__name__)),'app/static/test'),savefilename)
            cv2.imwrite(filename, testImg, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
            img = Image.open(filename)
            img.show()

            isface = input("图内脸是否是杨超越(1是,其他不是/跳过)：")
            if isface == "1":
                cutImage(filed,"ycy",filepath,left,top,right,bottom)

def getface(images_path):
    filesname = os.listdir(images_path)
    for filed in filesname:
        filepath = images_path + "/" + filed
        frame = cv2.imread(filepath)
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        for (top, right, bottom, left), face_encoding in zip(
                face_locations, face_encodings):
            cutImage(filed,"ycy",filepath,left,top,right,bottom)


def saveFace(picturefile,facefile):
    face = Face(picturefile=picturefile, facefile=facefile)
    face.save()

def cutImage(oldfile,model_name, filepath, left,top,right,bottom):
    frame = cv2.imread(filepath)
    frame = frame[top:bottom, left:right]
    i = randint(10000, 99999)
    filename = '%s_%s.jpg' % ( model_name, i)
    cv2.imwrite('%s/%s' % (os.path.join(os.path.dirname(os.path.abspath(__name__)),'static/test'),filename), frame, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
    saveFace(oldfile,filename)

#getface("app/static/images/ycy")