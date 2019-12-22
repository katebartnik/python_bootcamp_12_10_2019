"""bocian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

admin.site.site_header = "UMSRA Admin"
admin.site.site_title = "UMSRA Admin Portal"
admin.site.index_title = "Welcome to UMSRA Researcher Portal"


# Routing
from cars.views import hello_world
from maths.views import calculate, history, history_detail, do_math

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", hello_world),
    path("hello/<name>", hello_world),
    path("maths/", do_math),
    path("maths/<op>/<int:a>/<int:b>", calculate),
    path("maths/history", history),
    path("maths/history/<int:id>", history_detail)

    #path("hello/<int:name>", hello_world)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
