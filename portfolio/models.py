from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    semester = models.CharField(max_length=50)
    description = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    resume = models.FileField(upload_to="resume/", blank=True, null=True)
    image = models.ImageField(upload_to="profile/", blank=True, null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github = models.URLField(blank=True)
    live_demo = models.URLField(blank=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    college = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    year = models.CharField(max_length=20)
    cgpa = models.CharField(max_length=20)

    def __str__(self):
        return self.college