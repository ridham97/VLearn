from django.db import models

# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.course_name


class Javascript(models.Model):
    topic = models.CharField(max_length=264)
    content = models.CharField(max_length=264)

    def __str__(self):
        return self.topic


class Mcq(models.Model):
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    topic = models.ForeignKey(Javascript, on_delete=models.CASCADE)
    question = models.CharField(max_length=264)
    option_a = models.CharField(max_length=264)
    option_b = models.CharField(max_length=264)
    option_c = models.CharField(max_length=264)
    option_d = models.CharField(max_length=264)
    right_option = models.CharField(max_length=264)

    def __str__(self):
        return self.question
