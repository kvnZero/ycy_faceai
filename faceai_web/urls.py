"""faceai_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import index, upload_ajax, check, lgout
from app.views import good_show, feed_show, random_show
from django.conf.urls.static import static
from faceai_web import settings

urlpatterns = [
    path('', index),
    path('check/', check),
    path('lgout/', lgout),

    path('admin/', admin.site.urls),

    path('upload_ajax/', upload_ajax),

    path('list/good', good_show),
    path('list/feed', feed_show),
    path('list/random', random_show),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
