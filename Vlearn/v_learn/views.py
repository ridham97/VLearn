from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from v_learn.models import Course, Topic, Mcq


def Detail(request):
    return render(request, "Detail.html")


def Content(request):
    return render(request, "Conttent.html")


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


# def vmodule(request):
#     return render(request, "v-module.html")


# def vquiz(request):
#     return render(request, "v-quiz.html")


# def vsimulator(request):
#     return render(request, "v-simulator.html")


# def vvideotopic(request):
#     return render(request, "v-video_topic.html")


def Homepage(request):
    course_table = Course.objects.order_by('course_name')
    my_course_table = {"insert_course_table": course_table}
    return render(request, "Homepage.html", context=my_course_table)


def adminform(request):
    topic_data = Course.objects.all()
    topic_list = {"insetTopicData": topic_data}

    coursename = request.POST.get("course_name")
    topicValue = request.POST.get("TopicValue")
    contentValue = request.POST.get("ContentValue")
    save_data = Topic(course_name=coursename, topic=topicValue,
                      content=contentValue)
    save_data.save()
    return render(request, "admin.html", context=topic_list)
