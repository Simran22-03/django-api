from rest_framework import generics
from .models import Profile, Skill, Project, Education
from .serializers import (
    ProfileSerializer,
    SkillSerializer,
    ProjectSerializer,
    EducationSerializer,
)


# GET all profiles + POST new profile
class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# GET all skills + POST new skill
class SkillList(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


# GET all projects + POST new project
class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# GET all education + POST new education
class EducationList(generics.ListCreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer