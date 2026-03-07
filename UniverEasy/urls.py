#from cgitb import handler

from django.conf.urls import handler404
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('univers-select/', views.Univers.as_view(), name='univers'),
    path('univer/<slug:univer_slug>/faculties/', views.UniverFaculties.as_view(), name='univer_facs'),
    path('faculty/<slug:faculty_slug>/file-works/', views.FacultiesFiles.as_view(), name='facs_files'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('success/', views.SuccessPage.as_view(), name='success_page'),
    path('upload/', views.UploadFileView.as_view(), name='upload'),
]


#handler404 =

















