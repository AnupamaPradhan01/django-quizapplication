from django.db import models

# Quiz Info
class QuizInfo(models.Model):
    topic=models.CharField(max_length=100)
    desc=models.CharField(max_length=200)
   
    
    
class Question(models.Model):
    question=models.CharField(max_length=220)
    quiz=models.ForeignKey(QuizInfo,on_delete=models.CASCADE,related_name="questions")  

    
class Choice(models.Model):
    text=models.CharField(max_length=220)
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name="choices")
    score=models.FloatField(default=0)
    
class AnsCheck(models.Model):
    choice=models.ForeignKey(Choice,on_delete=models.CASCADE)
    quiz=models.ForeignKey(QuizInfo,on_delete=models.CASCADE)  
    question=models.ForeignKey(Question,on_delete=models.CASCADE)    
    
class UserResponse(models.Model):
    quiz=models.ForeignKey(QuizInfo,on_delete=models.CASCADE,default=None)  
    question=models.ForeignKey(Question,on_delete=models.CASCADE,default=None)  
    choice=models.ForeignKey(Choice,on_delete=models.CASCADE,default=None)     
  
    
