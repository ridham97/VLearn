from django.urls import path
from v_learn import views

app_name = "templates"

urlpatterns = [
    path('', views.Homepage, name="homepage"),
    path('adminform', views.adminform, name="adminform"),
    path('content', views.Content, name="content"),
    path('detail', views.Detail, name="detail"),
    path('forgotpass', views.forgotpassword, name="forgotpass"),
    path('login', views.Login, name="login"),
    path('register', views.Register, name="register"),
    path('profile', views.Profile, name="profile"),
    path('templates/v-module.html/',views.vmodule,name="vmodule"),
    path('templates/v-simulator.html/',views.vsimulator,name="vsimulator"),
    path('templates/v-quiz.html/',views.vquiz,name="vquiz"),
    path('templates/v-video_topic.html/',views.vvideotopic,name="vvideotopic")
]
