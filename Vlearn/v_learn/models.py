from django.db import models

# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.course_name or ''


class Topic(models.Model):
    course_name = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True)
    topic = models.CharField(max_length=264, null=True)
    content = models.CharField(max_length=10000, null=True)

    def __str__(self):
        return self.topic or ''


class Mcq(models.Model):
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,null=True)
    question = models.CharField(max_length=264,null=True)
    option_a = models.CharField(max_length=264,null=True)
    option_b = models.CharField(max_length=264,null=True)
    option_c = models.CharField(max_length=264,null=True)
    option_d = models.CharField(max_length=264,null=True)
    right_option = models.CharField(max_length=264,null=True)

    def __str__(self):
        return self.question or ''

class VlearnUser(models.Model):
    firstName = models.CharField(max_length=264,null=True)
    lastName = models.CharField(max_length=264,null=True)
    emailid = models.CharField(max_length=264,null=True)
    courseList = models.CharField(max_length=264,null=True)
    percentage =  models.CharField(max_length=264,null=True)

    def __str__(self):
        return self.firstName or ''

