"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from . import views
from .views import postdelete,orderbylikes,orderbydislikes,orderbytitle,orderbyauthor,likebtn,dislikebtn
app_name="mysite"
urlpatterns = [

    url(r'^home/$',views.index,name='index'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^submitguide/$',views.submitguide,name='submitguide'),
    url(r'^(?P<id>\d+)/delete$',postdelete,name='deletepost'),
    url(r'^(?P<id>\d+)/liked$',likebtn,name='likebtn'),
    url(r'^(?P<id>\d+)/disliked$',dislikebtn,name='dislikebtn'),
    url(r'^orderbylikes/$',orderbylikes,name='orderbylikes'),
    url(r'^orderbytitle/$',orderbytitle,name='orderbytitle'),
    url(r'^orderbyauthor/$',orderbyauthor,name='orderbyauthor'),
    url(r'^orderbydislikes/$',orderbydislikes,name='orderbydislikes'),
]

