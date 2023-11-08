from django.contrib import admin
from apps.main import models


# Register your models here.
@admin.register(models.Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ["class_name", "year_of_foundation", "is_active", "classroom_teacher"]
    ordering = "year_of_foundation",


@admin.register(models.ClassStudent)
class ClassStudentAdmin(admin.ModelAdmin):
    list_display = ["student_id", "class_name"]
    ordering = "class_name",


@admin.register(models.ClassSubject)
class ClassSubjectAdmin(admin.ModelAdmin):
    list_display = ["subject_id", "class_name"]
    ordering = "class_name",


@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["name"]
    ordering = "name",


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "student_id",
        "first_name",
        "last_name",
        "date_of_birth",
        "is_active",
        "is_graduated",
        "year_of_graduate",
        "comment",
        "date_of_create",
        "date_of_update",
        "gender",
        "parent"
    ]
    ordering = "student_id",


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        "teacher_id",
        "first_name",
        "last_name",
        "date_of_birth",
        "is_classroom",
        "phone",
        "is_active",
        "comment",
        "date_of_create",
        "date_of_update",
        "gender",
        "subject"
    ]
    ordering = "teacher_id",


@admin.register(models.Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = [
        "parent_id",
        "mother_full_name",
        "father_full_name",
        "responsible_person",
        "mother_contact_phone",
        "father_contact_phone",
        "rp_contact_phone",
        "comment",
        "address",
        "date_of_create",
        "date_of_update"
    ]
    ordering = "parent_id",


@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = [
        "staff_id",
        "first_name",
        "last_name",
        "date_of_birth",
        "phone",
        "is_active",
        "comment",
        "date_of_create",
        "date_of_update",
        "gender",
        "profession"
    ]
    ordering = "staff_id",


@admin.register(models.Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(models.Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(models.Management)
class ManagementAdmin(admin.ModelAdmin):
    list_display = [
        "management_id",
        "first_name",
        "last_name",
        "date_of_birth",
        "is_active",
        "comment",
        "date_of_create",
        "date_of_update",
        "gender",
        "responsibility",
    ]
    ordering = "management_id",


@admin.register(models.PublicMessage)
class PublicMessageAdmin(admin.ModelAdmin):
    list_display = ["public_message_id", "title", "text", "is_active", "author"]
    ordering = "-public_message_id",
