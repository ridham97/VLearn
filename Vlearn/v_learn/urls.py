from django.urls import path
from v_learn import views

app_name = "templates"

urlpatterns = [
    path('', views.Homepage, name="homepage"),
    path('adminform', views.adminform, name="adminform"),
    path('adminformMCQ',views.adminformMCQ,name="adadminformMCQ"),
    path('content', views.Content, name="content"),
    path('detail', views.Detail, name="detail"),
    path('forgotpass', views.forgotpassword, name="forgotpass"),
    path('login', views.Login, name="login"),
    path('register', views.Register, name="register"),
    path('profile', views.Profile, name="profile"),
    path('get_data_for_topic/',views.Get_Data_topic,name="Get_Data_topic")
]
