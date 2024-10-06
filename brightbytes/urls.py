from django.urls import path
from . import views

app_name = 'brightbytes'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('lessons/<course_id>', views.lessons, name='lessons'),
    path('lesson/<lesson_id>', views.lesson, name='lesson'),
    path('quiz/<quiz_id>', views.quiz, name='quiz'),
]