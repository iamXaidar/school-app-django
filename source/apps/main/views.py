from apps.main.models import *
from apps.main import utils
from django.db import models
from django.shortcuts import render, HttpResponse
from django.views import generic
from apps.main.forms import FilterForm


def view_home(request):
    context = {"menu": utils.main_menu}
    return render(request=request, template_name="main/index.html", context=context)


# Create your views here.
class ClassList(generic.ListView, utils.GeneralContext):
    queryset = Class.objects.select_related("classroom_teacher")
    template_name = "main/class_list.html"
    context_object_name = "classes"
    paginate_by = 25

    def get_queryset(self):
        is_active = True
        if self.request.path == "/classes/archive/":
            is_active = False

        qs = super().get_queryset().filter(is_active=is_active).only(
            "class_name", "year_of_foundation",
            "classroom_teacher__first_name",
            "classroom_teacher__last_name"
        ).annotate(students_count=models.Count("students"))

        if self.request.GET and not self.request.GET.get("page"):
            kwargs = {item: self.request.GET.get(item) for item in self.request.GET if self.request.GET.get(item)}
            print(kwargs)
            qs = qs.filter(**kwargs)
        return qs

    def get_context_data(self, *args, **kwargs):
        title = "Classes"
        general_context = self.get_general_context()  # contains other context
        main_context = super().get_context_data(*args, **kwargs)
        context = dict(list(general_context.items()) + list(main_context.items()))
        form = FilterForm()

        if self.request.path == "/class/archive/":
            title = "Classes archive"
        context["title"] = title
        context["forms"] = form
        return context


class ClassDetail(generic.DetailView, utils.GeneralContext):
    model = Class
    template_name = "main/class_detail.html"
    context_object_name = "class_students"
    slug_url_kwarg = "class_name"
    slug_field = "class_name"

    def get_object(self, queryset=None):
        main_obj = super().get_object()
        related_objs = main_obj.students.select_related("parent", "gender")
        # Filter
        if self.request.GET:
            gender_id = self.request.GET.get("gender")
            if gender_id:
                related_objs = related_objs.filter(gender=gender_id)

        related_objs = related_objs.only(
            "first_name", "last_name", "date_of_birth", "is_graduated", "is_active", "comment", "gender", "parent",
            "gender__name", "parent__mother_full_name", "parent__father_full_name", "parent__responsible_person",
            "parent__address"
        )
        return related_objs

    def get_context_data(self, **kwargs):
        custom_context = super().get_general_context()
        main_context = super().get_context_data(**kwargs)
        context = dict(list(custom_context.items()) + list(main_context.items()))
        form = FilterForm()

        context["title"] = self.request.path.split("/")[-2]
        context["forms"] = form
        return context


class ParentDetail(generic.DetailView, utils.GeneralContext):
    model = Parent
    template_name = "main/parent_detail.html"
    context_object_name = "parent"

    def get_context_data(self, **kwargs):
        general_context = super().get_general_context()
        context = super().get_context_data(**kwargs)
        context["title"] = context["parent"]
        return dict(list(general_context.items()) + list(context.items()))


class TeacherList(generic.ListView, utils.GeneralContext):
    queryset = Teacher.objects.select_related("gender", "subject").only(
        "first_name", "last_name", "date_of_birth", "is_classroom", "phone", "gender", "subject", "comment")
    template_name = "main/teacher_list.html"
    context_object_name = "teachers"

    def get_queryset(self):
        is_active = True
        if self.request.path == "/teacher/archive/":
            is_active = False
        qs = super().get_queryset().filter(is_active=is_active)
        # Filter
        if self.request.GET and not self.request.GET.get("page"):
            # We need to create a dict with filter params and values if they exist
            kwargs = {item: self.request.GET.get(item) for item in self.request.GET if self.request.GET.get(item)}
            qs = super().get_queryset().filter(**kwargs)

        return qs

    def get_context_data(self, **kwargs):
        general_context = super().get_general_context()
        main_context = super().get_context_data(**kwargs)
        context = dict(list(general_context.items()) + list(main_context.items()))
        title = "Teachers"
        form = FilterForm()
        if self.request.path == "/teacher/archive/":
            title = "Teachers archive"

        context["title"] = title
        context["forms"] = form

        return context

