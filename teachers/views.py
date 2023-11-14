from django.shortcuts import render , redirect 
from django.contrib import messages
import time , random
from django.http import HttpResponse 
from .models import Teacher_Data , Exam_Dat , Grammar_Bank
from students.models import UserReg
def login(request):
   time.sleep(1)
   if request.session.get('teacher_ad'):
      return redirect('mainteachers')
   if request.method == "POST":
      email = request.POST['teacherid']
      peassword = request.POST['teacherpassword']
      if Teacher_Data.objects.filter(teacher_id=email,teacher_password=peassword):
         userdata =Teacher_Data.objects.filter(teacher_id=email,teacher_password=peassword).values_list('teacher_name')
         request.session['teacher_ad'] = userdata[0]
         return redirect('mainteachers')
      else:
         messages.error(request,"İstifadəçi Tapılmadı")
         return redirect('loginteachers')
   return render(request,"teacherlogin.html")

def logoutt(request):
   request.session.flush()
   return redirect('loginteachers')

def mainteacher(request):
   if request.session.get('teacher_ad'):
    return render(request,"teachermainpage.html")
   else:
      request.session.flush()
      messages.error(request,'Zəhmət Olmasa Giriş Edin')
      return redirect('loginteachers')
   

def studentspage(request):
 if request.session.get('teacher_ad'):
   a = UserReg.objects.all().values()
   context = {
      'users' : a
   }
   return render(request,'teacherstudentspage.html',context)
 else:
      request.session.flush()
      messages.error(request,'Zəhmət Olmasa Giriş Edin')
      return redirect('loginteachers')

def deletestudent(request):
 if request.session.get('teacher_ad'):
   if request.method == "POST" and request.POST.get('examdelete'):
      name = request.POST['examdelete']
      Exam_Dat.objects.filter(exam_name=name).delete()
      messages.success(request,"Uğurla Silindi!")
      return redirect('teachersexams')
   elif request.method == "POST" and request.POST.get('deletestudent'):
      sagirdmail = request.POST['deletestudent']
      UserReg.objects.filter(mail=sagirdmail).delete()
      messages.success(request,"Uğurla Silindi!")
      return redirect('students')
 else:
   request.session.flush()
   messages.error(request,'Zəhmət Olmasa Giriş Edin')
   return redirect('loginteachers')
   

def addexam(request):
 if request.session.get('teacher_ad'):
   
   
   if request.method == "POST":
      questiontopics = Grammar_Bank.TYPE_CHOICES
      topiccon = len(questiontopics)
      questionlist = ""
      checksay = True
      quescon = 0
      count = request.POST['count']
      while quescon < int(count):
        random_index = random.randint(0, topiccon - 1)
        selected_topic = questiontopics[random_index][0]
        questions = Grammar_Bank.objects.filter(question_topic=selected_topic).values()
        lenof = len(questions)

        if lenof == 0:
         continue

        for numver in range(lenof):
         if questions[numver]['question_id'] not in questionlist:
            if quescon==7:
               questionlist += str(questions[numver]['question_id'])
               quescon += 1
               if numver == lenof - 1:
                 break 
            questionlist += str(questions[numver]['question_id']) + ','
            quescon += 1
            if numver == lenof - 1:
                break  # Exit the loop after adding a question to the list
          
      
      name = request.POST['name']
      time = request.POST['time']
      endtime = request.POST['endtime']
      grade = request.POST['grade']
      duration = request.POST['duration']
      a = Exam_Dat(
        exam_name=name,
        exam_time=time,
        exam_quescount=count,
        exam_grade=grade,
        exam_end = endtime,
        questions = questionlist
        )
      a.save()
      messages.success(request,"Uğurla Əlavə Olundu")
      redirect('teachersexams')
   user_data = Exam_Dat.objects.all().values()
   context = {
      'datas' : user_data
   }
   return render(request,"addexam.html",context)
 else:
   request.session.flush()
   messages.error(request,'Zəhmət Olmasa Giriş Edin')
   return redirect('loginteachers')

def addquestion(request):
  if request.session.get('teacher_ad'):
    if request.method == "POST":
      ques = request.POST['question']
      if request.POST['type']=='open':
        
        quesid = random.randint(1000,100000)
        new1 = Grammar_Bank(
          question=ques,
          question_topic = request.POST['topic'],
          correct_ans = request.POST['correcto'],
          question_id = quesid,
          question_type = "open"
                     )
        new1.save()
        messages.success(request,"Uğurla Əlavə Olundu")
      elif request.POST['type'] == 'close':
        quesid = random.randint(1000,100000)
        new2 = Grammar_Bank(
          question=ques,
          question_topic=request.POST['topic'],
          question_c1=request.POST['choice1'],
          question_c2=request.POST['choice2'],
          question_c3=request.POST['choice3'],
          question_c4=request.POST['choice4'],
          question_c5=request.POST['choice5'],
          correct_ans=request.POST['correctc'],
          question_id = quesid,
          question_type = "close"
                     )
        new2.save()
        messages.success(request,"Uğurla Əlavə Olundu")
      return redirect('addquestion')
    topics = Grammar_Bank.TYPE_CHOICES
    context = {
      'topics' : topics
    }
    return render(request,"addquestion.html",context)
  else:
   request.session.flush()
   messages.error(request,'Zəhmət Olmasa Giriş Edin')
   return redirect('loginteachers')
  

def lookques(request):
  questions = Grammar_Bank.objects.all().values()
  context = {
    'questions': questions
  }
  return render(request,'questionbank.htm',context)


