from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelChoiceField

class RegisterForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Password Confirm(again)',widget=forms.PasswordInput({'class':'form-control'}))
    class Meta:
        model=User
        fields=["username","email","first_name","last_name"]
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                 'email':forms.TextInput(attrs={'class':'form-control'}),
                 'first_name':forms.TextInput(attrs={'class':'form-control'}),
                 'last_name':forms.TextInput(attrs={'class':'form-control'}),}
        
class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))   
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))     
    
class MenuModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        # return "Menu #%s) %s" % (obj.id,obj.topic)
        return "%s" % (obj.topic)
        
class AddquestionForm(forms.ModelForm) :
    quiz = MenuModelChoiceField(queryset=QuizInfo.objects.all())
    class Meta:
        model=Question
        fields='__all__'
        
class ChoiceForm(forms.ModelForm) :
    class Meta:
        model=Choice
        fields='__all__'        
      
ChoicesFormset= forms.modelform_factory(
    Question, Choice, form=ChoiceForm,
    extra=1, can_delete=True, can_delete_extra=True
)      