from django.shortcuts import render
from django.http import HttpResponse
from django import forms 
from .models import UserReg , Children_Results
from django.contrib import messages
from django.shortcuts import redirect
import time
from datetime import datetime, time
import ast
from teachers.models import Exam_Dat,Grammar_Bank
def register(request):
    time.sleep(1)
    emails = []
    for i in 0,len(UserReg.objects.all())-1:
       a = UserReg.objects.all().values()[i]['mail']
       emails.append(a)
    if request.method == "POST":
     if request.POST['email'] in emails:
      messages.info(request,"You Already Have An Account")
      return redirect('register')
     
     new_user = UserReg(
        ad = request.POST['ad'],
        soyad = request.POST['soyad'],
        parent_name = request.POST['parent_name'],
        mail = request.POST['email'],
        password = request.POST['password']
     )
     new_user.save()
     return 
    class loginuser(forms.Form):
        ad = forms.CharField() 
        soyad = forms.CharField() 
        parent_name = forms.CharField() 
        email = forms.CharField() 
        password = forms.PasswordInput()
    
    context = {}
    context['form']=loginuser()
    return render(request,"register.html",context)


def login(request):
   time.sleep(1)
   if request.session.get('ad'):
      return redirect('main')
   if request.method == "POST":
      email = request.POST['email']
      peassword = request.POST['password']
      if UserReg.objects.filter(mail=email,password=peassword):
         userdata =UserReg.objects.filter(mail=email,password=peassword).values_list('ad','soyad','grade','mail','parent_name')
         request.session['ad'] = userdata[0][0]
         request.session['soyad'] = userdata[0][1]
         request.session['mail'] = userdata[0][3]
         request.session['sinif'] = userdata[0][2]
         request.session['valideyn'] = userdata[0][4]
         return redirect('main')
      else:
         messages1.error(request,"İstifadəçi Tapılmadı")
         return redirect('login')
   return render(request,"login.html")  



def main(request):
   return render(request,'main.htm')

def exams(request):
   doesexamstart = True
   if (len(Exam_Dat.objects.all().filter(exam_grade=request.session.get('sinif')).values())>0):
      data =  Exam_Dat.objects.all().filter(exam_grade=int(request.session.get('sinif'))).values()
      context  = {
         'now':datetime.now(),
         'exams':data
      }
      return render(request,"exams.html",context)
   else:
      context ={
         
      }
      return render(request,"exams.html")

   

def logout(request):
   request.session.flush()
   return redirect('login')


def examstart(request):
   if request.method == "POST" and request.POST.get('end'):
      questions = Exam_Dat.objects.all().filter(exam_name=request.session.get('examname')).values()[0]['questions']
      questions = questions.split(',')
      quescon = len(questions)
      quescon = str(quescon)
      list = []
      answersofchild = []
      correct_answers = []
      for question in questions:
        ans_of_child = request.POST[question]
        res = ans_of_child 
        if len(res)>1:
           answersofchild.append('⏳')
           correct_answers.append('1')
           continue
        answersofchild.append(res)
        
        corr_ans = Grammar_Bank.objects.all().filter(question_id=question).values()[0]['correct_ans']
        if ans_of_child == corr_ans:
           list.append('+')
           correct_answers.append(corr_ans)
        else:
           list.append('-')
           correct_answers.append(corr_ans)
         
      correctcon = list.count('+')
      wrongcon = list.count('-')
      newrec = Children_Results(
          child_name = request.session.get('ad'),
          child_surname = request.session.get('soyad'),
          child_parentname = request.session.get('valideyn'),
          child_grade = request.session.get('sinif'),
          child_email = request.session.get('mail'),
          child_corrects = correctcon,
          child_wrongs = wrongcon,
          child_answers = answersofchild,
          child_correctornot = list,
          correct_answersoftest = correct_answers,
          child_quescount = quescon
      )
      newrec.save()
      username = request.session.get('mail') + ';'
      exam = Exam_Dat.objects.get(exam_name=request.session.get('examname'))
      exam.add_participant(username=username)
      return redirect('result')
   elif request.method == "POST" and request.POST.get('start'):
      exam = Exam_Dat.objects.all().filter(exam_name=request.POST['start']).values_list('participated_childrens')
      exam = exam[0][0]
      exam = exam.split(';')
      if request.session.get('mail') in exam:
         messages.warning(request,"Siz Bu imtahanda iştirak Etmişsiniz!")
         return redirect('exams')
      examad = request.POST['start']
      request.session['examname']=examad
      questions = Exam_Dat.objects.all().filter(exam_name=examad).values()[0]['questions']
      questions = questions.split(',')
     
      listques = []
      for questionid in questions:
           new = Grammar_Bank.objects.all().filter(question_id=questionid).values()
           listques.append(new)
      examstart = Exam_Dat.objects.all().filter(exam_name=examad).values()[0]['exam_time']
      examend = Exam_Dat.objects.all().filter(exam_name=examad).values()[0]['exam_end']
      examend_without_timezone = examend.strftime('%Y-%m-%d %H:%M:%S')
      context = {
         'questions':listques,
         'examstart':examstart,
         'examend':examend_without_timezone
      }
   return render(request,"examstart.html",context)


def result(request):
   dataresults = Children_Results.objects.all().filter(child_email=request.session.get('mail')).values()
   context = {
      'quescon':dataresults[0]['child_quescount'],
      'answers':ast.literal_eval(dataresults[0]['child_answers']),
      'corrects':dataresults[0]['child_corrects'],
      'wrongs':dataresults[0]['child_wrongs'],
      'correctanswers':ast.literal_eval(dataresults[0]['correct_answersoftest']),
      'correctornots':ast.literal_eval(dataresults[0]['child_correctornot'])
   }
   request.session['examname']=''
   return render(request,'results.html',context)