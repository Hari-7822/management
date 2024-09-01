from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages

from students.models import Student #for Student_profile
from students.models import user #for User_profile
from students.forms import StudentForm


def list(request):
    list = user.objects.all()
    return (request, 'list.j2', {'user': list})

def Add_Student(request):
    if request.method == "POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            stu = form.cleaned_data['name']
            messages.success(request, f"Student {stu} is added successfully") if form.save() else messages.error(request, f"Student not added");form=StudentForm(request.POST)
    else:
        form = StudentForm()

    return render(request, 'forms/student.j2', {form:'form'})

def Edit_Student(request):
    if request.method == "POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            if not Student.objects.filter(id = form.cleaned_data['roll_number']):
                form.save()
            else:
                messages.error(request, f'Roll number {id} already exists!')
                # form=StudentForm(request.POST)
    else:
        form = StudentForm()
    return render(request, 'forms/student.j2', {'form':form})


def View_Student(request, *input):
    query=get_object_or_404(Student, username=input.name, id=input.id)
    return render(request, 'student_view.j2', {'data':query})


def PrintStudent(request, *input):
    query = get_object_or_404(Student, id= input.id, username= input.name)
    return render(request, 'print.j2', {'data':query})