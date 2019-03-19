from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models import Picture, User, Face
from faceai_web.settings import BASE_DIR, FACE_IMAGE, FACE_TEST_IMAGE
import threading
import os
import shutil
import random

def index(request):
    images = Picture.objects.filter(haveher=True,read=True,show=True).order_by('-time')
    if request.method=="POST":
        if request.POST['username']:
            username = request.POST['username']
            if request.POST['password']:
                password = request.POST['password']
                user = User.objects.filter(username=username, password=password).first()
                if user:
                    request.session['username']= user.username
                    request.session['id']=user.id
    try:
        return render(request, "main.html", {'images': images, 'username': request.session.get('username')})
    except KeyError:
        return render(request, "main.html", {'images':images})

def lgout(request):
    del request.session['username']
    del request.session['id']
    return redirect('/')

def check(request):
    if request.method=="POST":
        if request.POST['showid']:
            showid = request.POST['showid']
            if request.POST['value']:
                value = request.POST['value']
                face = Face.objects.filter(id=showid).first()
                if value=='1':
                    face.t_number = face.t_number+1
                elif value=='0':
                    face.f_number = face.f_number + 1
                allinput = face.t_number+face.f_number
                if allinput>10 and face.t_number/allinput>0.8:
                    #当人工识别率达到80%的情况为人脸
                    copyface(face.facefile)
                    face.show = True
                face.save()
                return redirect('/check/')
    getface = Face.objects.filter(show=False).order_by('?')[0]
    try:
        return render(request, "check.html", {'face': getface, 'username': request.session.get('username')})
    except KeyError:
        return render(request, "check.html", {'face': getface})

def copyface(faceimg):
    #复制到人脸样本目录
    def _start():
        shutil.copyfile(FACE_TEST_IMAGE+'/%s' % faceimg, FACE_IMAGE+'/%s' % faceimg)
    getThread = threading.Thread(target=_start)
    getThread.setDaemon(True)
    getThread.start()

def search(request):
    search = request.GET['s']
    images = Picture.objects.filter(title__contains=search)
    return render(request, "index.html", {'images':images,'search': search})

def getimg(request,page):
    pagenumber = ((int(page)-1)*20)+1
    images = Picture.objects.filter(haveher=True,read=True,show=True).order_by('-id')[pagenumber:int(page)*20]
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
        if not request.session.get('id'):
            return HttpResponse("请先登录后再上传")
        file_obj = request.FILES.get('file')
        type_list = ['.jpg', '.png']
        if os.path.splitext(file_obj.name)[1].lower() in type_list:
            savename = "%s_im_%s" % (random.randint(10000,99999),file_obj.name)
            f = open(os.path.join(BASE_DIR, 'app/static', 'images', savename), 'wb')
            for chunk in file_obj.chunks():
                f.write(chunk)
            f.close()
            user = User.objects.get(id=request.session.get('id'))
            p = Picture(user=user, filename=savename, title="default", haveher=False, good=0, show=False)
            p.save()
            return HttpResponse('OK')
        return HttpResponse("错误上传类型")

