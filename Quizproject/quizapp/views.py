from django.shortcuts import render,HttpResponseRedirect
from quizapp.models import QuizInfo,Choice,UserResponse
from quizapp.forms import RegisterForm,LoginForm,AddquestionForm,ChoicesFormset
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# home

def home(request):
    qi=QuizInfo.objects.all()
    return render(request,'quizapp/home.html',{'quizinfo':qi})

# Quiz Question
@login_required
def QuestionView(request,id):
    qi=QuizInfo.objects.get(id=id)
    ques=qi.questions.all()
    return render(request,'quizapp/question.html',{'ques':ques,'quiz':qi})

# quiz submit
def quiz_submit(request,id):
    if request.method=='POST':
         qi=QuizInfo.objects.get(id=id)
         ques=qi.questions.all()
         for question in ques:
           choice_id=request.POST.get(f"ques_{question.id}") 
           if choice_id:
               choice=Choice.objects.get(id=choice_id) 
               UserResponse.objects.create(quiz=qi,question=question,choice=choice)
           else:
               return HttpResponseRedirect('/result/')   
    return HttpResponseRedirect('/question/')
   



#SignUp form
def Register(request):
    if request.method=='POST':
     fm=RegisterForm(request.POST)
     if fm.is_valid():
         fm.save()
         fm=RegisterForm()
    else:
        fm=RegisterForm()     
    return render(request,"quizapp/register.html",{'form':fm}) 

# login views
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                username=fm.cleaned_data["username"]
                password=fm.cleaned_data["password"]
                user=authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    if user.is_superuser:
                     return HttpResponseRedirect('/admin_dashboard/')
                    else:
                        return HttpResponseRedirect('/user_dashboard/')
        else:
            fm=LoginForm()
        return render(request,'quizapp/login.html',{'form':fm})
    return HttpResponseRedirect('/user_dashboard/')

# dashboard
def user_dashboard(request):
    if request.user.is_authenticated:
     return render(request,'quizapp/user_dashboard.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')
    
def admin_dashboard(request):
    if request.user.is_authenticated:
     return render(request,'quizapp/admin_dashboard.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')    

# logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


# add question
def addquestion(request):
    fm=ChoicesFormset()
    return render(request,'quizapp/addquestion.html',{'form':fm})

def result(request):
    return render(request,'quizapp/result.html')