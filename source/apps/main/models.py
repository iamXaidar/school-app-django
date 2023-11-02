from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse


# Class models
class ClassSubject(models.Model):
    class_subject_id = models.BigAutoField(primary_key=True)
    subject_id = models.ForeignKey("Subject", on_delete=models.DO_NOTHING, db_column="subject_id")
    class_name = models.ForeignKey("Class", on_delete=models.DO_NOTHING, db_column="class_name")

    def __str__(self):
        return f"{self.class_name}"

    class Meta:
        db_table = "class_subject"
        unique_together = [["subject_id", "class_name"]]


class ClassStudent(models.Model):
    class_student_id = models.BigAutoField(primary_key=True)
    student_id = models.ForeignKey("Student", on_delete=models.DO_NOTHING, db_column="student_id")
    class_name = models.ForeignKey("Class", on_delete=models.DO_NOTHING, db_column="class_name")

    def __str__(self):
        return f"{self.class_name}"

    class Meta:
        db_table = "class_student"
        unique_together = [["student_id", "class_name"]]


class Class(models.Model):
    class_name = models.CharField(primary_key=True, max_length=20, validators=[MinLengthValidator(14)])
    year_of_foundation = models.CharField(max_length=4, validators=[MinLengthValidator(4)])
    is_active = models.BooleanField(default=True)
    classroom_teacher = models.ForeignKey("Teacher", on_delete=models.DO_NOTHING)
    students = models.ManyToManyField("Student", related_name="class_student_set", through=ClassStudent)
    subjects = models.ManyToManyField("Subject", related_name="class_subject_set", through=ClassSubject)

    def __str__(self):
        return self.class_name

    def get_absolute_url(self):
        return reverse(viewname="student_class", kwargs={"class_name": self.class_name})

    class Meta:
        db_table = "class"
        verbose_name = "Class"
        verbose_name_plural = "Classes"


# Persons models
class PersonsCommonInfo(models.Model):
    """Abstract model class contains common information about persons"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    comment = models.TextField(null=True, blank=True)
    date_of_create = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)
    gender = models.ForeignKey("Gender", on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True


class Student(PersonsCommonInfo):
    student_id = models.BigAutoField(primary_key=True)
    is_graduated = models.BooleanField(default=False)
    year_of_graduate = models.CharField(null=True, blank=True, max_length=4, validators=[MinLengthValidator(4)])
    parent = models.ForeignKey("Parent", on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "student"


class Teacher(PersonsCommonInfo):
    teacher_id = models.BigAutoField(primary_key=True)
    is_classroom = models.BooleanField(null=True, blank=True, default=False)
    phone = models.CharField(null=True, blank=True, max_length=15, validators=[MinLengthValidator(7)])
    subject = models.ForeignKey("Subject", on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "teacher"


class Parent(models.Model):
    parent_id = models.BigAutoField(primary_key=True)
    mother_full_name = models.CharField(null=True, blank=True, max_length=50)
    father_full_name = models.CharField(null=True, blank=True, max_length=50)
    responsible_person = models.CharField(null=True, blank=True, max_length=50)
    mother_contact_phone = models.CharField(null=True, blank=True, max_length=15, validators=[MinLengthValidator(7)])
    father_contact_phone = models.CharField(null=True, blank=True, max_length=15, validators=[MinLengthValidator(7)])
    rp_contact_phone = models.CharField(null=True, blank=True, max_length=15, validators=[MinLengthValidator(7)])
    comment = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    date_of_create = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.responsible_person is not None:
            return f"{self.responsible_person}"
        else:
            return f"{str(self.father_full_name).split()[0]} AND {str(self.mother_full_name).split()[0]}"

    def get_absolute_url(self):
        return reverse(viewname="parent", kwargs={"pk": self.parent_id})

    class Meta:
        db_table = "parent"


class Staff(PersonsCommonInfo):
    staff_id = models.BigAutoField(primary_key=True)
    phone = models.CharField(null=True, blank=True, max_length=15, validators=[MinLengthValidator(7)])
    profession = models.ForeignKey("Profession", on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.first_name}_{self.last_name}"

    class Meta:
        db_table = "staff"
        verbose_name_plural = "Staff"


# Properties models
class Gender(models.Model):
    gender_id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=6)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "gender"


class Profession(models.Model):
    profession_id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "profession"


class Subject(models.Model):
    subject_id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "subject"
