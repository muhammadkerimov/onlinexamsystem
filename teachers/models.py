from django.db import models

# Create your models here.




class Teacher_Data(models.Model):
    teacher_name = models.CharField(max_length=255)
    teacher_lname = models.CharField(max_length=255)
    teacher_lesson = models.CharField(max_length=20)
    teacher_id = models.CharField(max_length=10)
    teacher_password = models.CharField(max_length=10)
    def __str__(self): 
        return self.teacher_name , self.teacher_lname , self.teacher_id 

class Exam_Dat(models.Model):
    exam_name = models.CharField(max_length=255)
    exam_time = models.DateTimeField(max_length=255)
    exam_quescount = models.BigIntegerField()
    exam_grade = models.SmallIntegerField()
    exam_end = models.DateTimeField(max_length=255)
    questions = models.CharField(max_length=255)
    participated_childrens = models.CharField(max_length=10000,default='')

    
    def add_participant(self, username):
        # Check if the username is not already in the participants list
        if username not in self.participated_childrens.split(';'):
            # Add the username to the list (comma-separated values)
            if self.participated_childrens:
                self.participated_childrens += username + ';' 
            else:
                self.participated_childrens = username

            # Save the model instance
            self.save()

class Grammar_Bank(models.Model):
    TYPE_CHOICES =(
("Noun","The Noun"),
("Pronoun","Pronoun"),
("article","Article"),
("So do i","So do I"),
("Quantifiers","Quantifiers"),
("Tenses","Tense Forms"),
("Passive","Passive Voice"),
("Modal","Modal Verbs"),
)
    TYPETEST_CHOICES =(
        ("open","Açıq"),
        ("close","Qapalı")
    )
    question = models.TextField()
    question_topic = models.CharField(choices=TYPE_CHOICES,max_length=40)
    question_c1 =models.TextField()
    question_c2= models.TextField()
    question_c3 = models.TextField()
    question_c4 = models.TextField()
    question_c5 = models.TextField()
    correct_ans = models.TextField()
    question_id = models.CharField(max_length=255)
    question_type = models.CharField(max_length=255)
