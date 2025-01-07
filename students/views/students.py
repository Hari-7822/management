from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from django.apps import apps
from django.shortcuts import render, get_object_or_404

from students.models import Student 
from students.models import user 
from students.forms import StudentForm

from datetime import datetime

@login_required(login_url="user/login/")
def index(request):
    list = user.objects.all()
    return render(request, 'list.j2', {'user': list})

@login_required(login_url="user/login")
# @permission_required()
def Add_Student(request):
    if request.method == "POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            stu_name = form.cleaned_data['name']
            stu_age = form.cleaned_data['age']
            stu_grade = form.cleaned_data['grade']
            stu_roll = form.cleaned_data['roll_number']
            stu_fname = form.cleaned_data['father_name']
            stu_fage = form.cleaned_data['father_age']
            stu_focc = form.cleaned_data['father_occupation']
            stu_mname = form.cleaned_data['mother_name']
            stu_mage = form.cleaned_data['mother_age']
            stu_mocc = form.cleaned_data['mother_occupation']
            # stu_cre = form.cleaned_data['created_by']
            form.save(user=request.user)
            # Student.objects.create(name=stu_name, age=stu_age, grade=stu_grade, roll_number=stu_roll, father_name=stu_fname, father_age=stu_fage, father_occupation=stu_focc, mother_name=stu_mname, mother_age=stu_mage, mother_occupation = stu_mocc)
            print(stu_name)
            # messages.success(request, f"Student {stu_name} is added successfully") if form.save() else messages.error(request, f"Student not added");form=StudentForm(request.POST)
            return redirect("list/")
    else:
        form = StudentForm()

    return render(request, 'forms/student.j2', {'form':form})

# def Edit_Student(request):
#     if request.method == "POST":
#         form=StudentForm(request.POST)
#         if form.is_valid():
#             if not Student.objects.filter(id = form.cleaned_data['roll_number']):
#                 form.save()
#             else:
#                 messages.error(request, f'Roll number {id} already exists!')
#                 # form=StudentForm(request.POST)
#     else:
#         form = StudentForm()
#     return render(request, 'forms/student.j2', {'form':form})


def Student_View(request):
    data = Student.objects.all()
    return render(request, 'student_view.j2', {'student': data})


# def PrintStudent(request, *input):
#     query = get_object_or_404(Student, id= input.id, username= input.name)
#     return render(request, 'print.j2', {'data':query})


@login_required(login_url="user/login")
def info(request):
    return "Info"

@login_required(login_url="user/login")
def perms(request):
    return "Info"

@login_required(login_url="user/login")
def settings(request):
    return "Info"