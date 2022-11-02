from os import name
from django.urls import include, path 
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path('contact',views.contact,name="contact"),
    path('flex',views.flex,name="flex"),
    path('book',views.book,name="book"),
    path('test',views.test,name="test"),
    path('profile',views.profile,name="profile"),
    path('result',views.result,name='result'),
    path('studentperform',views.studentperform,name='studentperform'),
    path('atten',views.atten,name='atten'),
    path('attendance',views.attendance,name="attendance"),
    path('viewattendance',views.viewattendance,name="viewattendance"),
    path('teacher',views.teacher,name="teacher"),
    path('fees',views.fees,name="fees"),
    path('notice',views.notice,name="notice"),
    path('viewprofile',views.viewprofile,name="viewprofile"),
    path("Login",views.Login, name='Login'),
    path("Signup",views.Signup, name='Signup'),
    path("Forget",views.Forget, name='Forget'),
    path("accounts/",include("django.contrib.auth.urls")),
    path("Dashboard",views.Dashboard,name="Dashboard"),
    path("Calender",views.Calender,name="Calender"),
    path("Quiz",views.Quiz,name="Quiz"),
    path("logout",views.handlelogout,name="logout"),
    path('view_score', views.view_score, name="view_score"),
    path('api/check_score' , views.check_score, name="check_score"),
    path('<id>', views.take_quiz , name="take_quiz"),
    path('api/<id>', views.api_question, name="api_question"),

    
    
    
]

