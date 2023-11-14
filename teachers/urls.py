from django.urls import path , include
from . import views
urlpatterns = [
    
    path('teachers/login',views.login,name='loginteachers'),
    path('teachers/main',views.mainteacher,name='mainteachers'),
    path('teachers/logout',views.logoutt,name='logoutt'),
    path('teachers/students',views.studentspage,name='students'),
    path('teachers/delete',views.deletestudent,name='delete'),
    path('teachers/exams',views.addexam,name='teachersexams'),
    path('teachers/addquestion',views.addquestion,name='addquestion'),
    path('teachers/questionbank',views.lookques,name='questionbank'),
]
