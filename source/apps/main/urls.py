from django.urls import path, re_path
from .views import view_home, ClassList, ClassDetail, ParentDetail, TeacherList
import config.settings as settings

urlpatterns = [
    path("", view_home, name="home"),
    path("classes/active/", ClassList.as_view(), name="classes"),
    path("classes/archive/", ClassList.as_view(), name="class_archive"),
    re_path(r"^class/(?P<class_name>\w+)/", ClassDetail.as_view(), name="student_class"),
    path("parent/<int:pk>/", ParentDetail.as_view(), name="parent"),
    path("teacher/active/", TeacherList.as_view(), name="teachers"),
    path("teacher/archive/", TeacherList.as_view(), name="teacher_archive"),

]

if settings.DEBUG:
    ...
