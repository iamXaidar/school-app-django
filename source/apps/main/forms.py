from django import forms
from apps.main.models import Subject, Gender, Teacher, Profession
from apps.main.utils import make_year_fields, SCHOOL_FOUNDATION_YEAR, class_years


class FilterForm(forms.Form):
    gender = forms.ModelChoiceField(queryset=Gender.objects.all(), required=False, label="GENDER")
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(), required=False, label="SUBJECT")
    year_of_foundation = forms.ChoiceField(choices=make_year_fields(SCHOOL_FOUNDATION_YEAR, class_years), required=False)
    classroom_teacher = forms.ModelChoiceField(queryset=Teacher.objects.all(), required=False, label="TEACHER")
    profession = forms.ModelChoiceField(queryset=Profession.objects.all(), required=False, label="PROFESSION")


