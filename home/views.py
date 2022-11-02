import json
from django.conf import settings
from django.shortcuts import redirect, render,HttpResponse
#from home.models import Register
from django.contrib.auth.models import User

from django.contrib import admin, messages
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.http import JsonResponse, response
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.decorators import login_required
import os
from django.http import HttpResponse
from datetime import datetime
import pandas as pd
import numpy as np
import warnings
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 

#from studenterp.home.models import Course

# Create your views here.
def index (request):
    return render(request,'flex.htm')
    #return HttpResponse("this home page")

def studentperform (request):
    return render(request,'performance.htm')
linear = pd.read_pickle(r"./models/model1.pickle")
def result(request):
    print(request)
    if request.method == 'POST':
        temp = []
       
        a=float(28) 
        b=float(request.POST.get('Exam1'))
        c=float(request.POST.get('Exam2'))
        d=float(request.POST.get('studytime'))
        e=float(request.POST.get('freetime'))
        f=float(request.POST.get('traveltime'))
        g=float(request.POST.get('health'))
        h = float(3)
        i = float(4) 
        j = float(1) 
#    data2 = df[['absences', 'G1', 'G2','studytime', 'freetime', 'traveltime', 'failures','health','Medu','Fedu']]
    
    # [9.26470664] [ 6  8 10  2  4  1  0  4  2  3] [10]
    # [8.99847659] [28 10  9  3  4  1  1  5  3  4] [9]
    # [5.16980173] [4 7 6 2 3 1 0 2 3 1] [6]
    # [8.71262776] [ 4 10  9  2  4  1  0  5  2  2] [11]
    # temp=[28 ,10,  9,  3,  4,  1,  1,  5,  3,  4]
    temp = [a,b,c,d,e,f,j,g,h,i]
    predictions = linear.predict([temp])
    print(temp) 
   
    data = {'Sem1':b, 'Sem2':c, 'sem3':predictions,}
    courses = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize = (10, 5))

# creating the bar plot
    plt.bar(courses, values, color ='#87CEEB',width = 0.4)

    plt.xlabel("No. of sem")
    plt.ylabel("Pointer")
    plt.ylim([1, 10])


    plt.savefig('static/images/chart.jpg')

    predictions = linear.predict([temp])
    context ={
        'score': round(float(predictions),2),
        'percent':round(float(predictions*9.5),2)
        
    }
    return render(request,'result.htm',context)

def Login (request):
    if request.method == "POST":
        logingrno = request.POST['logingrno']
        loginpass = request.POST['loginpass']

        user = authenticate(username=logingrno,password=loginpass)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Login")
            return redirect ('Dashboard')
        else:
            messages.error(request,"Invalid USer")
            return redirect('Login')
    else:    
        return render(request,'Login.htm')

def Signup (request):
    
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        grno = request.POST['grno']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if User.objects.filter(username = grno).first():
            messages.success(request, "This username is already taken")
            return redirect('Signup')
        else:
            myuser = User.objects.create_user(grno,email,password)
            myuser.first_name=fname
            myuser.last_name=lname
            myuser.save()  
            messages.success(request,"Registration Successfully")
            return redirect ('Login')
    else:
        return render(request,'Signup.htm')
    
def handlelogout (request):
    logout(request)
    messages.success(request,"LOGOUT")
    return redirect('/')

def Forget (request):
    if request.method == "POST":
        f_gr = request.POST.get('f_gr')
        f_pass = request.POST.get('f_pass')
        u = User.objects.get(username=f_gr)
        u.set_password(f_pass)
        u.save()
        messages.success(request,"Password reset Successfully")
        return redirect ('Login')
    return render(request,'Forget.htm')

@login_required(login_url='/Login')
def Dashboard (request):
    return render(request,'dash.htm')

def Calender (request):
    return render(request,'Calender.htm')
    
def Quiz (request):
    courses = Course.objects.all()
    
    context = {'courses':courses}
    return render(request,'Quiz.htm',context)

@login_required(login_url='/Login')
def view_score(request):
    user = request.user
    score = ScoreBoard.objects.filter(user=user)
    context={'score': score}
    return render(request,'score.htm', context)

@login_required(login_url='/Login')
def take_quiz (request,id):
    context = {'id':id}
    return render (request,'test.htm',context)

@csrf_exempt
def check_score(request):
    data = json.loads(request.body)
    user = request.user
    course_id = data.get('course_id')
    solutions = json.loads(data.get('data'))
    course = Course.objects.get(id=course_id)
    score = 0
    for solution in solutions:
        question = Question.objects.filter(id = solution.get('question_id')).first()
        if (question.answer) == solution.get('option'):
            score = score + question.marks

    score_board = ScoreBoard(course = course, score = score, user = user)
    score_board.save()
    return JsonResponse({'message' : 'success' , 'status':True})

def api_question (request,id):
    raw_questions = Question.objects.filter(course = id)[:20]
    questions = []

    for raw_question in raw_questions:
        question={}
        question['id'] = raw_question.id
        question['question'] = raw_question.question
        question['answer'] = raw_question.answer
        question['marks'] = raw_question.marks

        options = []

        options.append(raw_question.option_1)
        options.append(raw_question.option_2)
        if raw_question.option_3 != '':
            options.append(raw_question.option_3)
        if raw_question.option_4 != '':
            options.append(raw_question.option_4)

        question['options'] = options

        questions.append(question)

    return JsonResponse(questions, safe=False)

def flex(request):
    return render(request,'flex.htm')

@login_required(login_url='/Login')
def book(request):
    context = {'file':FilesAdmin.objects.all()}
    return render(request,'book.htm',context)

@login_required(login_url='/Login')
def notice(request):
    context = {'file':NotificationAdmin.objects.all()}
    return render(request,'notice.htm',context)

def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):        
        with open(file_path,'rb') as fh:
            response = HttpResponse(fh.read(),content_type="application/adminupload")
            response['Content-Disposition'] = 'inline;filename='+os.path.basename(file_path)
            return response

    
    else:
        return HttpResponse("this home page")

@login_required(login_url='/Login')
def profile(request):
    user = request.user
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        mobno = request.POST.get('mobno')
        address = request.POST.get('address')
        course = request.POST.get('course')
        classdiv = request.POST.get('classdiv')
        rollno = request.POST.get('rollno')  
        profile = TestProfile(user=user,fname=fname , lname=lname, email=email, mobno=mobno,address=address,course=course,classdiv=classdiv,rollno=rollno)
        profile.save()
        return redirect ('viewprofile')
    args = {'user':request.user}
    return render(request,'profile.htm',args) 



@login_required(login_url='/Login')
def viewprofile(request):
    user = request.user
    data = TestProfile.objects.filter(user=user)
    return render(request,'viewprofile.htm',{'data':data})

def attendance(request):
    user = request.user
    date = datetime.today()
    if request.method == "POST":
        attendance = Attendance(user=user,date=date)
        attendance.save()
    return render(request,'attendance.htm')
 
def viewattendance(request):
    user = request.user
    data = Attendance.objects.filter(user=user)
    return render(request,'viewattendance.htm',{'data':data})

@login_required(login_url='/Login')
def teacher(request):
    data = Lecture.objects.all()
    return render(request,'link.htm',{'data':data})
    
@login_required(login_url='/Login')
def fees(request):
    return render(request,'fees.htm')

def atten(request):

    data = Lecture.objects.all()
    return render(request,'at.htm',{'data':data})
    

def newdash(request):
    return render(request,'newdash')

@login_required(login_url='/Login')
def test(request):
    args = {'user':request.user}
    return render(request,'dash.htm',args)


def contact(request):
    if request.method == "POST":
        Fname = request.POST.get('Fname')
        Email = request.POST.get('Email')
        Sub = request.POST.get('Sub')
        Msg = request.POST.get('Msg')
        #print(Fname,Email,Sub,Msg)
        con = Feedback(Fname=Fname,Email=Email,Sub=Sub,Msg=Msg)
        con.save()
        return redirect('flex')
    return render(request,'flex.htm')




    



