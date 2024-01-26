from django.urls import path 
from .import views

urlpatterns = [
    path("",views.home,name="home"),
    path("Question<int:id>/",views.QuestionView,name="question"),
    path('submit<int:id>/',views.quiz_submit,name="submit"),
    path('result/',views.result,name="result"),
    
    
    
    path("register/",views.Register,name="signup"),
    path("login/",views.user_login,name="login"),
    path("user_dashboard/",views.user_dashboard,name="user_dashboard"),
    path("admin_dashboard/",views.admin_dashboard,name="admin_dashboard"),
    path("logout/",views.user_logout,name="logout"),
    
    
    
    path("addquestion/",views.addquestion,name="addquestion"),
]
