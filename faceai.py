from faceai_web.settings import BASE_DIR
from app.faceget import faceClass
import os
import django
face = faceClass()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "faceai_web.settings")
django.setup()
IMAGE_DIR = os.path.join(BASE_DIR, 'app/static', 'images')
from app.models import Picture

def getPicture():
    pictures = Picture.objects.filter(show=False, read=False)
    if len(pictures)>0:
        print("Get %s Picture" % len(pictures))
    for p in pictures:
        if face.faceai("%s/%s" % (IMAGE_DIR, p.filename)):
            p.haveher = True
            p.show = True
            print("Id:%s is ycy" % p.id)
        else:
            p.title="other Picture"
            print("Id:%s not ycy" % p.id)
        p.read=True
        p.save()


if __name__ == "__main__":
    getPicture()