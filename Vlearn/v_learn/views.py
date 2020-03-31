from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
from django.conf import settings 

# Create your views here.
from django.http import HttpResponse
from v_learn.models import Course, Topic, Mcq


def Detail(request):
    return render(request, "Detail.html")


def Content(request):
    return render(request, "Content.html")


def forgotpassword(request):
    return render(request, "forgot-password.html")


def Login(request):
    return render(request, "Login.html")


def Profile(request):
    return render(request, "Profile.html")


def Register(request):
    return render(request, "register.html")


# def vfaq(request):
#     return render(request, "v-faq.html")


def vmodule(request):
    with open(os.path.join(settings.BASE_DIR,'templates/v-module.html'),"r") as f:
        data = f.read()
        topic_content = Topic.objects.all()
        topic_content = {"topic_content":topic_content}
        return HttpResponse(data)


def vquiz(request):
    with open(os.path.join(settings.BASE_DIR,'templates/v-quiz.html'),"r") as f:
        data = f.read()
        return HttpResponse(data)


def vsimulator(request):
   with open(os.path.join(settings.BASE_DIR,'templates/v-simulator.html'),"r") as f:
        data = f.read()
        return HttpResponse(data)


def vvideotopic(request):
    with open(os.path.join(settings.BASE_DIR,'templates/v-video_topic.html'),"r") as f:
        data = f.read()
        return HttpResponse(data)


def Homepage(request):
    course_table = Course.objects.order_by('course_name')
    my_course_table = {"insert_course_table": course_table}
    return render(request, "Homepage.html", context=my_course_table)

def Content(request):
    topic_list = Topic.objects.all()
    topic_list = {"topic_list":topic_list}
    return render(request,"Content.html",context=topic_list)

def Detail(request):
    topic_list = Topic.objects.all()
    topic_list = {"topic_list":topic_list}
    return render(request,"Detail.html",context=topic_list)        


def adminform(request):
    topic_data = Course.objects.all()
    topic_list = {"insetTopicData": topic_data}

    coursename = request.POST.get("course_name")
    topicValue = request.POST.get("TopicValue")
    contentValue = request.POST.get("ContentValue")
    save_data = Topic(course_name_id=coursename, topic=topicValue,content=contentValue)
    save_data.save()
    return render(request, "admin.html", context=topic_list)
