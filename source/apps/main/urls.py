from django.urls import path, re_path
from .views import view_home, ClassList, ClassDetail, ParentDetail, TeacherList, StaffList, ManagementList

urlpatterns = [
    path("", view_home, name="home"),
    path("classes/active/", ClassList.as_view(), name="classes"),
    path("classes/archive/", ClassList.as_view(), name="class_archive"),
    re_path(r"^class/(?P<class_name>\w+)/", ClassDetail.as_view(), name="student_class"),
    path("parent/<int:pk>/", ParentDetail.as_view(), name="parent"),
    path("teacher/active/", TeacherList.as_view(), name="teachers"),
    path("teacher/archive/", TeacherList.as_view(), name="teacher_archive"),
    path("staff/active/", StaffList.as_view(), name="staff"),
    path("staff/archive/", StaffList.as_view(), name="staff_archive"),
    path("management/active/", ManagementList.as_view(), name="management"),
    path("management/archive/", ManagementList.as_view(), name="management_archive"),

]

