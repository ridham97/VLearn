from django.urls import path
from v_learn import views


urlpatterns = [
  path('',views.index,name="index"),
]