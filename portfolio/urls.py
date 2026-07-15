from django.urls import path
from .views import *

urlpatterns = [
    path("profile/", ProfileList.as_view()),
    path("skills/", SkillList.as_view()),
    path("projects/", ProjectList.as_view()),
    path("education/", EducationList.as_view()),
]