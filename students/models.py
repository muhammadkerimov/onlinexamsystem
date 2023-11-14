from django.db import models
class UserReg(models.Model):
    ad = models.CharField(max_length=255)
    soyad = models.CharField(max_length=255)
    parent_name = models.CharField(max_length=255)
    mail = models.EmailField()
    password = models.CharField(max_length=20)
    grade = models.IntegerField()
    def __str__(self): 
        return self.ad , self.parent_name , self.mail 
    
class Children_Results(models.Model):
    child_name = models.CharField(max_length=255)
    child_surname = models.CharField(max_length=255)
    child_parentname = models.CharField(max_length=255)
    child_grade = models.CharField(max_length=255)
    child_email = models.CharField(max_length=255)
    child_corrects = models.CharField(max_length=255)
    child_wrongs = models.CharField(max_length=255)
    child_answers = models.CharField(max_length=1000)
    child_correctornot = models.CharField(max_length=1000)
    correct_answersoftest = models.CharField(max_length=1000)
    child_quescount = models.CharField(max_length=255)