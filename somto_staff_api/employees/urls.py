from django.urls import path
from .views import ManagerList, InternList, StaffRoleDetail

urlpatterns =[
    path('managers/', ManagerList.as_view()),
    path('interns/', InternList.as_view()),
    path('staff/<int:pk>/role/', StaffRoleDetail.as_view()),
]