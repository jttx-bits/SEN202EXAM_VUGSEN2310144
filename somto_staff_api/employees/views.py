from django.shortcuts import render
from rest_framework import generics
from .models import Manager, Intern
from .serializers import ManagerSerializer, InternSerializer


class ManagerList(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class InternList(generics.ListCreateAPIView):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer


class StaffRoleDetail(generics.RetrieveAPIView):
    def get_queryset(self):
        return Manager.objects.all().union(Intern.objects.all())

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return Response({"role": instance.get_role()})

# Create your views here.
