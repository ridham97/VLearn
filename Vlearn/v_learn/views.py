from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
import os
from django.conf import settings 

# Create your views here.
from django.http import HttpResponse
from v_learn.models import Course, Topic, Mcq, VlearnUser


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
    # for input topic and content
    topic_data = Course.objects.all()
    topic_Course = {"topicCourse": topic_data}
    coursename = request.POST.get("course_name")
    topicValue = request.POST.get("TopicValue")
    contentValue = request.POST.get("ContentValue")
    save_data = Topic(course_name_id=coursename, topic=topicValue,content=contentValue)
    save_data.save()
    return render(request, "adminTopicContent.html", context=topic_Course)

def adminformMCQ(request):
    topic_data = Topic.objects.all()
    topic = {"topic": topic_data}

    course = request.POST.get("course")
    topic = request.POST.get("topic")
    que = request.POST.get("question")
    optA = request.POST.get("optA")
    optB = request.POST.get("optB")
    optC = request.POST.get("optC")
    optD = request.POST.get("optD")
    answer = request.POST.get("answer")
    save_mcq = Mcq(course_name_id=course,topic_id=topic,question=que,option_a=optA,option_b=optB,option_c=optC,option_d=optD,right_option=answer)
    save_mcq.save()
    return render(request, "adminMCQ.html", context=topic)

def Register(request):
    firstName = request.POST.get("first_name")
    lastName = request.POST.get("last_name")
    useremail = request.POST.get("email")
    save_data = VlearnUser(firstName=firstName,lastName=lastName,emailid=useremail,courseList=1,percentage=1)
    save_data.save()
    return render(request, "register.html")

def Get_Data_topic(request):
    id=request.GET['id']
    topic = Topic.objects.get(id=id)
    return JsonResponse({'name':topic.topic,
    'content':topic.content})

def Get_Data_mcq(request):
    id=request.GET['id']
    mcqs = Mcq.objects.filter(topic_id=id).values('id', 'question', 'option_a', 'option_b', 'option_c', 'option_d', 'right_option')
    mcqs = list(mcqs) 
    return JsonResponse ({'mcqs': mcqs})   