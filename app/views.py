from django.shortcuts import render
from django.http import HttpResponse
from app.models import Picture
from faceai_web.settings import BASE_DIR
from app.faceget import faceClass
import threading
import os
face = faceClass()

def index(request):
    images = Picture.objects.all().order_by('-id')
    return render(request, "index.html", {'images':images})

def search(request):
    search = request.GET['s']
    images = Picture.objects.filter(title__contains=search)
    return render(request, "index.html", {'images':images,'search': search})

def getimg(request,page):
    pagenumber = ((int(page)-1)*20)+1
    images = Picture.objects.all().order_by('-id')[pagenumber:int(page)*20]
    img={'title':'','filename':''}
    json_text=""
    for image in images:
        img['filename'] = image.filename
        img['title'] = image.title
        json_text += str(img).replace("'",'"')+","
    jsondata = '{"data":[%s]}' % json_text[:-1]
    return HttpResponse(str(jsondata))

def upload_ajax(request):
    if request.method == 'POST':
        file_obj = request.FILES.get('file')
        f = open(os.path.join(BASE_DIR, 'app/static', 'images', file_obj.name), 'wb')
        for chunk in file_obj.chunks():
            f.write(chunk)
        f.close()
        faceai(os.path.join(BASE_DIR, 'app/static', 'images'), file_obj.name)
        return HttpResponse('OK')

def faceai(filepath, filename):
    def _start():
        if face.faceai(filepath+"/"+filename):
            p = Picture(filename=filename, title="default", haveher=True, good=0)
            p.save()
            print("Upload Picture")
    
    getThread = threading.Thread(target=_start)
    getThread.setDaemon(True)
    getThread.start()